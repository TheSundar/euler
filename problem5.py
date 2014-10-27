
# Simple solution

# prod = 1
# for i in range(1, 21):
#
#     if prod % i > 0:
#         print i
#         for j in range(1, 21):
#             print '-----',(prod*j) % i
#             if (prod*j) % i == 0:
#                 prod *= j
#                 break
# print prod


### Brute Force
x=2520
while True:
    print x
    if all([x%i==0 for i in range(1,21)]):
        print x
        break
    x+=1
