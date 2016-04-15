# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 17:41:21 2016
This program contains functions to roll damage for specific weapons in 5e.
@author: amade
"""

"Import packages"
from random import randint
from math import ceil

"Assign and display global variables."
strbonus = 8
profbonus = 5


def flametongue2hands(numberattacks,GWM):
    allattackslashingtotal = 0
    allattackfiretotal = 0
        
    for i in range(1,numberattacks+1):
        print("\nAttack Number %d:" %i)        
        
        """slashing damage"""        
        slashing = randint(1,10)
        if slashing <= 2:
            print("""Slashing die rolled a %d, reroll.""" % slashing)
            slashing = randint(1,10)
        print("Slashing Die = %d" %slashing)
        slashingbonus = (ceil(1.5*strbonus)+profbonus)   
        print("Slashing Bonus = %d" %slashingbonus)
        slashing += slashingbonus
        "Great Weapons Master Feat bonus damage"
        if GWM == True:
            print("+10 damage from GWM feat")            
            allattackslashingtotal += 10
        
        """fire damage"""
        firetotal = 0
        for i in range (1,3):
            firedie = randint(1,6)
            if firedie <= 2:
                print("Fire Die number %d rolled a %d, reroll." %(i,firedie))
                firedie = randint(1,6)
            print("Fire Die number %d = %d" % (i,firedie))
            firetotal += firedie
        
        allattackslashingtotal += slashing
        allattackfiretotal += firetotal
        
        
        print("%d slashing damage \n%d fire damage" % (slashing,firetotal))
    
    print("""\nTotal: \n%d slashing damage \n%d fire damage""" % (allattackslashingtotal,allattackfiretotal))
    
    
    
def vengeance(numberattacks,GWM):
    allattackslashingtotal = 0
    
    for i in range (1,numberattacks+1):
        
        """slashing damage"""
        print("\nAttack Number %d" %i)
        slashtotal = 0
        for i in range (1,3):
            slashdie = randint(1,6)
            if slashdie <= 2:
                print("Slashing Die number %d rolled a %d, reroll" %(i,slashdie))
                slashdie = randint(1,6)
            print("Slashing Die number %d = %d" %(i,slashdie))
            slashtotal += slashdie
        slashingbonus = (ceil(1.5*strbonus)+profbonus+1)   
        print("Slashing Bonus = %d" %slashingbonus)
        slashtotal += slashingbonus
        allattackslashingtotal += slashtotal
        
        "Great Weapons Master Feat bonus damage"
        if GWM == True:
            print("+10 damage from GWM feat")            
            allattackslashingtotal += 10
    print("\nTotal:\n%d slashing damage" %allattackslashingtotal)




vengeance(3,GWM=True)
#flametongue2hands(3,GWM=True)