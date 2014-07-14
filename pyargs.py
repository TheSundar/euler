import fileinput
import sys

for line in fileinput.input(["a.txt"], inplace=True, backup='.bak'):
    if line !='/n':
        pre,post=line.split()
        sys.stdout.write(pre+' '+str(float(post)*100)+' %\n')
    else:
        sys.stdout.write(line)