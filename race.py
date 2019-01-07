# -*- coding: utf-8 -*-
from string import ascii_uppercase
from random import random, randint, choice,uniform as randchoice

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]

class TrackPart:
   def __init__(self, length=None, terrain=None , complexity=None):
    
    self.length = randint(0,10)
    self.terrain = choice(["asphalt","sand","mud","rocky"])
    self.complexity = choice(["normal","rapid","subtle"])
    
    
class Tack():
    def generation(self, num):
        parts = []
        for i in range (0, num):
            p = TrackPart()
            
            parts.append(p)
        return parts
       
    def __init__(self, parts=None):
      if parts is None :
          self.parts = self.generation(20)
      else:    
          self.parts = self.generation(parts)
    
    
class Pilot():
     def __init__(self, name=None,normal_speed=None,rapid_speed=None,subtle_speed=None):
         self.name = choice(ascii_uppercase)
         self.normal_speed = randchoice(0.5,1.5)
         self.rapid_speed = randchoice(0.5,1.5)
         self.subtle_speed = randchoice(0.5,1.5)
    
class Car(): 
     def __init__(self, name=None, pilot=Pilot(), asphalt_speed=None,sand_speed=None,mud_speed=None,rocky_speed=None):
         self.name= randint(1,20)
         self.pilot= pilot
         self.asphalt_speed=randchoice(0.5,1.5)
         self.sand_speed=randchoice(0.5,1.5)
         self.mud_speed=randchoice(0.5,1.5)
         self.rocky_speed=randchoice(0.5,1.5)
         
def time_for_part(My_terrain, My_car, My_pilot):
    
    
    if My_terrain.terrain is "asphalt" and My_terrain.complexity is "normal":       
        Speed = 1 + My_pilot.normal_speed * My_car.asphalt_speed
        Time = My_terrain.length / Speed
    elif  My_terrain.terrain is "asphalt" and My_terrain.complexity is "rapid":
        Speed = 1 + My_pilot.rapid_speed * My_car.asphalt_speed
        Time = My_terrain.length / Speed
    elif My_terrain.terrain is "asphalt" and My_terrain.complexity is "subtle":       
        Speed = 1 + My_pilot.subtle_speed * My_car.asphalt_speed
        Time = My_terrain.length / Speed
    elif My_terrain.terrain is "sand" and My_terrain.complexity is "normal":       
        Speed = 1 + My_pilot.normal_speed * My_car.sand_speed
        Time = My_terrain.length / Speed
    elif  My_terrain.terrain is "sand" and My_terrain.complexity is "rapid":
        Speed = 1 + My_pilot.rapid_speed * My_car.sand_speed
        Time = My_terrain.length / Speed
    elif My_terrain.terrain is "sand" and My_terrain.complexity is "subtle":       
        Speed = 1 + My_pilot.subtle_speed * My_car.sand_speed
        Time = My_terrain.length / Speed
    elif My_terrain.terrain is "mud" and My_terrain.complexity is "normal":       
        Speed = 1 + My_pilot.normal_speed * My_car.mud_speed
        Time = My_terrain.length / Speed
    elif  My_terrain.terrain is "mud" and My_terrain.complexity is "rapid":
        Speed = 1 + My_pilot.rapid_speed * My_car.mud_speed
        Time = My_terrain.length / Speed
    elif My_terrain.terrain is "mud" and My_terrain.complexity is "subtle":       
        Speed = 1 + My_pilot.subtle_speed * My_car.mud_speed
        Time = My_terrain.length / Speed
    elif My_terrain.terrain is "rocky" and My_terrain.complexity is "normal":       
        Speed = 1 + My_pilot.normal_speed * My_car.rocky_speed
        Time = My_terrain.length / Speed
    elif  My_terrain.terrain is "rocky" and My_terrain.complexity is "rapid":
        Speed = 1 + My_pilot.rapid_speed * My_car.rocky_speed
        Time = My_terrain.length / Speed
    elif My_terrain.terrain is "rocky" and My_terrain.complexity is "subtle":       
        Speed = 1 + My_pilot.subtle_speed * My_car.rocky_speed
        Time = My_terrain.length / Speed
  
    return Time



def time_for_track(track,car,pilote):
    time = 0
    for tronçons in piste :
        
        time = time + time_for_part(tronçons, car, pilote)

    return time




####### Génération d'une piste de 20 tronçons
print ("#### Génération d'une piste de 20 tronçons #### \n")

mes_tronçons= Tack()
piste= mes_tronçons.parts
for pis in piste:
  print (pis.complexity,",",pis.terrain,"(",pis.length,")")
print ("\n")
###### Génération 5 voitures avec pilotes
print ("#### Génération 5 voitures avec pilotes ####\n")
list_car_pilot = []

for i in range (0, 5):
    car = Car()
    pilot = Pilot()
    list_car_pilot.append((car,pilot))
    print ("Car",car.name,"with Pilot",pilot.name)
print ("\n")
print ("#### Affichage du temps ####\n")
times=[]       

for (voiture,pilot) in list_car_pilot:
    
        Time1 = time_for_track(piste , voiture, pilot)
        times.append([Time1,(voiture.name,pilot.name)])
#print (times)
        
for t in times:
    print("["+str(t[0]),", Car",t[1][0],"with Pilot",t[1][1]+"]")
    
print ("\n")
print ("#### Affichage du vainqueur  ####\n")

small_time = times[0][0]
index = times[0]
for t in times:
    if t[0] < small_time:
        small_time=t[0]
        index= t
print ("the winner is Car :",index[1][0], "with Pilot",index[1][1],"with Time :",index[0] )
