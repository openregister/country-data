#!/bin/sh

export LC_ALL=C
  awk -F'	' '$1 != "None" {print $3}' |
  sort
