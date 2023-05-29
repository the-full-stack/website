from pathlib import Path

import modal

MOUNT_PATH = Path("/") / "vol"
VOLUME_NAME = "lecture-notes-creator-videos"
volume = modal.SharedVolume().persist(VOLUME_NAME)

target_dir = Path("..") / "docs" / "llm-bootcamp" / "spring-2023"

image = (
    modal.Image.debian_slim()
    .pip_install(
        [
            "requests",
            "youtube-transcript-api",
            "openai",
            "tqdm",
            "pytube",
            "ipykernel",
        ]
    )
    .apt_install(
        [
            "ffmpeg",
        ]
    )
)

stub = modal.Stub("lecture-notes-creator", image=image)


@stub.local_entrypoint()
def main(lecture_file="bootcamp-lectures.json", output_dir=target_dir):
    """Writes chapter summaries for each YouTube video lecture in the target file."""
    import json

    output_dir = Path(output_dir)
    output_dir = output_dir.absolute()
    assert output_dir.exists()

    with open(lecture_file) as f:
        lectures = json.load(f)

    for lecture in lectures:
        print("working on", lecture["slug"])

        print("\t::", "pulling chapters and transcripts from youtube")
        chapters = get_chapters_with_transcripts.call(lecture["yt_id"])

        print("\t::", "summarizing each chapter with an LLM")
        summaries = list(
            summarize_chapter.map(
                chapter["transcript"]
                for chapter in chapters
                if "summary" not in chapter
            )
        )
        for chapter, summary in zip(chapters, summaries):
            chapter["summary"] = summary

        print("\t::", "pulling out chapter screens and writing them to remote storage")
        extract_chapter_screens.call(lecture, chapters)

        print("\t::", "writing out chapter summaries in local markdown files")
        # combine the chapter summaries in markdown format
        markdown = write_chapter_summaries_markdown(chapters)

        # write the markdown locally
        with open(output_dir / lecture["slug"] / "chapter_summaries.md", "w") as f:
            f.write(markdown)

        print("\t::", "done!")


@stub.function(shared_volumes={MOUNT_PATH: volume})
def get_chapters_with_transcripts(yt_id: str) -> list[dict]:
    import requests
    from youtube_transcript_api import YouTubeTranscriptApi

    url = f"https://yt.lemnoslife.com/videos?part=chapters&id={yt_id}"
    r = requests.get(url)
    r.raise_for_status()

    chapters = r.json()["items"][0]["chapters"]["chapters"]
    assert len(chapters) >= 0, "Video has no chapters"

    chapters = [
        {k: v for k, v in chap.items() if k != "thumbnails"} for chap in chapters
    ]  # Drop the 'thumbnails' key

    transcript = YouTubeTranscriptApi.get_transcript(yt_id)

    for ind in range(len(chapters)):
        chapter = chapters[ind]
        next_chapter = chapters[ind + 1] if ind < len(chapters) - 1 else {"time": 1e10}
        chapters[ind]["transcript"] = " ".join(
            [
                seg["text"]
                for seg in transcript
                if seg["start"] >= chapter["time"]
                and seg["start"] < next_chapter["time"]
            ]
        )

    return chapters


@stub.function(
    shared_volumes={MOUNT_PATH: volume},
    retries=modal.Retries(max_retries=5, backoff_coefficient=2.0, initial_delay=5.0),
    concurrency_limit=4,
    secret=modal.Secret.from_name("openai-api-key-fsdl"),
)
def summarize_chapter(chapter_transcript: str) -> str:
    import openai

    instructions = f"""
Summarize the following excerpt of a lecture transcript into just a few informative bullet points.
Write from the perspective of the speaker (so don't use the phrase "The speaker").

Transcript excerpt:
{chapter_transcript}""".strip()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": instructions}]
    )

    try:
        return response["choices"][0]["message"]["content"]
    except Exception:
        return "Error, chapter is probably too long to summarize"


@stub.function(shared_volumes={MOUNT_PATH: volume})
def extract_chapter_screens(
    lecture: dict, chapters: list[dict], overwrite=False
) -> None:
    # Download the highest resolution video
    import subprocess

    from pytube import YouTube

    yt_id, slug = lecture["yt_id"], lecture["slug"]
    directory = MOUNT_PATH / slug
    directory.mkdir(exist_ok=True)
    fname = directory / "video.mp4"

    if fname.exists() and not overwrite:
        return

    YouTube(f"https://youtu.be/{yt_id}").streams.get_highest_resolution().download(
        filename=fname
    )

    for ind, chapter in enumerate(chapters):
        chapter_path = directory / f"chapter_{ind}.jpg"
        cmd = (
            f"ffmpeg -y -ss {chapter['time'] + 5} -i {fname} -frames:v 1 {chapter_path}"
        )
        subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        ).communicate()


def write_chapter_summaries_markdown(chapters):
    markdown = "## Chapter Summaries\n\n"
    for ind, chapter in enumerate(chapters):
        markdown += f"### {chapter['title']}\n\n"
        markdown += f"![Chapter {ind} Cover Image](chapter_{ind}.jpg)\n\n"
        markdown += f"{chapter['summary']}\n\n"

    return markdown
