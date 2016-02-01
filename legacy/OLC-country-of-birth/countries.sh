#!/bin/sh

export LC_ALL=C

  sed -e 's/^.*"> *//' -e 's/ *<.*$//' |
  sort
