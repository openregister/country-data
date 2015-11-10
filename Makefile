# FCO countries are published at https://www.gov.uk/government/publications/geographical-names-and-information
COUNTRY_CSV_URL=https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/375189/20141112-FCO_Country_Names_v1.csv

all:: data/Country/countries.tsv

data/Country/countries.tsv: bin/countries.py
	@mkdir -p data/Country
	curl $(COUNTRY_CSV_URL) | bin/countries.py > $@

