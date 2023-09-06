num=[2,11,3,6,33,69,90,21,24]
min=num[0]
max=num[0]
for i in range(len(num)):
  if num[i]>max:
   max=num[i]
  elif num[i]<min:
    min=num[i]
print("min:",min)
print("max:",max)


