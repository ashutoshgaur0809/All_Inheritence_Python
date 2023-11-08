class Mom:
    mname = ""
    def eat(self):
        print("Mom is eating")
        
class Dad:
    fname = ""
    def eat(self):
        print("Dad is eating")
    
    
class Child(Dad,Mom):
    
    def show(self):
        print("child ki mom ->",self.mname,"child k Dad ->",self.fname)
        
c1 = Child()
c1.mname = "Nidhi"
c1.fname = "Abhishek"
c1.show()
c1.eat()