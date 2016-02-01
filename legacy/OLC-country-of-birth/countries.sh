#!/bin/sh

export LC_ALL=C

  sed -e 's/^.*"> *//' \
      -e 's/ *<.*$//' \
      -e 's/&amp;/\&/g' |
  sort
