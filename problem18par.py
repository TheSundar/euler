import itertools
lis=[2,3,5,7,11,13,17]
sum1=0
for i in itertools.permutations('0123456789',10):
    i=''.join(i)
    if all([int(i[j[0]:j[0]+3])%j[1]==0 for j in zip(range(1,8),lis)]):

        sum1+=int(i)
print sum1



