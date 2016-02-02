NAME=$(shell basename ${PWD})
URL='https://devtracker.dfid.gov.uk/location/country'
FILE=$(NAME).html
INDEX=countries.txt

countries.txt:	$(FILE) countries.sh
	countries.sh < $(FILE) > $@

$(FILE):
	curl -s $(URL) > $@

clean:
	rm -f $(FILE) $(INDEX)
