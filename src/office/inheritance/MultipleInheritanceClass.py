'''
Created on 12-Feb-2019

@author: GS-1629
'''

class A:
    def test(self):
        print("Hello from A...")
        
class B:
    def test(self):
        print('Hello from B...')

class C(B,A):
    pass

def main():
    obj = C()
    obj.test()
    
if __name__ == '__main__':
    main()