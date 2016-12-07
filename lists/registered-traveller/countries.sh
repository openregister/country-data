#!/bin/sh

export LC_ALL=C
  grep '<option }} value="' |
  sed -e 's/<\/option.*$//' \
      -e 's/^.*>//' \
      -e 's/&amp;/\&/g' |
  sort
