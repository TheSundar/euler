import tempfile
from itertools import groupby, count
import os

temp_dir = tempfile.mkdtemp()

import time

start = time.time()
print "hello"

from os import listdir
from os.path import isfile, join
path='C:/Users/Sundar/Desktop/backup helios/test'
files = [ path+'/'+ f for f in listdir(path) if isfile(join(path,f)) ]



def tempfile_split(filename, temp_dir, chunk=1500):
    with open(filename, 'r') as datafile:
        groups = groupby(datafile, key=lambda k, line=count(): next(line) // chunk)
        for k, group in groups:
            output_name = os.path.normpath(os.path.join(temp_dir + os.sep, "tempfile_%s.tmp" % k))
            with open(output_name, 'a') as outfile:
                outfile.write(''.join(group))

for file in files:
    tempfile_split(file,'d:/',1500)

end = time.time()
print end - start