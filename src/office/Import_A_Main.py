'''
Created on 12-Feb-2019

@author: GS-1629
'''
class Class01:
    def c01(self):
        print('Class 01 --> c01')
        
class Class02:
    def c02(self):
        print('Class 02 --> c02')

def main():
    o1 = Class01()
    print(o1.c01())
    o2 = Class02()
    print(o2.c02())
      
if __name__ == '__main__':
    print('Module is directly run within same module')
    main()
else:
    print('Module is invoke from import module')