"""a=input("enter a number:")
b=a[::-1]
if a==b:
    print("palindrome")
else:
    print("not a palindrome")"""

x=input("enter the string:")
strr =""
count=len(x)
while count>0:
    strr=strr + x[count-1]
    count=count-1
print("the reverse string is:",strr)
if(strr==x):
    print("it is a palindrome string")
else:
    print("it in not a palindrome!")


