#!/bin/sh

export LC_ALL=C
  ./countries.py "$1" |
  sort
