NAME=$(shell basename ${PWD})
URL='https://www.gov.uk/government/publications/country-names/country-names-the-permanent-committee-on-geographical-names-for-british-official-use'
FILE=$(NAME).html
INDEX=countries.txt

countries.txt:	$(FILE) countries.sh
	countries.sh < $(FILE) > $@

$(FILE):
	curl -s $(URL) > $@

clean:
	rm -f $(FILE) $(INDEX)
