'''
Created on 13-Feb-2019
There are so many other operators which we can overload in similar ways
@author: GS-1629
'''
class operator:
    def __init__(self, a, b, c):
        print('sample code fo operator overload')
        self.a=a
        self.b=b
        self.c=c
    
    def __str__(self):
        return ('{}, {}, {} '.format(self.a, self.b, self.c))

    def __add__(self, other):
        self.a=self.a+other.a
        self.b=self.b+other.b
        self.c=self.c+other.c
        return operator(self.a,self.b,self.c)
    
def main():
    obj = operator(1,2,3)
    obj1 = operator(2,3,1)
    
    print(obj)        
    print(obj1)
    
    print(obj+obj1)
    

if __name__ == '__main__':
    main()