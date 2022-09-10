.Phony: all
all: generate

generate: *.drawio
	printenv SHELL
	/Applications/draw.io.app/Contents/MacOS/draw.io -x -f png -o ./ ./*.drawio

.Phony: clean
clean:
	rm -f *.png