#!/usr/bin/env python3

import csv

from pyuca import Collator
c = Collator("bin/allkeys.txt")

codes = {}

lists = {
    'country': {
        'title': 'Country register',
        'url': 'http://country.openregister.org',
        'publisher': 'foreign-commonwealth-office',
        'format': 'register',
        'path': '../data/country/countries.tsv'
    },
    'territory': {
        'title': 'Territory register',
        'url': 'http://territory.openregister.org',
        'publisher': 'foreign-commonwealth-office',
        'format': 'register',
        'path': '../data/territory/territories.tsv'
    },
    'uk': {
        'title': 'UK register',
        'url': 'http://uk.openregister.org',
        'publisher': 'cabinet-office',
        'format': 'register',
        'path': '../data/uk/uk.tsv'
    },
    'country-names': {
        'title': 'Country names',
        'url': 'https://www.gov.uk/government/publications/country-names/country-names-the-permanent-committee-on-geographical-names-for-british-official-use',
        'publisher': 'foreign-commonwealth-office',
        'format': 'HTML'
    },
    'country-names-mod': {
        'title': 'Country names',
        'url': 'https://www.gov.uk/government/publications/country-names',
        'publisher': 'ministry-of-defence',
        'format': 'XLSX'
    },
    'foreign-travel-advice': {
        'title': 'Foreign travel advice',
        'url': 'https://www.gov.uk/foreign-travel-advice',
        'publisher': 'foreign-commonwealth-office',
        'format': 'HTML'
    },
    'geographical-names': {
        'title': 'Geographical names and information',
        'url': 'https://www.gov.uk/government/publications/geographical-names-and-information',
        'publisher': 'foreign-commonwealth-office',
        'format': 'CSV'
    },
    'overseas-territories': {
        'title': 'Overseas territories geographical names and information',
        'url': 'https://www.gov.uk/government/publications/geographical-names-and-information',
        'publisher': 'foreign-commonwealth-office',
        'format': 'CSV'
    },
    'gpc': {
        'title': 'Government procurement card codes',
        'url': 'https://www.gov.uk/government/publications/government-procurement-card-data-country-codes',
        'publisher': 'foreign-commonwealth-office',
        'format': 'CSV'
    },
    'hmrc': {
        'title': 'ISO Country Codes',
        'url': 'https://www.gov.uk/government/publications/iso-country-codes',
        'publisher': 'hm-revenue-customs',
        'format': 'PDF'
    },
    'marriage-abroad': {
        'title': 'Marriage abroad',
        'url': 'https://www.gov.uk/marriage-abroad/y',
        'publisher': 'foreign-commonwealth-office',
        'format': 'HTML'
    },
    'country-of-birth': {
        'title': 'Passports country of birth',
        'url': '',
        'publisher': 'hm-passport-office',
        'format': 'HTML'
    },
    'current-location': {
        'title': 'Passports current location',
        'url': '',
        'publisher': 'hm-passport-office',
        'format': 'HTML'
    },
    'passports-beta': {
        'title': 'Passports beta',
        'url': 'https://github.com/openregister/country-data/blob/master/legacy/passports-beta/passports-beta.tsv',
        'publisher': 'hm-passport-office',
        'format': 'HTML'
    },
    'visa-fees': {
        'title': 'Visa fees',
        'url': 'https://visa-fees.homeoffice.gov.uk/y',
        'format': 'HTML',
        'publisher': 'uk-visas-and-immigration'
    },
    'world': {
        'title': 'World locations',
        'url': 'https://www.gov.uk/government/world',
        'data': 'https://www.gov.uk/api/world-locations',
        'format': 'JSON',
        'publisher': 'foreign-commonwealth-office'
    },
    'devtracker': {
        'title': 'Development tracker',
        'url': 'https://devtracker.dfid.gov.uk/location/country',
        'format': 'HTML',
        'publisher': 'department-for-international-development'
    },
    'registered-traveller': {
        'title': 'Registered traveller',
        'url': 'https://www.faster-uk-entry.service.gov.uk/initialapplication/details',
        'format': 'HTML',
        'publisher': 'home-office'
    },
    'trade-tariff': {
        'title': 'Trade Tariff',
        'url': 'https://www.gov.uk/government/publications/uk-trade-tariff-country-and-currency-codes',
        'format': 'HTML',
        'publisher': 'hm-revenue-customs'
    }
}

