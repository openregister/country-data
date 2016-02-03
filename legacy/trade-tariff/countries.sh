#!/bin/sh

export LC_ALL=C

  countries.py |
  sed -e 's/  */ /g' |
  sort
