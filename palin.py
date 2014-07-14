def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n >= 1:
       primfac.append(n)
    return primfac
import collections
c={}
for i in xrange(1,21):
    z= collections.Counter(primes(i))

    for x,y in z.items():
        if x in c.keys() and y > c[x]:
            c[x]=y
        elif x not in c.keys():
            c[x]=y

prod=1
for x,y in c.items():
    prod*=pow(x,y)
print prod



