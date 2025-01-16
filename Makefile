run:
	quarto preview

build: clean
	quarto render

clean:
	-find . -name "*_files" | xargs -I {} rm -R "{}"
	-find . -name "*.html" | xargs -I {} rm "{}"
