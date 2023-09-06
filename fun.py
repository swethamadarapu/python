def fun(a,b):
    return a>b
print(fun(1,2))

class A:
    x=1
    y=5

    def findmax(self):
        return self.x > self.y
obj = A()
print(obj.findmax())

obj1 = A()
print(obj1.x)


obj.x = 10
print(obj.findmax())
