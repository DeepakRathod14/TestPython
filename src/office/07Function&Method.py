# Empty class sample

class EmpltyClass:
    def __init__(self,x):
        print('Invoke EmpltyClass-->Initializer Method ',x)
        self.setterTest(x)
        
    def setterTest(self,x):
        self.x=x    
    
    def getterTest(self):
        print(self.x)
        
# Sample of Bean (Getter & Setter)
class Bean:
    def __init__(self,x,y,z):
        self.setter(x, y, z)
        
    def setter(self, x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def getter(self):
        print(self.x, self.y, self.z)

def globalFunction(x,y):
    return (x+y)


# Main method to invoke all class object and it's member
if __name__ == '__main__':
    e= EmpltyClass(10) # Creating object of Empty Class & invoke Initializer Method
    print(e.getterTest())
    
    p3=Bean(100,200,300)
    print(p3.getter())
    
    print(globalFunction(10, 10))
    
