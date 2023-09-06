a=[12,19,22,8,10]
for i in range(3):
    temp =a[0]
    a.remove(a[0])
    a.insert(len(a),temp)
print(a)
