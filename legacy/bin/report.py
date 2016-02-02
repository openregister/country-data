#!/usr/bin/env python3

from pyuca import Collator
c = Collator("bin/allkeys.txt")

names = {
    'country-names': {
        'title': 'Country names',
        'url': 'https://www.gov.uk/government/publications/country-names/country-names-the-permanent-committee-on-geographical-names-for-british-official-use',
        'publisher': 'FCO',
        'format': 'HTML',
        'fields': ["name", "slug"]
    },
    'foreign-travel-advice': {
        'title': 'Foreign travel advice',
        'url': 'https://www.gov.uk/foreign-travel-advice',
        'publisher': 'FCO',
        'format': 'HTML',
        'fields': ["name", "slug", "filter-terms"]
    },
    'geographical-names-and-information': {
        'title': 'Geographical names and information',
        'url': '',
        'format': 'CSV'
    },
    'gpc': {
        'title': 'Government procurement card codes',
        'url': 'https://www.gov.uk/government/publications/government-procurement-card-data-country-codes',
        'format': 'CSV'
    },
    'hmrc': {
        'title': 'ISO Country Codes',
        'url': 'https://www.gov.uk/government/publications/iso-country-codes',
        'format': 'PDF'
    },
    'marriage-abroad': {
        'title': 'Marriage abroad',
        'url': '',
        'format': 'HTML'
    },
    'OLC-country-of-birth': {
        'title': 'Passports country of birth',
        'url': '',
        'format': 'HTML'
    },
    'OLC-current-location': {
        'title': 'Passports current location',
        'url': '',
        'format': 'HTML'
    },
    'passports-beta': {
        'title': 'Passports beta',
        'url': '',
        'format': 'HTML'
    },
    'visa-fees': {
        'title': 'Visa fees',
        'url': '',
        'format': 'HTML'
    },
    'world': {
        'title': 'World locations',
        'url': '',
        'format': 'HTML'
    },
    'devtracker': {
        'title': 'Development tracker',
        'url': 'https://devtracker.dfid.gov.uk/location/country',
        'format': 'HTML'
    },
    'registered-traveller': {
        'title': 'Registered traveller',
        'url': 'https://www.faster-uk-entry.service.gov.uk/initialapplication/details',
        'format': 'HTML',
        'publisher': 'Home Office'
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


def name_link(name):
    return "<a href='#%s'>%s</a>" % (name, name)

print("""
<!doctype html>
<html>
<head>
<meta charset='utf-8'>
<style>
body {
    font-family: "Helvetica Neue";
}
.name {
    border-top: 1px solid grey;
}
h1 {
    font-size: 2em;
}
th {
    text-align: left;
}
</style>
</head>
<body>
<div class="wrapper">
""")

for name in sorted(names):
    print("""
        <div class="name" id='%s'>
        <h1> %s %s (%s)</h1>
        <p><a href="%s">%s</a></p>
        </div>
    """ %(
        name,
        names[name]['count'], names[name]['title'], names[name]['format'],
        names[name]['url'], names[name]['url']

))

print("""
<table>
<thead>
    <tr><th>Country</th><th>Count</td><th>Lists</th></tr>
</thead>
<tbody>
""")

for country in sorted(by_country, key=c.sort_key):
    names_list = ", ".join([name_link(name) for name in by_country[country]['names']])
    print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (country, by_country[country]['count'], names_list))

print("""
</tbody>
</table>
</div>
</body>
<script type="text/javascript" src="bower_components/jquery/dist/jquery.js"></script>
<script type="text/javascript" src="bower_components/tablesorter/dist/js/jquery.tablesorter.combined.js"></script>
<script>
$(function() {
    $("table").tablesorter();
});
</script>
</html>
""")
