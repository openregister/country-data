# see: https://www.gov.uk/government/publications/iso-country-codes
URL=https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/389369/appendix5.pdf

countries.csv:	countries.pdf
	pdftotext countries.pdf > $@

# download from GOV.UK
countries.pdf:
	curl -s $(URL) > $@

init:
	brew install poppler
