SOURCE=WEUQ-Document.tex

doc: 
	make WEUQ-Document.pdf
	echo "done!"

links: simcenterdocumentation.cls simcenterfooter.png simcenterlogo.pdf

simcenterdocumentation.cls: ../Latex/LatexClass/simcenterdocumentation.cls
	ln -s ../Latex/LatexClass/simcenterdocumentation.cls .

simcenterfooter.png: ../Latex/LatexClass/simcenterfooter.png
	ln -s ../Latex/LatexClass/simcenterfooter.png .

simcenterlogo.pdf: ../Latex/LatexClass/simcenterlogo.pdf
	ln -s ../Latex/LatexClass/simcenterlogo.pdf .

WEUQ-Document.pdf: ${SOURCE} links
	pdflatex  WEUQ-Document.tex
	biber  WEUQ-Document
	pdflatex  WEUQ-Document.tex
	pdflatex  WEUQ-Document.tex

