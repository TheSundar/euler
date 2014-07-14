import math

starting=14
counter=0

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def primegen():
    for i in range(2,10000):
        if is_prime(i):
            yield i

counter=0
temp=[]
while True:
    temp=starting
    while temp>1:
        for i in primegen():
            while temp%i==0:
                temp=temp/i
                print temp,i,'***'
                if temp==1:
                    break
            counter=counter+1
            if temp==1:
                break
        starting=starting+1
        if counter==3:
            break








