1. Update `.env.example` with your credentials and rename it to `.env`. If you don't have a Modal token yet, run `make modal-token`.
2. Set up a Python environment. If you're using pyenv-virtualenv, you can just run `make venv`.
3. `make it-all` to generate summaries for all lectures in `bootcamp-lectures.json`.

See the `Makefile` and `app.py` for details.
