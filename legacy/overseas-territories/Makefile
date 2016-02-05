NAME=$(shell basename ${PWD})
URL='https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/271613/20140113-FCO_GNI_UK_Overseas_Territory_Names_v1.csv'
FILE=$(NAME).csv
INDEX=countries.txt

countries.txt:	$(FILE) countries.sh
	countries.sh < $(FILE) > $@

$(FILE):
	curl -s $(URL) > $@

clean:
	rm -f $(FILE) $(INDEX)
