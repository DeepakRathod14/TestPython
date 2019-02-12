'''
Created on 12-Feb-2019

@author: GS-1629
'''
class Vehical:
    def RunningType(self):
        print('Vehical will run on Road, Air, Water, track')

class AutomobileVehical(Vehical):
    def Type(self):
        print('Use by most of common public transport')
        
class NonAutomobileVehical(Vehical):
    def Type(self):
        print('No fuels are required') 
               
class FossileFual(AutomobileVehical):
    def FualAvarage(self, avarage):
        self.avarage=avarage
        print('Running by Different sources')
        print('Vehical fual avarage = '.format(self.avarage))

class Electronic(AutomobileVehical):
    def FualType(self):
        print('Running with Electricity')
        
class DisaleVarient(FossileFual):
    def FualAvarage(self,avarage):
        FossileFual.FualAvarage(self,avarage)

class PatrolVerient(FossileFual):
    def FualAvarage(self, avarage):
        FossileFual.FualAvarage(self, avarage)

class GasVerient(FossileFual):
    def FualAvarage(self, avarage):
        FossileFual.FualAvarage(self, avarage)

class AdvanceVehicals(Electronic):
    def TypesOfVehicals(self):
        print('4 wheels and 2 wheels electronics vehicals ')
    
class Bycicl(NonAutomobileVehical):
    def Feature(self):
        print('No fuel required & run on road')
    
    
"""
Vehical --> Automobile
                Fossile Fual,
                    Gas, Disel, Patrol
                Electronic
                    AdvanceVehicals.
Vehical --> Non-Automobile
                Bycicl """