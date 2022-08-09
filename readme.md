# FSDL Website

This website came online in January 2021.

It uses `mkdocs`, which you can set up with `make setup`.

To develop locally, run `make serve` and edit the files.

To deploy, push `main` branch to github and it will deploy via github action, or manually run `make deploy`.

## Processing lecture notes

Download Google Doc as `input.docx`, then run:

```
pandoc --extract-media=. input.docx -o output.md
cat output.md | sed 's/^#/##/' | sed 's/^ *> //g' | sed s'/{.underline}//g' | sed 's/\[\[/[/g' | sed 's/\]\]/]/g' | sed 's/{width=.*}//g' | sed 's/{width=.*"$//' | sed 's/^height=.*"}//' > output.md 
```
