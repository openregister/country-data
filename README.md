# Country register data

Data for the [country register](http://country.openregister.org), taken from the
[list of geographical names](https://www.gov.uk/government/publications/geographical-names-and-information)
maintained by the [Foreign & Commonwealth Office](https://www.gov.uk/government/organisations/foreign-commonwealth-office).
The register primary key is the [ISO_3166-1](http://en.wikipedia.org/wiki/ISO_3166-1) alpha-2 code for a country.

# Building

Use make to build register shaped data
— we recommend using a [Python virtual environment](http://virtualenvwrapper.readthedocs.org/en/latest/):

    $ mkvirtualenv -p python3 country-data
    $ workon country-data
    $ make init

    $ make

# Licence

The software in this project is covered by LICENSE file.

The data is [© Crown copyright](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/crown-copyright/)
and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.
