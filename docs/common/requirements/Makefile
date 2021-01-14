# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= 
SPHINXBUILD   ?= sphinx-build
#SPHINXBUILD   ?= python3 -m sphinx
SOURCEDIR     = .
BUILDDIR      = ./web

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

RTM:
	make clean
	rm -fr ../../../../RTM-Documentation/docs/_sources
	rm -fr ../../../../RTM-Documentation/docs/_static
	rm -fr ../../../../RTM-Documentation/docs/_images
	rm -fr ../../../../RTM-Documentation/docs/common
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" ../../../../RTM-Documentation/docs $(O)


.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
