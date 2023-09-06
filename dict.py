bikes={
        "pulsar" : "1 lakh",
         "R15"   :"1.5lakh",
         "RoyalEenfield" : "2 lakh",
         "Bmw"   :"3 lakh"
         }
a = bikes.keys()
b = bikes.values()
print(a)
print(b)
bikes["Dio"]="90 thousand"
print(bikes)
bikes.pop("Bmw")
print(bikes)
bikes["R15"]=1.90
print(bikes)
bikes.popitem()
print(bikes)
bikes.update({"Harely":"5 lakh"})
print(bikes)
for x,y in bikes.items():
 print(x,y)


