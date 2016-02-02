NAME=$(shell basename ${PWD})
URL='https://www.faster-uk-entry.service.gov.uk/initialapplication/details'
FILE=$(NAME).html
INDEX=countries.txt

countries.txt:	$(FILE) countries.sh
	countries.sh < $(FILE) > $@

$(FILE):
	curl -s $(URL) > $@

clean:
	rm -f $(FILE) $(INDEX)
