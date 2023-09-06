x=input("enter the string:")
strr =" "
count=len(x)
while count>0:
    strr=strr + x[count-1]
    count=count-1
print("the reverse string is:",strr)
