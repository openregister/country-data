#!/usr/bin/env python3

from pyuca import Collator
c = Collator("bin/allkeys.txt")

names = {
    'country-names': {
        'title': 'Country names',
        'url': 'https://www.gov.uk/government/publications/country-names/country-names-the-permanent-committee-on-geographical-names-for-british-official-use',
        'publisher': 'foreign-commonwealth-office',
        'format': 'HTML',
        'fields': ["name", "slug"]
    },
    'foreign-travel-advice': {
        'title': 'Foreign travel advice',
        'url': 'https://www.gov.uk/foreign-travel-advice',
        'publisher': 'foreign-commonwealth-office',
        'format': 'HTML',
        'fields': ["name", "slug", "filter-terms"]
    },
    'geographical-names': {
        'title': 'Geographical names and information',
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
    }
}

by_country = {}

for name in names:
    count = 0
    path = name + '/countries.txt'
    for line in open(path):
        count = count + 1
        country = line.strip()
        if not country in by_country:
            by_country[country] = {}
            by_country[country]['count'] = 0
            by_country[country]['names'] = []

        by_country[country]['count'] = by_country[country]['count'] + 1
        by_country[country]['names'].append(name)

    names[name]['count'] = count
    if not 'data' in names[name]:
        names[name]['data'] = names[name]['url']


def name_link(name):
    return "<a href='#%s'>%s</a>" % (name, name)

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
</style>
</head>
<body>
<div class="wrapper">

<h2>Lists of countries</h2>

<table id="lists" class="tablesorter">
<thead>
    <tr>
      <th class='name'>List</th>
      <th>Title</th>
      <th>Publisher</th>
      <th>Data</th>
      <th class='count'>Count</th>
    </tr>
</thead>
<tbody>
""")

for name in sorted(names):
    txt = "%s/countries.txt" % (name)
    print("<tr id='%s'>" % (name))
    print("<td>%s</td>" % (name))
    print("<td><a href='%s'>%s</a></td>" % (names[name]['url'], names[name]['title']))
    print("<td>%s</td>" % (names[name]['publisher']))
    print("<td><a href='%s'>%s</a></td>" % (names[name]['data'], names[name]['format']))
    print("<td class='count'><a href='%s'>%s</a></td>" % (txt, names[name]['count']))
    print("</tr>")

print("""
</tbody>
</table>

<h2>Countries</h2>
<table id="countries" class="tablesorter">
<thead>
    <tr>
        <th class='country'>Country</th>
        <th>Lists</th>
        <th class='count'>Count</th>
    </tr>
</thead>
<tbody>
""")

for country in sorted(by_country, key=c.sort_key):
    names_list = ", ".join([name_link(name) for name in by_country[country]['names']])
    print("<tr>")
    print("<td>%s</td>" % (country))
    print("<td>%s</td>" % (names_list))
    print("<td class='count'>%s</td>" % (by_country[country]['count']))
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
    $("#countries").tablesorter({theme : 'blue'});
});
</script>
</html>
""")
