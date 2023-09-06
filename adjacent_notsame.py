a="assdfghhjklllddcc"
c=list(a)
b = len(c)
count=0
for i in range (b-1):
    if c[i] == c[i+1]:
       count =count+1
 
  
print(c,count)


