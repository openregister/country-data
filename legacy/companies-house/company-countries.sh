#!/bin/sh

    python company-countries.py |
    sed -e 's/^ *//' -e 's/  */ /g' -e 's/ *$//' |
    sort |
    uniq -c |
    sort -rn |
    sed -e 's/^ *//' \
        -e 's/  */	/' \
        -e 's/ *$//'   |
    awk -F'	' 'BEGIN { print "country-name	count" }
      { print $2 "	" $1 }'
