# x,y,z=1,1,1
# a=55385
# print (a*(a+1)/2)
#
#
# for a in xrange(x,100000):
#     for b in xrange(1,a):
#         if (a*(a+1)/2) < (b*((3*b)-1)/2):break
#         if (a*(a+1)/2) > (b*((3*b)-1)/2):continue
#         for c in xrange(1,b):
#             if (b*((3*b)-1)/2)<(c*(2*c-1)):break
#             if (b*((3*b)-1)/2)>(c*(2*c-1)):continue
#
#             if (a*(a+1)/2)==(b*((3*b)-1)/2) and (b*((3*b)-1)/2)==(c*(2*c-1)):
#                 print a,b,c


from math import sqrt
for x in xrange(285,10000000):
	c = (x**2 + x)/2
	y = (.5 + sqrt(.25 + 6*c))/3
	z = (1 + sqrt(1 + 8*c))/4

	if y - int(y) == 0 and z - int(z) == 0:
		print 'x = %d' % x
		print 'y = %d' % y
		print 'z = %d' % z
