NAME=$(shell basename ${PWD})
URL='https://www.gov.uk/api/world-locations'
FILE=$(NAME).tsv
INDEX=countries.txt

countries.txt:	$(FILE) Makefile
	awk -F'	' '$$1 != "None" {print $$3}' $(FILE) > $@

$(FILE):	bin/world.py
	bin/world.py > $@

clean:
	rm -f $(FILE) $(INDEX)

init:
	pip install -r requirements.txt
