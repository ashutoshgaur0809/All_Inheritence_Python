class Parent:
    name = ""
    def eat(self):
        print("Parent is eating")
        
class Child1(Parent):
    
    def show(self):
        print("Child 1 is showing ->",self.name)
    
    
class Child2(Parent):
    
    def show(self):
        print("Child 2 is looking ->",self.name)
        
c1 = Child1()
c2 = Child2()

c1.name = "Ashu"
c1.show()
c1.eat()

c2.name = "Prince"
c2.show()
c2.eat()