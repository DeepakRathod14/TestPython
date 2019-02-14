'''
Created on 12-Feb-2019

@author: deepak
'''
class Operation():
    def calculation(self):
        num=10
        print(type(num),num)
        
        num=10.00
        print(type(num),num)

        num=10/5
        print(type(num),num)

        num=10//5
        print(type(num),num)

        num=round(10/3, 3)
        print(type(num),num)
        
        num=10%4
        print(type(num),num)
        
        num= int(10.9686)
        print(type(num),num)

        num=float(10)
        print(type(num),num)
''' when I say float(10) or int(1o) round(10/3).... 
    it is actually creating object and value pass to constructor (Initializer Method)
'''
        
def main():
    obj = Operation()
    obj.calculation()
    
if __name__ == '__main__':
    main()
        