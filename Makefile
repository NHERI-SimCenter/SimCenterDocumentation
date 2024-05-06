
include Makefile.in
SPHINXOPTS    ?= 
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = ./docs
BUILDDIR      = ./build/$(1)
PYTHON 		= python3

# use shell pattern expansion to remove 'Tool' from R2DTool-Documentation
PUBLDIR = $(shell v="$(SIMDOC_APP)"; echo "../$${v%Tool}-Documentation/docs/")

# Directories to remove when cleaning
CLEANDIR      = _sources _static _images common

CSVDIR  = docs/common/reqments/_out_from_json/
JSONDIR = docs/common/reqments/data/

# This environment variable should specify a directory
# that contains both the SimCenterDocumentation/ and
# application source repositories.
export SIMCENTER_DEV = $(shell pwd | xargs dirname)

# Path to widget documentation directory
USER_INPUT_DOC_DIR = docs/common/user_manual/user_inputs_documentation

#-Help-----------------------------------------------------
help:
	@echo 'usage: make <app> <target>'
	@echo '   or: make <all|update>'
	@printf '\n'
	@echo 'where <app> is one of:'
	@printf '    {pelicun, qfem, r2d, pbe, we, hydro, ee, rtm}\n\n'
	@echo 'and <target> is one of:'
	@echo '    web    Run html target with build directory'
	@echo '           set to app publishing repository.'
	@echo '    html   Run html target in dev build directory.'
	@echo '    spell  Run spell checker.'
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
hydro:   export SIMDOC_APP=HydroUQ
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
	make we html 2>&1 | grep 'build succ'
	make ee html 2>&1 | grep 'build succ'
	make pbe html 2>&1 | grep 'build succ'
	make hydro html 2>&1 | grep 'build succ'

pelicun rtm:
	$(eval SIMDOC_APP=$(SIMDOC_APP))

pbe:
	rm -f build/$(SIMDOC_APP)_Examples.json
	make build/$(SIMDOC_APP)_Examples.json
	$(eval SIMDOC_APP=$(SIMDOC_APP))

db:
	@echo Generating temporary files for Damage and Loss Database docs...
	cd ./docs/common/dldb && python3 generate_dldb_doc.py

r2d qfem we ee hydro:
	rm -f build/$(SIMDOC_APP)_Examples.json
	make build/$(SIMDOC_APP)_Examples.json
	$(eval SIMDOC_APP=$(SIMDOC_APP))


example_reference: 
	for i in $(JSONDIR)/*.json; do \
	    json_file="$${i##*/}"; \
	    make $(CSVDIR)/$${json_file%.*}.csv; \
	done

web:
	find . -type f -name "*.rst" -exec touch {} +
	@echo cleaning directories: $(addprefix $(PUBLDIR),$(CLEANDIR))
	rm -fr $(addprefix $(PUBLDIR),$(CLEANDIR))
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(PUBLDIR)" $(O)
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(PUBLDIR)" $(O)
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(PUBLDIR)" $(O)

spell: example_reference
	@$(SPHINXBUILD) -b spelling "$(SOURCEDIR)" "$(call BUILDDIR,$(SIMDOC_APP))/html" $(O)

html: example_reference
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(call BUILDDIR,$(SIMDOC_APP))/html" $(O)


singlehtml: example_reference
	@$(SPHINXBUILD) -b singlehtml "$(SOURCEDIR)" "$(call BUILDDIR,$(SIMDOC_APP))/singlehtml" $(O)


text:
	@$(SPHINXBUILD) -b text "$(SOURCEDIR)" "$(call BUILDDIR,$(SIMDOC_APP))/latex" $(O)


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

examples:
	rm -f build/$(SIMDOC_APP)_Examples.json
	make build/$(SIMDOC_APP)_Examples.json

build/%.json: examples.yaml Makefile FORCE
ifeq ($(SIMDOC_APP), R2DTool)
	pwd
	ls ../$(SIMDOC_APP)/../R2DExamples/
	$(PYTHON) scripts/index_examples.py $(SIMDOC_APP) \
    | aurore -D- -B ../$(SIMDOC_APP)/../R2DExamples/ -C scripts/config.yml get \
    > $(call BUILDDIR,$(SIMDOC_APP))_Examples.json
else
	$(PYTHON) scripts/index_examples.py $(SIMDOC_APP) \
    | aurore -D- -B ../$(SIMDOC_APP)/Examples/ -C scripts/config.yml get \
    > $(call BUILDDIR,$(SIMDOC_APP))_Examples.json
endif

$(CSVDIR)/%.csv: $(JSONDIR)/%.json ./scripts/json2csv.py
	python3 ./scripts/json2csv.py \
		-Eqfem $(SIMCENTER_DEV)/quoFEM/Examples/qfem*/src/input.json \
		-Eeeuq $(SIMCENTER_DEV)/EE-UQ/Examples/eeuq-*/src/input.json \
		-Eweuq -  \
		-Epbdl $(SIMCENTER_DEV)/PBE/Examples/pbdl-*/src/input.json \
		-Er2dt $(SIMCENTER_DEV)/R2DExamples/E*/input.json \
		-Ehdro $(SIMCENTER_DEV)/HydroUQ/Examples/hdro-*/src/input.json  \
		< '$<' > '$@'

csv-debug: FORCE
	for i in $(JSONDIR)/*.json; do \
	    json_file="$${i##*/}"; \
        echo $$json_file; \
        python3 ./scripts/json2csv.py -v \
            -Eqfem $(SIMCENTER_DEV)/quoFEM/Examples/qfem*/src/input.json \
            -Eeeuq $(SIMCENTER_DEV)/EE-UQ/Examples/eeuq-*/src/input.json \
            -Eweuq -  \
            -Epbdl $(SIMCENTER_DEV)/PBE/Examples/pbdl-*/src/input.json \
            -Er2dt $(SIMCENTER_DEV)/R2DExamples/E*/input.json \
            -Ehdro $(SIMCENTER_DEV)/HydroUQ/Examples/hdro-*/src/input.json \
            < "$(JSONDIR)/$$json_file"; \
	done

FORCE:
.PHONY: csv-debug

user_inputs:
	@echo "\nRunning the following command to generate user input documentation pages:\n"
	$(PYTHON) \
	$(USER_INPUT_DOC_DIR)/widget_documentation_utilities.py \
	$(USER_INPUT_DOC_DIR)/User_Inputs_Documentation_CSV_Files \
	-r $(USER_INPUT_DOC_DIR)/User_Inputs_Documentation_RST_Files \
	-t $(USER_INPUT_DOC_DIR)/User_Input_Documentation_Tables.rst
	@echo "\n'make user_inputs' complete.\n"

starter_files:
	@echo "\nRunning the following command to create starter csv files for user input documentation:\n"
	$(PYTHON) \
	$(USER_INPUT_DOC_DIR)/widget_documentation_starter_file_creation_utilities.py \
	$(USER_INPUT_DOC_DIR)/widget_header_files_list.txt \
	-c $(USER_INPUT_DOC_DIR)/User_Inputs_Documentation_CSV_Files
	@echo "\n'make starter_files' complete.\n"
