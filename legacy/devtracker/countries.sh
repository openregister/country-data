#!/bin/sh

export LC_ALL=C
  grep '<a href="/countries/' |
  sed -e 's/^.*">//' \
      -e 's/<.*$//' \
      -e 's/&amp;/\&/g' |
  sort
