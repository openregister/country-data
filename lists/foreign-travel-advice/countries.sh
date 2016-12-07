#!/bin/sh

export LC_ALL=C
  grep '<li data-synonyms=' |
  sed -e 's/^.*">//' \
      -e 's/<.*$//' \
      -e 's/&amp;/\&/g' |
  sort
