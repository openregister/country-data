#!/bin/sh

export LC_ALL=C
  grep '<option value="' |
  sed -e 's/" *>/">/' -e 's/^.*">//' -e 's/<.*$//' -e 's/^ *//' -e 's/ *$//'|
  grep -v 'Select…' |
  sort
