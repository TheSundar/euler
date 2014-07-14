print len(set([i**j for i in range(2,101) for j in range(2,101)]))

string=''

for i in xrange(1,1000000):
    string+=str(i)
product=1


for i in range(0,7):
     product*=int(string[(10**i)-1])
print product