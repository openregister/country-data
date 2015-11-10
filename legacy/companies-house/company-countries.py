#!/usr/bin/env python3

import sys
from datetime import datetime
import csv

reader = csv.DictReader(sys.stdin)
reader.fieldnames = [field.strip() for field in reader.fieldnames]

for row in reader:
    print(row['RegAddress.Country'])
    print(row['CountryOfOrigin'])
