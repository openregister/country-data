#!/bin/sh

export LC_ALL=C

tail -n+2 |
  csvtool cols 1 - |
  sed 's/"//g' |
  sort
