ifneq (,$(wildcard ./.env))
    include .env
    export
endif

.PHONY: help summaries images

help: ## get a list of all the targets, and their short descriptions
	@# source for the incantation: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?##"}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

it-all: secrets summaries images  ## Generate summaries and download images
	@echo "###"
	@echo "# 🥞: done!
	@echo "###"

summaries: modal-auth  ## Generate summaries for all lectures in bootcamp-lectures.json
	modal run app.py --lecture-file bootcamp-lectures.json --output-dir ../docs/llm-bootcamp/spring-2023/

images: modal-auth  ## Download local copies of images for lectures
	modal volume get --force lecture-notes-creator-videos **/*.jpg ../docs/llm-bootcamp/spring-2023/

secrets: modal-auth  ## push secrets from .env to Modal
	modal secret create openai-api-key-fsdl OPENAI_API_KEY=$(OPENAI_API_KEY)

modal-auth: environment ## confirms authentication with Modal, using secrets from `.env` file
	@echo "###"
	@echo "# 🥞: If you haven't gotten a Modal token yet, run make modal_token"
	@echo "###"
	@modal token set --token-id $(MODAL_TOKEN_ID) --token-secret $(MODAL_TOKEN_SECRET)

modal-token: environment ## creates token ID and secret for authentication with modal
	modal token new
	@echo "###"
	@echo "# 🥞: Copy the token info from the file mentioned above into .env"
	@echo "###"

environment: ## installs requirements into current python environment
	python -m pip install -qqq -r requirements.txt

venv: ## creates a pyenv virtualenv if you have it installed
	pyenv virtualenv lecture-notes-creator
	pyenv activate lecture-notes-creator
