'''
Created on 12-Feb-2019

@author: GS-1629
'''

class Organisation:
    def setFeature(self, name, surname, age):
        print('This is Organisation class method')
        self.FirstName=name
        self.LastName=surname
        self.age = age
    
    def __str__(self):
        return ("FirstName = "+self.FirstName+" , LastName = "+self.LastName+", Age = "+str(self.age))
        
class Employee(Organisation):
    
    def __init__(self,a):
        print("Initializer Method --> {}".format(a))
    
    def setFeature(self, name, surname, age, sal):
        print('This is Organisation class method')
        self.FirstName=name
        self.LastName=surname
        self.age = age
        self.sal=sal
        
    def __str__(self):
        return (super().__str__() +", Salary = "+str(self.sal))

class Labor(Employee):
    def __init__(self,a):
        super().__init__(a)
     
    def setFeature(self, name, surname, age, sal, incomeTax):
        Employee.setFeature(self, name, surname, age, sal)
        self.incomeTax=incomeTax

    def __str__(self):
        return (super().__str__() +", Income Tax = "+str(self.incomeTax))
         
def main():
    obj = Organisation()
    obj1 = Employee(33)
    obj2 = Labor(44)
    
    obj.setFeature("Deepak", "Rathod", 32)
    obj1.setFeature("Deepak I", "Rathod", 33, 15000)
    obj2.setFeature("Rathod", "Deepak", 35, 20000, 800)
    
    print(obj)
    print(obj1)
    print(obj2)
if __name__ == '__main__':
    main()