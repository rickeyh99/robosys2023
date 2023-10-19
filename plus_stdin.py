#!/usr/bin/python3
# SPDX-FileCopyrightText:2023 Riki Harada

import sys


def tonum(s):
    try:
        return int(s)
    except:
        return float(s)


ans = 0
for line in sys.stdin:
        ans += tonum(line)

print(ans)
