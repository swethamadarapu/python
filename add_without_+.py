def add(a,b):
 while(b!=0):
  c=a&b
  a=a^b
  b=c<<1
 return a
 #print(f"sum of two numbers are:{a}")
print(add(22,19))

