class father:
    def fun(self):
        print("this is father class")
class mother:
    def fun1(self):
        print("this is mother class")
class child(father,mother):
    def fun3(self):
        print("this is child class")
obj=child()
obj.fun()
obj.fun1()
obj.fun3()
