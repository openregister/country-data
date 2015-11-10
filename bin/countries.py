#!/usr/bin/env python3

"""Import iso country codes"""

import csv
import io
import sys


column_to_field = [['The two-letter ISO 3166-1 code', 'country'],
                   ['Country', 'name'],
                   ['Official Name', 'official-name'],
                   ['Name for Citizen', 'citizen-names'],
                   ['Notes', 'text']]

if __name__ == '__main__':
    # the countries csv seems to be in cp1252, not utf-8
    input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='cp1252')
    reader = csv.DictReader(input_stream)
    print (*[field for column, field in column_to_field], sep='\t')

    # GB isn't included in the csv for some reason
    print ('GB', 'United Kingdom', 'The United Kingdom of Great Britain and Northern Ireland', 'Briton, British citizen', 'GB is the United Kingdom\'s ISO 3166-1 alpha-2 code. The code UK is exceptionally reserved for the United Kingdom on the request of the country. Its main usage is the .uk internet ccTLD.', sep='\t')
    for num, row in enumerate(reader):
        print (*[row[column] for column, field in column_to_field], sep='\t')

