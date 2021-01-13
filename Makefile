#SHELL = /bin/bash -O globstar

include Makefile.in

SPHINXOPTS    ?= 
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = ./docs
BUILDDIR      = ./build/$(1)
PUBLDIR       = ../$(1)-Documentation/docs/

# Directories to remove when cleaning
CLEANDIR      = _sources _static _images common

#-Examples-------------------------------------------------
EXPDIR = ./docs/common/user_manual/examples/desktop
EXPSRC = ${SIMCENTER_DEV}/$(SIMDOC_APP)/examples
RENDRE = rendre -D $(EXPSRC)/examples.json

#-Help-----------------------------------------------------
help:
	@echo 'usage: make <app> <target>'
	@echo '   or: make <all|update>'
	@printf '\n'
	@echo 'where <app> is one of:'
	@printf '    {pelicun, qfem, rdt, pbe, we, ee}\n\n'
	@echo 'and <target> is one of:'
	@echo '    web    Run html target with build directory'
	@echo '           set to app publishing repository.'
	@echo '    html   Run html target in dev build directory.'
	@echo '    latex  Run latex target in dev build directory.'
	@printf "\nRunning 'make all' will run 'make <app> html'\n"
	@printf "for all <app> options listed above.\n\n"

#----------------------------------------------------------

.PHONY: help Makefile pbe rdt qfem we ee html pdf latexpdf latex

ee:      export SIMDOC_APP=EE-UQ
we:      export SIMDOC_APP=WE-UQ
rdt:     export SIMDOC_APP=RDT
pbe:     export SIMDOC_APP=PBE
qfem:    export SIMDOC_APP=quoFEM
pelicun: export SIMDOC_APP=pelicun
export SIMDOC_APP
export TEXINPUTS:=${SIMCENTER_DEV}/texmf//:./build/${SIMDOC_APP}/latex//:/${TEXINPUTS}
export TEXINPUTS:=~/texlive/2020//:${TEXINPUTS} 
export BSTINPUTS:=../texmf//:${BSTINPUTS} 

all:
	make pelicun html
	make qfem html
	make rdt html
	make pbe html
	make we html
	make ee html

pelicun rdt pbe ee:
	# $(eval SIMDOC_APP=$(SIMDOC_APP))

qfem we:
	# $(eval SIMDOC_APP=$(SIMDOC_APP))
	# sync example files
	-rsync -Rcv $(addprefix $(EXPSRC)/./,$(shell $(RENDRE) -l examples.yaml#/$(SIMDOC_APP) path -j ' ' -- \%%:doc))  $(EXPDIR)

web:
	@echo removing $(addprefix $(call PUBLDIR,$(SIMDOC_APP)),$(CLEANDIR))
	rm -fr $(addprefix $(call PUBLDIR,$(SIMDOC_APP)),$(CLEANDIR))
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" $(call PUBLDIR,$(SIMDOC_APP)) $(O)

html:
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" $(call BUILDDIR,$(SIMDOC_APP))/html $(O)


latex:
	@$(SPHINXBUILD) -b latex "$(SOURCEDIR)" $(call BUILDDIR,$(SIMDOC_APP))/latex $(O)


pdf:
	mkdir -p $(call BUILDDIR,$(SIMDOC_APP))/pdf/
	$(PDFLATEX) \
	-output-directory="$(call BUILDDIR,$(SIMDOC_APP))/pdf/" \
	$(call BUILDDIR,$(SIMDOC_APP))/latex/*.tex

latexpdf:
	make latex
	make pdf


update:
	pip install -r requirements.txt 

