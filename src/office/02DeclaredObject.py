# Empty class sample

class EmpltyClass:
    pass        
# Sample var & Method declaration 
class FirstLevelSample:
    print('First Hello From FirstLevelSample Class')

f1 = FirstLevelSample()
e = EmpltyClass()
print(end='\n')
print(e)
print(id(e))
print((type(e)))
print(end='\n')
print(f1)
print(id(f1))
print((type(f1)))

''' In python3 everything is object
    1. Object it self
    2. ID= unique ID which will never change during Execution
    3. Type = type of object which will never change during Execution
    4. value= may change during execution.
'''    