issues = {
    'AX': {
        'countries': [
            "Åland Islands",
            "Aland Islands",
            "Finland (including Aland Islands)"
        ]
    },
    'HM': {
        'countries': [
            "Heard and McDonald Islands",
            "Heard and McDonald lslands",
            "Heard Island and McDonald Islands"
        ]
    },
    'HK': {
        'countries': [
            "Hong Kong",
            "Hong Kong Special Administrative"
        ]
    },
    'CI': {
        'countries': [
            "Ivory Coast",
            "Ivory Coast (Cote D'Ivoire)",
            "Ivory Coast (Cote d’Ivoire)",
            "Cote d'Ivoire",
            "Côte d'Ivoire",
            "Cote d’Ivoire",
            "Cote d’lvoire"
        ]
    },
    'KP': {
        'countries': [
            "Korea (North)",
            "Korea, Democratic People's Republic of",
            "Korea, North",
            "Korea, Republic of",
            "Korea, South",
            "DPR Korea",
            "North Korea",
        ]
    },
    'KR': { 
        'countries': [
            "Korea (South)",
            "Korea, Republic of",
            "Korea, South",
            "South Korea"
        ]
    },
    'MM': {
        'countries': [
            "Burma",
            "Myanmar",
            "Myanmar (Burma)"
        ]
    },
    'PL': {
        'countries': [
            "Occ. Palestinian Territories",
            "Occupied Palestinian Territories (OPT)",
            "Occupied Palestinian Territory (West Bank (including East Jerusalem) and Gaza Strip)",
            "Palestinian Occupied Territories",
            "Palestinian Territory, Occupied",
            "The Occupied Palestinian Territories"
        ]
    },
    'RE': {
        'countries': [
            "Reunion",
            "Réunion",
            "Reunion"
        ]
    },
    'PM': {
        'countries': [
            "St Pierre & Miquelon",
            "St Pierre and Miquelon"
        ]
    },
    'TZ': {
        'countries': [
            "Tanzania",
            "Tanzania (Tanganyika, Zanzibar, Pemba)",
            "Tanzania, United Rep. of",
            "Tanzania, United Republic of"
        ]
    },
    'VA': {
        'countries': [
            "Vatican City",
            "Vatican City State",
            "Holy See",
            "Holy See (Vatican City State)"
        ]
    },
    'VG': {
        'countries': [
            "British Virgin Islands",
            "Virgin Islands (British)",
            "Virgin Islands, British",
        ]
    },
    'VI': {
        'countries': [
            "Virgin Islands (USA)",
            "Virgin Islands of USA",
            "Virgin Islands, U.S."
        ]
    },
    'YU': { 'countries': [
        "Yugoslavia"
    ]}
}

by_country = {}

def country_names(name, lines):
    count = 0

    for line in lines:
        count = count + 1
        country = line.strip()
        if not country in by_country:
            by_country[country] = {}
            by_country[country]['count'] = 0
            by_country[country]['names'] = []

        by_country[country]['count'] = by_country[country]['count'] + 1
        by_country[country]['names'].append(name)

    return count


for name in lists:
    list = lists[name]
    if not 'data' in list:
        list['data'] = list['url']

    if not 'path' in list:
        list['path'] = name + '/countries.txt'

    if (list['format'] != 'register'):
        list['count'] = country_names(name, open(list['path']))
    else:
        names = []
        official_names = []
        for row in csv.DictReader(open(list['path']), delimiter='	'):
            codes[row[name]] = row
            names.append(row['name'])
            official_names.append(row['official-name'])

        list['count'] = country_names(name, names)
        country_names(name + "-official", official_names)

    lists[name] = list

for code in codes:
    by_country[codes[code]['name']]['code'] = code
    by_country[codes[code]['official-name']]['code'] = code

