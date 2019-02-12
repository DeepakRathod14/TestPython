'''
Created on 12-Feb-2019

@author: GS-1629
'''
from office import Import_A
from office import Import_A as AName
from . import Import_A as BName
from office.Import_A_Main import Class01, Class02, main

print(AName.__file__)
print(BName.__file__)
print(Import_A)
print(Class01)
print(Class02)
print(main())