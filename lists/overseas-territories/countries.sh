#!/bin/sh

export LC_ALL=C
  csvtool cols 1 - |
  sed 's/"//g' |
  sort
