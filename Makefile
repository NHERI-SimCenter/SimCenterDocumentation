
include Makefile.in

SPHINXOPTS    ?= 
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = ./docs
BUILDDIR      = ./build/$(1)

# use shell pattern expansion to remove 'Tool' from R2DTool-Documentation
PUBLDIR = $(shell v="$(SIMDOC_APP)"; echo "../$${v%Tool}-Documentation/docs/")

# Directories to remove when cleaning
CLEANDIR      = _sources _static _images common

CSVDIR  = docs/common/reqments/_out/
JSONDIR = docs/common/reqments/data/

export SIMCENTER_DEV = $(shell pwd | xargs dirname)
#-Examples-------------------------------------------------
EXPDIR = ./docs/common/user_manual/examples/desktop
EXPSRC = ${SIMCENTER_DEV}/$(SIMDOC_APP)/Examples
RENDRE = rendre -v -D '$(EXPSRC)/index.json'
# Create list of files
EXAMPLES = $(shell $(RENDRE) -l examples.yaml\#/$(SIMDOC_APP) path -j ' ' -- $(EXPSRC)/./\%%:doc)


#-Help-----------------------------------------------------
help:
	@echo 'usage: make <app> <target>'
	@echo '   or: make <all|update>'
	@printf '\n'
	@echo 'where <app> is one of:'
	@printf '    {pelicun, qfem, r2d, pbe, we, ee, rtm}\n\n'
	@echo 'and <target> is one of:'
	@echo '    web    Run html target with build directory'
	@echo '           set to app publishing repository.'
	@echo '    html   Run html target in dev build directory.'
	@echo '    latex  Run latex target in dev build directory.'
	@printf "\nRunning 'make all' will run 'make <app> html'\n"
	@printf "for all <app> options listed above.\n\n"
#----------------------------------------------------------

.PHONY: help Makefile pbe r2d qfem we ee rtm hydro html pdf latexpdf latex 

# Export target-specific environment vars
ee:      export SIMDOC_APP=EE-UQ
we:      export SIMDOC_APP=WE-UQ

r2d:     export SIMDOC_APP=R2DTool

pbe:     export SIMDOC_APP=PBE
hydro:   export SIMDOC_APP=Hydro
qfem:    export SIMDOC_APP=quoFEM
pelicun: export SIMDOC_APP=pelicun
rtm: export SIMDOC_APP=requirements


export SIMDOC_APP


# LaTeX path variables
export TEXINPUTS:=${SIMCENTER_DEV}/SimCenterDocumentation/latex//:./build/${SIMDOC_APP}/latex//:${TEXINPUTS}
#export TEXINPUTS:=/usr/share/texmf-dist//:${TEXINPUTS}
export BSTINPUTS:=../texmf//:${BSTINPUTS}


all:
	make pelicun html 2>&1 | grep 'build succ'
	make qfem html 2>&1 | grep 'build succ'
	make r2d html 2>&1 | grep 'build succ'
	make pbe html 2>&1 | grep 'build succ'
	make we html 2>&1 | grep 'build succ'
	make ee html 2>&1 | grep 'build succ'


hydro pelicun pbe rtm:
	$(eval SIMDOC_APP=$(SIMDOC_APP))


r2d qfem we ee:
	$(eval SIMDOC_APP=$(SIMDOC_APP))


web:
	find . -type f -name "*.rst" -exec touch {} +
	@echo cleaning directories: $(addprefix $(PUBLDIR),$(CLEANDIR))
	rm -fr $(addprefix $(PUBLDIR),$(CLEANDIR))
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(PUBLDIR)" $(O)
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(PUBLDIR)" $(O)
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(PUBLDIR)" $(O)

spell:
	@$(SPHINXBUILD) -b spelling "$(SOURCEDIR)" "$(call BUILDDIR,$(SIMDOC_APP))/html" $(O)

html:
	for i in $(JSONDIR)/*.json; do \
	    file_name="$${i##*/}"; \
	    make $(CSVDIR)/$${file_name%.*}.csv; \
	done
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(call BUILDDIR,$(SIMDOC_APP))/html" $(O)


latex:
	@$(SPHINXBUILD) -b latex "$(SOURCEDIR)" "$(call BUILDDIR,$(SIMDOC_APP))/latex" $(O)


pdf:
	mkdir -p $(call BUILDDIR,$(SIMDOC_APP))/pdf/
	$(PDFLATEX) \
	-output-directory="$(call BUILDDIR,$(SIMDOC_APP))/pdf/" \
	$(join $(call BUILDDIR,$(SIMDOC_APP)),/latex/*.tex)

latexpdf:
	make latex
	make pdf

update:
	pip install -U -r requirements.txt

$(CSVDIR)/%.csv: $(JSONDIR)/%.json
	python3 ./scripts/json2csv.py \
		-Eqfem $(SIMCENTER_DEV)/quoFEM/Examples/qfem*/src/input.json \
		-Eeeuq $(SIMCENTER_DEV)/EE-UQ/Examples/eeuq-*/src/input.json \
		-Eweuq $(SIMCENTER_DEV)/WE-UQ/Examples/weuq-*/src/input.json \
		-Epbdl $(SIMCENTER_DEV)/PBE/Examples/pbdl-*/src/input.json \
		-Er2dt $(SIMCENTER_DEV)/R2DTool/Examples/E*/input.json \
		< '$<' > '$@'


