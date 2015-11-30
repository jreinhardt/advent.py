#!/usr/bin/env python
"""
This script will check out todays lesson
"""

import datetime
import subprocess

date = datetime.date.today()

if date.month != 12:
    subprocess.call(['git','checkout','not_advent'])
elif date.day < 25:
    subprocess.call(['git','checkout','day_%s' % date.day])
else:
    subprocess.call(['git','checkout','merry_christmas'])

