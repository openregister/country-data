report.html:	bin/allkeys.txt bin/report.py
	bin/report.py > $@

bin/allkeys.txt:
	curl http://www.unicode.org/Public/UCA/latest/allkeys.txt > bin/allkeys.txt

init:
	pip install --upgrade -r requirements.txt
	bower install jquery jquery.tablesorter
