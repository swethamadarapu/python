d = dict({1:"a",2:"b",3:"c",4:"d",5:"e"})
print(d.keys())
for i in d.keys():

    if i%2==0:
        d[i]="swetha"
print(d)
