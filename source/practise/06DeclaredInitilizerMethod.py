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
        print('Invoke Bean-->Initializer Method ',x,y,z)
        self.setter(x, y, z)
        
    def setter(self, x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def getter(self):
        print(self.x, self.y, self.z)


# Main method to invoke all class object and it's member
if __name__ == '__main__':
    'This is docstring section for Main Function level'
    e= EmpltyClass(10) # Creating object of Empty Class & invoke Initializer Method
    print(e.getterTest())
    
    p3 = Bean(11, 12, 13) # Creating object of Bean Class & invoke constructor/ Initializer method
    print(p3.getter())
