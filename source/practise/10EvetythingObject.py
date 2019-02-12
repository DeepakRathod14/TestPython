# Empty class sample
from xmlrpclib import boolean

class EmpltyClass:
        
    def setterTest(self,x):
        self.x=x    
    
    def getterTest(self):
        print(self.x)
        
# Sample of Bean (Getter & Setter)
class Bean:
        
    def setter(self, x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def getter(self):
        print(self.x, self.y, self.z)


if __name__ == '__main__':
    print(type(5))
    print(type(5.5))
    print(type('A'))
    print(type("Sample"))
    print(type(boolean))
    print(type((1,2,3)))
    print(type([1,2,3]))
    
    e=EmpltyClass()
    print(type(e))
    print(type(Bean))
    print((type(EmpltyClass)))
    print(type(type))
    print(type(12345678985321231534531232135431215435132121543514354534543543512151))
    print(type(__doc__))
    
    