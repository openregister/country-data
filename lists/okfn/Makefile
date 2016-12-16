URL='http://data.okfn.org/data/core/country-codes/r/country-codes.csv'
FILE=cache/country-codes.csv
MAPS=alpha3.csv

all:	$(MAPS)

alpha3.csv:	$(FILE) bin/alpha3.py
	bin/alpha3.py < $(FILE) > $@

$(FILE):
	mkdir -p cache
	curl -qs $(URL) > $@

clean:
	rm -rf $(FILE) cache

init:

install:
	cp $(MAPS) ../../maps
