COUNTRIES=\
	country-names/countries.txt \
	country-of-birth/countries.txt \
	current-location/countries.txt \
	devtracker/countries.txt \
	foreign-travel-advice/countries.txt \
	geographical-names/countries.txt \
	gpc/countries.txt \
	hmrc/countries.txt \
	marriage-abroad/countries.txt \
	passports-beta/countries.txt \
	registered-traveller/countries.txt \
	trade-tariff/countries.txt \
	visa-fees/countries.txt \
	world/countries.txt

report.html:	bin/allkeys.txt bin/report.py $(COUNTRIES)
	bin/report.py > $@

bin/allkeys.txt:
	curl http://www.unicode.org/Public/UCA/latest/allkeys.txt > bin/allkeys.txt

init:
	pip install --upgrade -r requirements.txt
	bower install jquery jquery.tablesorter
