'''
Created on 12-Feb-2019

@author: GS-1629
'''
class Person:
    def personIdentyfication(self,name,age):
        self.name=name
        self.age=age

class emp(Person):
    def employeeIdentification(self,empID):
        self.empID=empID
        
class assignment(emp):
    def assignmentIdentification(self, language):
        self.lagn=language
    
    def __str__(self):
        return (self.name+", "+str(self.age)+", "+str(self.empID)+", "+self.lagn)
    
def main():
    obj = assignment()
    obj.personIdentyfication("Deepak Rathod", 33)
    obj.employeeIdentification(1629)
    obj.assignmentIdentification("Python")
    print(obj)
    
if __name__ == '__main__':
    main()