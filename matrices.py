import itertools
str="11<->23,12 <->9,3 <-> 16,14<->2,23 <->  9,20 <->34,18 <-> 3,12<->4"
str=str.replace(' ','').split(',')
str= dict([i.split("<->") for i in str ])

list=[]


for i in str.items():
    sublist=[]
    sublist.append(i[0])
    key=i[0]
    val=i[1]
    while True:
        if val in str.keys():
            sublist.append(val)
            val=str[val]
            key=val
            if key in str.keys():
                del str[key]
        else:
            list.append(sublist)
            break
print list








