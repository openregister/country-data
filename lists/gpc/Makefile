NAME=$(shell basename ${PWD})
URL='https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/340933/Country_codes_CSV.csv'
FILE=$(NAME).csv
INDEX=countries.txt

countries.txt:	$(FILE) countries.sh
	countries.sh < $(FILE) > $@

$(FILE):
	curl -s $(URL) > $@

clean:
	rm -f $(FILE) $(INDEX)
