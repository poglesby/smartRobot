#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time, sys, random

argfile = str(sys.argv[1])

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

# for line in f:
#     print line[:135] + "#elit"
text = ''.join(f)
string = text.split(".")
for l in string:
    print l[:134] + " #elit"
    time.sleep(random.randrange(20))
