'''
Created on 12-Feb-2019

@author: deepak
'''
class Opeartion():
    def StringOperation(self):
        s = 'Single quote string'
        print(s)
        print(id(s)) # Here we can see String var ID (Immutable-if value change, ID change)
        
        s="Double quote String"
        print(s)
        print(id(s)) 
        
        s="split string quote \n with operation"
        print(s)
        print(id(s))
        
        s=r"Double quote \n String"
        print(s)
        print(id(s)) 
        
        n=100
        s="{} Double quote String".format(n) # Python3 syntax working fine
        print(s)
        print(id(s)) 
        
        n=200
        s="%s Double quote String" %n # Python2 syntax is working fine
        print(s)
        print(id(s)) 
        
        s=''' 
        This allow you to print String 
        in several lines
        like docString '''
        print(s)
        print(id(s)) 
        
        s='''\
        This allow you to print String 
        in several lines
        like docString '''
        print(s)
        print(id(s)) 
        
if __name__ == '__main__':
    obj = Opeartion()
    obj.StringOperation()