class Parent:
    name = ""
    def eat(self):
        print("Parent is eating")
        
class Child1(Parent):
    midname = ""
    def show(self):
        print("Child 1 is showing ->",self.name,self.midname,self.lname)
    
    
class Child2(Parent):
    lname = ""
    def look(self):
        print("Child 2 is looking ->",self.name,self.midname,self.lname)
        

class Child3(Child1,Child2):
    def full(self):
        print("fULL NAME IS - >",self.name,self.midname,self.lname)
        
obj = Child3()
obj.name = "Ashu"
obj.midname = "tosh"
obj.lname = "gaur"

obj.full()
obj.eat()
obj.show()
obj.look()
    
    
    