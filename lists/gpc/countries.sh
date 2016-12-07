#!/bin/sh

export LC_ALL=C

iconv -f ISO8859-1 -t UTF-8 |
  sed \
    -e 's/Aland Islands !ÿland Islands/Åland Islands/' \
    -e 's/Curaao/Curaçao/' \
    -e 's/Saint Barthlemy/Saint Barthélemy/' \
    -e 's/Reunion !ÿRunion/Réunion/' \
    -e "s/Cote d'Ivoire !ÿCte d'Ivoire/Côte d'Ivoire/" |
  tail -n+2 |
  sed -e '/^,, *$/d' -e '/row(s) affected/d' |
  csvtool cols 1 - |
  sed -e 's/"//g' -e '/^[ \t]*$/d' |
  sort
