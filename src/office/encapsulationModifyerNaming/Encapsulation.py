'''
Created on 13-Feb-2019
Python have 3 level of access specifyer
    1. Public
    2. partial Private
    3. near about private
@author: GS-1629
'''
class AccessSpecifyer:
    def __init__(self):
        self.pub="Public"
        self._priv = "Private"
        self.__strickPriv = 'Mangling call'
        
    def refMethod(self):
        print(self.pub)
        print(self._priv)
        print(self.__strickPriv)  

class SecondLevelClass():
    def refMethod(self):
        print(AccessSpecifyer.pub)
        print(AccessSpecifyer._priv)
        print(AccessSpecifyer.__strickPriv)  

class ThirdLevelClass(AccessSpecifyer):
    def refMethod(self):
        print(super().pub)
        print(super()._priv)
        print(super().__strickPriv) 
                
def main():
    #First Level
    obj = AccessSpecifyer()
    obj.refMethod()
    print(obj.pub)
    print(obj._priv)
    print(obj._AccessSpecifyer__strickPriv)
    # Get information what are attribute inside AccessSpecifyer class
    print(obj.__dict__)
    
    #Second Level have confusion
    # Third Level have confusion
    o = ThirdLevelClass()
    print(o.pub)
    print(o._priv)
    print(o._AccessSpecifyer__strickPriv) 
    print(o.refMethod())
if __name__ == '__main__':
    main()