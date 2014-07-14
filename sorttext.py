
def value(str):
    val=0
    for i in str:
        val+=ord(i)-64

    return val


with open('names.txt','r') as file:
    for line in file:
        string=line
        line=line.replace('"','')
        line=sorted(line.split(','))


        print sum([(i[0]+1)*value(i[1]) for i in enumerate(line)])


