'''
Created on 12-Feb-2019

@author: GS-1629
'''

class Father:
    def setFeature(self, name, surname):
        print('This is Father class method')
        self.FirstName=name
        self.LastName=surname

    def getFeature(self):
        print(self.FirstName, self.LastName)
        
class ChildClass(Father):
    def setFeature(self, name, surname): # Method overriding
        print('This is Child class method')
        self.FirstName=name
        self.LastName=surname 

def identifyer():
    print(issubclass(Father, ChildClass))
    print(issubclass(ChildClass, Father))
    print(issubclass(Father, object))
    print(issubclass(ChildClass, object))
    print(issubclass(object, Father))
    
def main():
    obj1 = Father()
    obj2 = ChildClass()
    
    obj1.setFeature("AUtomation", "Python")
    print(obj1.getFeature())
    
    obj2.setFeature("Child Class Automation", "Child Python")
    print(obj2.getFeature())

if __name__ == '__main__':
    main()
    identifyer()