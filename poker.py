import operator
import collections
import itertools

from itertools import groupby
import string
def FourOfAKind(y):
    x=collections.defaultdict(list)

    for i in y:
        if i[0]=='J':
            x[i[1]].append(11)
        elif i[0]=='Q':
            x[i[1]].append(12)
        elif i[0]=='K':
            x[i[1]].append(13)
        elif i[0]=='A':
            x[i[1]].append(14)
        elif i[0]=='T':
            x[i[1]].append(10)
        else:
            x[i[1]].append(int(i[0]))


# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.


    lis=sorted(['T','K','A','Q','J'])
    iterval=list(itertools.chain.from_iterable(x.values()))

    # print '***' ,max(iterval),x

    if lis==sorted(iterval):
        return 23,'Royal Flush: Ten, Jack, Queen, King, Ace, in same suit'
    if len(x.keys())==1:
       for k, g in groupby(enumerate(sorted(iterval)), lambda (i,x):i-x):
           if map(operator.itemgetter(1), g)==sorted(x.values()[0]):
               return 22,max(iterval),'Straight Flush: All cards are consecutive values of same suit'
    if 4 in collections.Counter(iterval).values():
        return 21,x,'Four of a Kind: Four cards of the same value'
    if 5 in collections.Counter(iterval).values():
        return 21,x,'Four of a Kind: Four cards of the same value'
    if 3 in collections.Counter(iterval).values() and 2 in collections.Counter(iterval).values() :
        return 20,x,'Full House: Three of a kind and a pair'

    if len(x.keys())==1:
        return 19,x,'Flush: All cards of the same suit'

    for k, g in groupby(enumerate(sorted(iterval)), lambda (i,x):i-x):
           if map(operator.itemgetter(1), g)==sorted(iterval):
               return 18,x,'Straight: All cards are consecutive values.'
    if 3 in collections.Counter(iterval).values():
        return 17,x,'Three of a Kind: Three cards of the same value'

    if len(collections.Counter(iterval).values())==3 and 2 in collections.Counter(iterval).values():
        return 16,x,'Two Pairs: Two different pairs'
    if 2 in collections.Counter(iterval).values():
        return 15,x,'One Pair: Two cards of the same value.'
    else:
        return max(iterval),x,'max value'






# y="JH 3C 5S 4D AD"
#
#
# print FourOfAKind(y)

with open('poker.txt','r') as file:

    for line in file:
        print line[:5],line[5:]
        line=line.split()
        print FourOfAKind(line[:5])
        print FourOfAKind(line[5:])
        raw_input('press key')





