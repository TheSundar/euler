s= str(316)
values=[]
if len(s)%2!=0:
    values.append(int(s[0]))
    s=s[1:]
if len(s)%2==0:
    for i in range(0,len(s),2):
        values.append(int(s[i:i+2]))
div=0
res=0
flag=False
for element in values:
    element=res*100+element
    for i in range(1,10):
        temp=(div *10)+i
        if element == temp * i:
            div+=temp
            break
        elif element < temp * i:
            div+=temp-1
            res=element-(div* i-1)
            if res<0:
                flag=True
                break
        if flag:
            break




print div






