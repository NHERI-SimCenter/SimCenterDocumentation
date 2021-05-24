all:
	for i in *.json; do echo $$i; make out/$${i/json/csv}; done

out/%.csv: %.json
	../json2csv.py \
		-Eqfem ~/simc/quoFEM/Examples/qfem*/src/input.json \
		-Eeeuq ~/simc/EE-UQ/Examples/eeuq*/src/input.json \
		-Epbdl ~/simc/PBE/Examples/pbdl*/src/input.json \
		< $< > $@ 
