import time

import time
tStart = time.time()
f = open("names.txt", "r").readlines()
values = []
for line in f:
    temp = []
    for token in line.replace("\n", "").split(' '):
        temp.append(token)
    values.append(temp)
print values
values.reverse()
print values
for i in range(0, len(values) - 1):
    j = 0
    for k in values[i+1]:
        values[i+1][j] = max([int(k) + int(values[i][j]), int(k) + int(values[i][j+1])])
        j += 1
print str(values[len(values)-1][0])
print "Run Time = " + str(time.time() - tStart)

triangle =             """75
                         95 64
                       17 47 82
                     18 35 87 10
                   20 04 82 47 65
                 19 01 23 75 03 34
                88 02 77 73 07 63 67
              99 65 04 28 06 16 70 92
            41 41 26 56 83 40 80 70 33
          41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
      70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


triangle_array = [[int(n) for n in line.split()] 
		   for line in triangle.split('\n')]

print triangle_array

def max_path(tr):

    if len(tr) == 1: 
        return tr[0][0]

    else:
        return sum([ tr[0][0], 
                     max( max_path( [ line[1:] for line in tr[1:] ] ),
                          max_path( [ line[:-1] for line in tr[1:] ] ) 
                         )
                   ])


start = time.time()
max_sum = max_path(triangle_array)
stop = time.time() - start

print("Answer = {0}".format(max_sum))
print("Elapsed time: {0:.6f}".format(stop))

fi = open('names.txt', 'r')
Tri=[]
for line in fi:
    Tri.append( map( int, line.split() ) )

print '***'
print Tri

ms=0 # maxsum
def sub( r, c, s ): # row, column, sum
    r+=1
    if r==len(Tri):
        global ms
        if s>ms: ms=s
        return
    for i in [0,1]: sub( r, c+i, s+Tri[r][c+i] )


sub( 0, 0, Tri[0][0] )
print ms