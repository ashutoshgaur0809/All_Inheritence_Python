class Parent:
    name = ""
    def eat(self):
        print("I can eat")

# Parent class inherited in child
class Child(Parent):
    
    def show(self):
        print("My name is ->",self.name)
        return self.name
        
# Create object of subclass
obj = Child()

# Access Superclass varible with subclass's obj
obj.name = "Ashutosh"
# Access subclass Function
s = obj.show() 
print(s)     
# Access Superclass Function
obj.eat()