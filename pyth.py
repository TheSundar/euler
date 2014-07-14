import math
for i in range(1,1000):
    for j in range(1,1000):
        if math.sqrt(i*i+j*j).is_integer():
            if i+j+math.sqrt(i*i+j*j)==1000:
                print int(i*j*(math.sqrt(i*i+j*j)))
                exit()


# for c in xrange(334,500):
#     for a in xrange(1, (1000-c)/2):
#         b = (1000 - c) - a
#         if a**2 + b**2 == c**2:
#             print "a,b,c =",a,b
# print sum([(x,y,1000-x-y) for x in range(1,1000) for y in range(1,x) if x**2+y**2==(1000-x-y)**2]