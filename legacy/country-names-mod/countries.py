#!/usr/bin/env python3

import sys
import openpyxl

wb = openpyxl.load_workbook(sys.argv[1])
sh = wb.get_active_sheet()
for r in sh.rows:
    print(r[0].value)
