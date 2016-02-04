NAME=$(shell basename ${PWD})
URL='https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/497622/Country_names.xlsx'
FILE=$(NAME).xlsx
INDEX=countries.txt

countries.txt:	$(FILE) countries.sh countries.py
	countries.sh "$(FILE)" < $(FILE) > $@

$(FILE):
	curl -s $(URL) > $@

clean:
	rm -f $(FILE) $(INDEX)
