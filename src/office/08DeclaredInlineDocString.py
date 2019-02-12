# Empty class sample
'This is docstring section for python file level'

class EmpltyClass:
    'This is docstring section for EmpltyClass Class level'
    def __init__(self,x):
        'This is Method Initializer Block similar to constructor of class EmpltyClass'
        print('Invoke EmpltyClass-->Initializer Method ',x)
        self.setterTest(x)
        
    def setterTest(self,x):
        self.x=x    
    
    def getterTest(self):
        print(self.x)
        
# Sample var & Method declaration 
class FirstLevelSample:
    'This is docstring section for FirstLevelSample Class level'
    i=10
    def testMethod(self):
        'This is docstring section for FirstLevelSample->testMethod() level'
        print('FirstLevelSample --> testMethod() ')

# Sample of Bean (Getter & Setter)
class Bean:
    'This is docstring section for Bean Class level'
    def __init__(self,x,y,z):
        'This is Method Initializer Block similar to constructor of class Bean'
        self.setter(x, y, z)
        
    def setter(self, x,y,z):
        'This is docstring section for setter Method level'
        self.x=x
        self.y=y
        self.z=z
        
    def getter(self):
        'This is docstring section for getter Method level'
        print(self.x, self.y, self.z)

def globalFunction(x,y):
    'This is docstring section for globalFunction Function level'
    return (x+y)


# Main method to invoke all class object and it's member
if __name__ == '__main__':
    'This is docstring section for Main Function level'
    e= EmpltyClass(10) # Creating object of Empty Class & invoke Initializer Method
    p1 = FirstLevelSample() # Creating object of FirstLevelSample Class
    p2=FirstLevelSample() # Creating object of FirstLevelSample Class
    p3 = Bean(11, 12, 13) # Creating object of Bean Class & invoke constructor/ Initializer method
    
    p1.x=10
    p1.y=20
    p2.sample='This is sample text'
    
    print(p1.x,p1.y)
    print(p1.i)
 
    print(p2.testMethod())
    print(p2.sample)
    
    print(p3.getter())
    
    # Different level of print doc String
    print(__doc__) # File level docString invoke
    print(EmpltyClass(10).__doc__) # class level
    print(FirstLevelSample().__doc__) # Class Level
    print(Bean(100,200,300).__doc__) # Class Level
    
    print(p1.testMethod.__doc__) # FirstLevelSample Class testMethod docString
    print(p3.getter.__doc__) # Bean Class getter Method docString
    print(p3.__init__.__doc__) # Bean Class Constructor docString
    
    print(globalFunction.__doc__) # Global function level docstring
    
    print(help(p3.getter))
    print(help(p3.__init__))