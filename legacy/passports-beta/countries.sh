#!/bin/sh

export LC_ALL=C

  awk -F'	' '{ print $1 }' |
  sort
