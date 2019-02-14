'''
Created on 12-Feb-2019
https://www.xvideos.com/video22077915/asian_flowerr_s_cam_show
@author: deepak
'''
class A:
    def __init__(self,a):
        print('A class'.format(a))

class B(A):
    def __init__(self,a):
        super().__init__(a)
        print('B class')

def sample():
    obj = A(100)
    obj1 = B(200)
    
    print(obj)
    print(obj1)
    
if __name__ == '__main__':
    sample()