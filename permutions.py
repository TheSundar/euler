import itertools

p= list(itertools.permutations('0123456789', 10))[999999]
for i in p:
    print "".join(p)