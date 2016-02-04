#!/bin/sh

export LC_ALL=C

  countries.py |
  sed -e 's/  */ /g' \
      -e 's/[0-9]*$//' |
  sort -u
