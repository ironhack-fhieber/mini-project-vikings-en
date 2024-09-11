from vikingsClasses import Viking, Saxon, War
import random

war = War()
min_strength = 20
max_strength = 35
soldier_names = ["Ragnar", "Bjoern", "Leif", "Erik", "Sven", "Harald", "Ivar", "Gunnar", "Sigurd", "Skadi"]

#Create 5 Vikings
for i in range(0,5):
    war.addViking(Viking(soldier_names[random.randint(0,9)],100,random.randint(min_strength, max_strength)))

#Create 5 Saxons
for i in range(0,5):
    war.addSaxon(Saxon(100,random.randint(min_strength, max_strength)))
    
round = 1
while war.stillActive():
    print(f"==== Round: {round} ====")
    print(war.vikingAttack())
    if war.stillActive():
        print(war.saxonAttack())

    print("Viking army: {len(war.vikingArmy)} warriors left || Saxon army: {len(war.saxonArmy)} warriors left")
    print(war.showStatus())

    round += 1
    print('')