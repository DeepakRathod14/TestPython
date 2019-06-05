# Empty class sample

class EmpltyClass:
        
    def setterTest(self,x):
        self.x=x    
    
    def getterTest(self):
        print(self.x)
        
# Sample of Bean (Getter & Setter)
class Bean:
    
    def __init__(self):
        print("Const")
            
    def setter(self, x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def getter(self):
        print(self.x, self.y, self.z)

if __name__ == '__main__':
    e= EmpltyClass() # Creating object of Empty Class & invoke Initializer Method
    print(e.setterTest(55))
    print(e.getterTest())
    
    p3 = Bean() # Creating object of Bean Class & invoke constructor/ Initializer method
    p3.setter(11, 12, 13)
    print(p3.getter())
