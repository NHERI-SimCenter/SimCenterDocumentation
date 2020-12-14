#
# make RDT html
SHELL = /bin/bash -O globstar


SPHINXOPTS    ?= 
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = ./docs
BUILDDIR      = ./build/$(1)
PUBLDIR       = ../$(1)-Documentation/docs/

# Directories to remove when cleaning
CLEANDIR      = _sources _static _images common

# define build_dir
# publish: export BUILDDIR = ../$(1)-Documentation/docs
# %:       export BUILDDIR = ./build/$(1)
# endef

help:
	@echo 'usage: make <app> <target>'
	@printf '\n'
	@echo 'where <app> is one of:'
	@echo '    qfem'
	@echo '    rdt'
	@echo '    pbe'
	@echo '    ee'
	@echo '    we'
	@echo '    all   Make all of the above'
	@echo ''
	@echo 'and <target> is one of:'
	@echo '    web'
	@echo '    html'
	@echo '    latex'
	@echo ''

pandoc:
	# echo **/*.rst | sed -e 's/ /\n/g'
	pandoc **/*.rst -o doc.pdf


ee:     export SIMDOC_APP=EE-UQ
we:     export SIMDOC_APP=WE-UQ
rdt:    export SIMDOC_APP=RDT
pbe:    export SIMDOC_APP=PBE
qfem: export SIMDOC_APP=quoFEM
export SIMDOC_APP

# .PHONY: help Makefile pbe rdt qfem we ee

rdt pbe qfem we ee:
	$(eval SIMDOC_APP=$(SIMDOC_APP))

web:
	@echo removing $(addprefix $(call PUBLDIR,$(SIMDOC_APP)),$(CLEANDIR))
	rm -fr $(addprefix $(call PUBLDIR,$(SIMDOC_APP)),$(CLEANDIR))
	python3 test.py

html:
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" $(call BUILDDIR,$(SIMDOC_APP)) $(O)


.PHONY: help Makefile pbe rdt qfem we ee html




# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
