# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


github:
	make clean
	rm -fr ../../../TinF-Documentation/docs/_sources
	rm -fr ../../../TinF-Documentation/docs/_static
	rm -fr ../../../TinF-Documentation/docs/_images
	rm -fr ../../../TinF-Documentation/docs/common
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" ../../../TinF-Documentation/docs $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
