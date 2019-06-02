'''
Created on 13-Feb-2019

@author: GS-1629
'''
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
    
    def food(self):
        print('somethihng')
    
class Human(Animal):
    def move(self):
        print('I can walk and Run')
        Animal.food(self)
    
class Snack(Animal):
    def move(self):
        print('It can scrolling on ground')
        
def main():
    h1 = Human()
    h1.move()
    
    s1 = Snack()
    s1.move()
    
    '''a1 = Animal()
    print(a1.move()) '''

if __name__ == '__main__':
    main()