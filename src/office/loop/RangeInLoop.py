'''
Created on 12-Feb-2019

@author: deepak
'''
class A:
    def printing(self, num1=15): # Default argument, it will pick this value while we not pass any argument.
        print('Sample Number print')
        for i in range(num1,20):
            print(i)
    
def test(num):
    for i in range(num,20):
        print(i)

if __name__ == '__main__':
    obj = A()
    obj.printing(17)
    obj.printing(18)
    obj.printing()