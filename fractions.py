from decimal import *
getcontext().prec = 1000
import re
for i in range(2,1000):
    x=str(Decimal(1) / Decimal(i))[2:]
    print re.findall(r'^(.+?)((.+)\3+)$', x )