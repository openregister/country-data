#!/bin/sh

export LC_ALL=C

  awk -F'	' '{ print $1 }' |
  sed -e 's/&amp;/\&/g' |
  sort
