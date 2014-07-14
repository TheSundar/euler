# 90342 ;2 correct
# 07794 ;0 correct
# 39458 ;2 correct
# 34109 ;1 correct
# 51545 ;2 correct
# 12531 ;1 correct

import itertools
from collections import defaultdict
# def mrange(start, stop, step=1):
#     i = start
#     while i < stop:
#         yield i
#         i += step
#
# number= mrange(10**16,(10**17))
#
# newlist=[]
# a="90342"
#

#
# def combination(x,n):
#
#     if n==0:
#         temp=[]
#         for i in range(1,len(x)+1):
#
#             temp.extend(list(itertools.combinations(x,i)))
#
#
#         return temp
#
#
#
#     return list(itertools.combinations(x,n))
#
# def combineDictTuple(dt):
#
#     d = {}
#     print dt
#     for item in dt:
#         d.update(item)
#     return d
# def numgenerator(dt):
#
#     d = defaultdict(list,{})
#     for item in dt:
#         print item
#         for i,j in item.items():
#             d[j].append(i)
#
#     return d



def prob(a,n):
    temp=[]
    if n==0:
        temp=number

    modchar=[{i: c} for i, c in enumerate(a)]
    # combos = combination(modchar,n)
    # newCombos = [combineDictTuple(dt) for dt in combos]
    # newCombos = numgenerator(newCombos)
    print newCombos
    print n
    raw_input('press')
    # exit()
    #
    # for j in number:
    #     for i in newCombos:
    #         index=i.keys()
    #         val=i.values()
    #         # print index,val
    #         if n==0:
    #             if all(str(j)[index[l]]==val[l] for l in range(0,len(val))):
    #                 try:
    #                     if temp.index(j):
    #                         del temp[temp.index(j)]
    #                         break
    #                 except:
    #                     pass
    #
    #         else:
    #
    #             if all(str(j)[index[l]]==val[l] for l in range(0,len(val))):
    #                 temp.append(j)
    #                 break
    #
    #
    # return temp


val='''5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct'''

# 93996
val=val.replace('correct','').replace(';','').split('\n')
modchar=[]
for i in val:
    i=i.split()
    modchar.extend([{i: c} for i, c in enumerate(i[0])])

    # number=prob(i[0],int(i[1]))

print modchar




#
# number=prob(a,2)
# print len(number)
#
# number=prob('39458',2)
# print len(number)
# number=prob('51545',2)
# print len(number)



# for i in range(0,5):
#     for j in range(i+1,5):
#         for k in number:
#             if str(k)[i]==a[i] and str(k)[j]==a[j]:
#                 newlist.append(k)
#
#         raw_input('enter key')






