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

R2D:
	make clean
	rm -fr ../../RDT-Documentation/docs/_sources
	rm -fr ../../RDT-Documentation/docs/_static
	rm -fr ../../RDT-Documentation/docs/_images
	rm -fr ../../RDT-Documentation/docs/common
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" ../../RDT-Documentation/docs $(O)

PBE:
	make clean
	rm -fr ../.../PBE-Documentation/docs/_sources
	rm -fr ../../PBE-Documentation/docs/_static
	rm -fr ../../PBE-Documentation/docs/_images
	rm -fr ../../PBE-Documentation/docs/common
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" ../../PBE-Documentation/docs $(O)

quoFEM:
	make clean
	rm -fr ../.../quoFEM-Documentation/docs/_sources
	rm -fr ../../quoFEM-Documentation/docs/_static
	rm -fr ../../quoFEM-Documentation/docs/_images
	rm -fr ../../quoFEM-Documentation/docs/common
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" ../../quoFEM-Documentation/docs $(O)

EE:
	make clean
	rm -fr ../../EE-UQ-Documentation/docs/_sources
	rm -fr ../../EE-UQ-Documentation/docs/_static
	rm -fr ../../EE-UQ-Documentation/docs/_images
	rm -fr ../../EE-UQ-Documentation/docs/common
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" ../../EE-UQ-Documentation/docs $(O)

WE:
	make clean
	rm -fr ../../WE-UQ-Documentation/docs/_sources
	rm -fr ../../WE-UQ-Documentation/docs/_static
	rm -fr ../../WE-UQ-Documentation/docs/_images
	rm -fr ../../WE-UQ-Documentation/docs/common
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" ../../WE-UQ-Documentation/docs $(O)

HydroUQ:
	make clean
	rm -fr ../../HydroUQ-Documentation/docs/_sources
	rm -fr ../../HydroUQ-Documentation/docs/_static
	rm -fr ../../HydroUQ-Documentation/docs/_images
	rm -fr ../../HydroUQ-Documentation/docs/common
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" ../../HydroUQ-Documentation/docs $(O)

Bootcamp:
	make clean
	rm -fr ../../SimCenterBootcamp2020/docs/_sources
	rm -fr ../../SimCenterBootcamp2020/docs/_static
	rm -fr ../../SimCenterBootcamp2020/docs/_images
	rm -fr ../../SimCenterBootcamp2020/docs/common
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" ../../SimCenterBootcamp2020/docs $(O)

.PHONY: help Makefile expl


# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
