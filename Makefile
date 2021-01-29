setup:
	pip install mkdocs-material

serve:
	mkdocs serve

deploy:
	mkdocs gh-deploy --force
