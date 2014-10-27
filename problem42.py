def value(i):
    sum=0
    for l in i:
        sum+=ord(l)-64
    return sum
def sumofnat():
    for i in xrange(1,100):
        yield (i*(i+1))/2
with open('words.txt','r') as file:
    a=file.readlines()[0].replace('"','').split(',')
    print a
    print len([i for i in map(value,a)if i in sumofnat() ])
