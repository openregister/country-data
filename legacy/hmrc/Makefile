NAME=$(shell basename ${PWD})
# see: https://www.gov.uk/government/publications/iso-country-codes
URL=https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/389369/appendix5.pdf
FILE=$(NAME).pdf
TXT=$(NAME).txt
INDEX=countries.txt

countries.txt:	$(TXT) countries.sh
	countries.sh < $(TXT) > $@

$(TXT):	$(FILE) Makefile
	pdftotext $(FILE) $(TXT)

$(FILE):
	curl -s $(URL) > $@

clean:
	rm -f $(FILE) $(TXT) $(INDEX)

init:
	brew install poppler
