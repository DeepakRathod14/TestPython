'''
Created on 13-Feb-2019

@author: GS-1629
'''
class BasicConditions():
    def ConditionFirstLevel(self, name="None"):
        if name == "None" or name == '':
            print('Your name is : {}'.format(name))
        else:
            print('Your name is : {}'.format(name))

def main():
    obj = BasicConditions()
    obj.ConditionFirstLevel()
    obj.ConditionFirstLevel('Deepak')
    obj.ConditionFirstLevel('Rathod')
    obj.ConditionFirstLevel('None')
    obj.ConditionFirstLevel('none')
    obj.ConditionFirstLevel('')
    
if __name__ == '__main__':
    main()