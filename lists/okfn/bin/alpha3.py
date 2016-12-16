#!/usr/bin/env python3

import sys
import csv

# name,official_name_en,official_name_fr,ISO3166-1-Alpha-2,ISO3166-1-Alpha-3,ISO3166-1-numeric,ITU,MARC,WMO,DS,Dial,FIFA,FIPS,GAUL,IOC,ISO4217-currency_alphabetic_code,ISO4217-currency_country_name,ISO4217-currency_minor_unit,ISO4217-currency_name,ISO4217-currency_numeric_code,is_independent,Capital,Continent,TLD,Languages,geonameid,EDGAR

alpha2 = {}

for row in csv.DictReader(open('../../data/country/countries.tsv'), delimiter='\t'):
    alpha2[row['country']] = "country:" + row['country']

for row in csv.DictReader(open('../../data/territory/territories.tsv'), delimiter='\t'):
    alpha2[row['territory']] = "territory:" + row['territory']

fields = ['alpha3', 'world-location']

print("\t".join(fields))

for row in csv.DictReader(sys.stdin):

    row['alpha3'] = row['ISO3166-1-Alpha-3']

    if row['alpha3']:

        if row['ISO3166-1-Alpha-2'] in alpha2:
            row['world-location'] = alpha2[row['ISO3166-1-Alpha-2']]

        print("\t".join([row.get(field, '') for field in fields]))
