NAME=$(shell basename ${PWD})
FILE=$(NAME).html
INDEX=countries.txt

countries.txt:	$(FILE) countries.sh
	countries.sh < $(FILE) > $@

clean:
	rm -f $(FILE) $(INDEX)
