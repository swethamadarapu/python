myDict = {1: "swetha", 2:"sunny", 3:"sai", 4:"sagar", 5:"swathi"}
#print(len(myDict))
l1 = []
l2 =[]
l1 = myDict.keys()
l2 = myDict.values()
print(l1)
'''
for key,value in myDict.items():
    l1.append(key)
    l2.append(value)'''
myDict.clear()
for i in range(len(l1)):
    myDict[l2[i]] = l1[i]
print(myDict)
        
'''for key,value in myDict.items():
    myDict.update({value : key})
    del myDict[next(iter(myDict))]
print(myDict)'''

