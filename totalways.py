line=''
with open('name.txt','r') as file:
    for line in file:
        line=line.replace('"','').split(',')

a='hai'
print

# .print [map(lambda  ,i) for i in line]