def name_link(name):
    return "<a href='#%s' class='_%s'>%s</a>" % (name, name, name)

print("""
<!doctype html>
<html>
<head>
<meta charset='utf-8'>
<link rel="stylesheet" href="bower_components/tablesorter/dist/css/theme.blue.min.css" type="text/css">
<style>
body {
    font-family: "Helvetica Neue";
}
h1 {
    font-size: 2em;
}
table {
    width: 100%;
}
th, td {
    text-align: left;
}
.count {
    text-align: right;
}
td {
    vertical-align: top;
}
.name, .country {
    width: 20%;
}

#issues .countries span {
    background-color: #f5f0d6;
    margin-right: 1.2em;
}

tr.country,
tr.country-official,
tr.territory,
tr.territory-official,
tr.uk,
tr.uk-official {
    background-color: #e2e2e2;
}

</style>
</head>
<body>
<div class="wrapper">

<h2>Lists of countries</h2>

<table id="lists" class="tablesorter">
<thead>
    <tr>
      <th></th>
      <th class='name'>List</th>
      <th>Title</th>
      <th>Publisher</th>
      <th>Data</th>
      <th class='count'>Count</th>
    </tr>
</thead>
<tbody>
""")

for name in sorted(lists):
    list = lists[name]
    print("<tr id='%s'>" % (name))
    print("<td><input type='checkbox' name='%s' checked></td>" % (name))
    print("<td class='name'>%s</td>" % (name))
    print("<td><a href='%s'>%s</a></td>" % (list['url'], list['title']))
    print("<td>%s</td>" % (list['publisher']))
    print("<td><a href='%s'>%s</a></td>" % (list['data'], list['format']))
    print("<td class='count'><a href='%s'>%s</a></td>" % (list['path'], list['count']))
    print("</tr>")

print("""
</tbody>
</table>

<h2>Names</h2>
<table id="names" class="tablesorter">
<thead>
    <tr>
        <th class='country'>Country</th>
        <th class='name'>Name</th>
        <th>Lists</th>
        <th class='count'>Count</th>
    </tr>
</thead>
<tbody>
""")

for country in sorted(by_country, key=c.sort_key):
    classes = " ".join([name for name in by_country[country]['names']])
    names_list = " ".join([name_link(name) for name in by_country[country]['names']])

    if not 'code' in by_country[country]:
        by_country[country]['code'] = ''

    print("<tr class='%s'>" % (classes))
    print("<td class='country'>%s</td>" % (by_country[country]['code']))
    print("<td class='name'>%s</td>" % (country))
    print("<td class='names'>%s</td>" % (names_list))
    print("<td class='count'>%s</td>" % (by_country[country]['count']))
    print("</tr>")

print("""
</tbody>
</table>

<h2>Issues</h2>
<table id="issues" class="tablesorter">
<thead>
    <tr>
        <th class='issue'>Issue</th>
        <th class='countries'>Countries</th>
    </tr>
</thead>
<tbody>
""")

n = 0
for code in sorted(issues):
    countries_list = "</span> <span>".join([country for country in issues[code]['countries']])
    print("<tr id='issue_%s'>" % (code))
    print("<td class='issue'>%s</td>" % (code))
    print("<td class='countries'><span>%s</span></td>" % (countries_list))
    print("</tr>")


print("""
</tbody>
</table>

</div>
</body>
<script type="text/javascript" src="https://code.jquery.com/jquery-2.2.0.min.js"></script>
<script type="text/javascript" src="https://cdn.jsdelivr.net/tablesorter/2.17.4/js/jquery.tablesorter.min.js"></script>
<script>
$(function() {
    $("#lists").tablesorter({theme : 'blue'});
    $("#names").tablesorter({theme : 'blue'});
    $("#issues").tablesorter({theme : 'blue'});
    $('input').each(function(){
        $(this).click(function () {
            $("._" + this.name).toggle();
            $('#names td.names').each(function () {
                $(this).parent().show();
                var count = $(this).children(':visible').length;
                if (count == 0) {
                    $(this).parent().hide();
                }
                $(this).next('td').text(count);
            });
        });
    });
});
</script>
</html>
""")
