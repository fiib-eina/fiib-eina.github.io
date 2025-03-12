help:
    just --list

list_preview:
    rg --files-without-match "draft:" --glob "*.qmd" ./src/01_teoria/ --sort path
    rg --files-without-match "draft:" --glob "*.qmd" ./src/02_problemas/ --sort path
    rg --files-without-match "draft:" --glob "*.qmd" ./src/03_practicas/ --sort path

list_index:
    grep < _output/index.html './src/' | sed -E 's/.*html">(.+)<\/a.*/\1/g' | grep --color=auto '<b>'

publish: list_index
    read PRESS_KEY_TO_CONTINUE
    quarto publish gh-pages --no-prompt --no-browser --no-render

preview:
    quarto preview

render *files:
    quarto render {{files}}
