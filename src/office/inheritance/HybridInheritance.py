'''
Created on 12-Feb-2019

@author: GS-1629
'''
class A():
    def m(self):
        print('A class method M...')

class B(A):
    def m(self):
        A.m(self)
        print('B class method M...')
        
class C(A):
    def m(self):
        A.m(self)
        print('C class method M...')
        
class D(B,C):
    def m(self):
        B.m(self)
        C.m(self)
        A.m(self)
        print('D class method M...')


class A1():
    def m(self):
        print('A class method M...')

class B1(A1):
    def m(self):
        super().m()
        print('B class method M...')
        
class C1(A1):
    def m(self):
        super().m()
        print('C class method M...')
        
class D1(B1,C1):
    def m(self):
        super().m()
        print('D class method M...')
def main():
    obj = D()
    obj.m()
    print('--------- RESOLVED DIMON DEATH PROBLEM --------')
    
    obj1 = D1()
    obj1.m()
    
if __name__ == '__main__':
    main()
