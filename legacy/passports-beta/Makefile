NAME=$(shell basename ${PWD})
FILE=$(NAME).tsv
INDEX=countries.txt

countries.txt:	$(FILE) countries.sh
	countries.sh < $(FILE) > $@

clean:
	rm -f $(FILE) $(INDEX)
