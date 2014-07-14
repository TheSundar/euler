import timeit
print timeit.timeit('sum([i for i in xrange(2,999999) if i == (sum([int(j)**5 for j in str(i) ]))])',number=10)
print timeit.timeit('sum( (y for y in range(2,999999) if y == sum(map(lambda x: pow(x,5), map(int,str(y)))) ) )',number=10)