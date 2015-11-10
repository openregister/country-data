#!/bin/sh

    python company-countries.py |
    sort |
    uniq -c |
    sort -rn |
    sed -e 's/^ *//' \
        -e 's/  */	/' \
        -e 's/ *$//'  
}
