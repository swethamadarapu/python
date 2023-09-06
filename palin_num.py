num = int(input("enter the number:"))
temp = num
rem=0
#rem=0
while(num>0):
    rev=num%10
    rem=rem*10+rev
    num=num//10
if(temp==rem):
    print("it is a palindrome")
else:
    print("it is not")






