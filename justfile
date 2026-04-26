help:
    @just --list

list_preview:
    # List all files that are not marked as draft in the preview directory.
    rg --files-without-match "draft:" --glob "*.qmd" ./src/01_teoria/ --sort path
    rg --files-without-match "draft:" --glob "*.qmd" ./src/02_problemas/ --sort path
    rg --files-without-match "draft:" --glob "*.qmd" ./src/03_practicas/ --sort path
    rg --files-without-match "draft:" --glob "*.qmd" ./src/04_examenes/ --sort path

list_index:
    grep < _output/index.html './src/' | sed -E 's/.*html">(.+)<\/a.*/\1/g' | grep --color=auto '<b>'

# Publish does NOT re-render.
publish: list_index
    read PRESS_KEY_TO_CONTINUE
    quarto publish gh-pages --no-prompt --no-browser --no-render

# Command for previewing the site locally.
preview:
    quarto preview --host localhost --port 7777

# Command for previewing the site remotely.
remote_preview:
    quarto preview --host 0.0.0.0 --port 7777

render *files:
    quarto render {{files}}
