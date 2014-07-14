num=1001*1001
coldiff=1000

sum=num
while coldiff>0:

    for i in range(1,5):
        num=num-coldiff
        sum+=num
    coldiff=coldiff-2
print sum



