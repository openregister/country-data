#!/bin/sh

export LC_ALL=C

  sed -e '/^[a-z]/d' \
      -e 's/[ \t\r]*$//' \
      -e '/^$/d' \
      -e '/[Aa]ppendix/d' |
      sort
