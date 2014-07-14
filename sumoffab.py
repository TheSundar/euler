sum=0
a=1
b=1
counter=2
while True:
    c=a+b
    a=b
    b=c
    counter+=1
    print len(str(b))
    if len(str(b))<=100:
        print b,counter
    if len(str(b))>=1000:
        print counter
        break





