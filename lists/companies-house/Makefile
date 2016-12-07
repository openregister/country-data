#
#  find countries in Companies House open data
#
#  Companies House "free" data, see:
#  http://download.companieshouse.gov.uk/en_output.html
#
DATE=2015-10-01
URL_PREFIX=http://download.companieshouse.gov.uk/BasicCompanyData-$(DATE)-part
URL_SUFFIX=_5.zip

PARTS=\
	cache/part1.zip\
	cache/part2.zip\
	cache/part3.zip\
	cache/part4.zip\
	cache/part5.zip

.PHONY: all flake8 prune out

all:	company-countries.tsv

company-countries.tsv:	$(PARTS) company-countries.sh company-countries.py
	cat-companies.sh $(PARTS) | company-countries.sh > $@


#
#  download data
#
cache/part1.zip:;	mkdir -p cache && curl -s "$(URL_PREFIX)1$(URL_SUFFIX)" > $@
cache/part2.zip:;	mkdir -p cache && curl -s "$(URL_PREFIX)2$(URL_SUFFIX)" > $@
cache/part3.zip:;	mkdir -p cache && curl -s "$(URL_PREFIX)3$(URL_SUFFIX)" > $@
cache/part4.zip:;	mkdir -p cache && curl -s "$(URL_PREFIX)4$(URL_SUFFIX)" > $@
cache/part5.zip:;	mkdir -p cache && curl -s "$(URL_PREFIX)5$(URL_SUFFIX)" > $@

#
#  clean
#
prune::
	rm -rf cache data

clean::
	rm -rf $(REGISTERS) $(COUNTRIES) data

#
#  python
#
flake8::
	flake8 .

