.PHONY : default
default : all

.PHONY : all
all : prop

prop:   codedoc.tex references.bib
	pdflatex codedoc.tex
	biber codedoc
	pdflatex codedoc.tex
	pdflatex codedoc.tex

clean:
	rm -f *.aux
	rm -f codedoc.pdf
	rm -f *.lof
	rm -f *.lot
	rm -f *.toc
	rm -f *.log
	rm -f *.bcf
	rm -f *.run.xml
	rm -f *.bbl
	rm -f *.blg
	rm -f *~
	rm -f *.out
	rm -f *.spl
