NAME=$(shell basename ${PWD})
URL='https://www.gov.uk/marriage-abroad/y'
FILE=$(NAME).html
INDEX=countries.txt

countries.txt:	$(FILE) countries.sh
	countries.sh < $(FILE) > $@

$(FILE):
	curl -s $(URL) > $@

clean:
	rm -f $(FILE) $(INDEX)
