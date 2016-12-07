#!/bin/sh

export LC_ALL=C
  grep '<li><a href="#' |
  sed -e 's/^.*">//' -e 's/<.*$//' |
  sort
