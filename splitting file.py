from itertools import izip_longest
import time

start = time.time()


from os import listdir
from os.path import isfile, join
path='C:/Users/Sundar/Desktop/backup helios/test'
files = [ path+'/'+ f for f in listdir(path) if isfile(join(path,f)) ]

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

n = 1500

for file in files:
    with open(file) as f:
        for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
            with open('small_file_{0}'.format(i * n), 'w') as fout:
                fout.writelines(g)


