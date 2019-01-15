# -*- coding: utf-8 -*-
from string import ascii_uppercase
from random import random, randint, choice, uniform as randchoice

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]

class TrackPart:
   def __init__(self, length=None, terrain=None, complexity=None):
    
    self.length = randint(0, 10)
    self.terrain = choice(["asphalt","sand","mud","rocky"])
    self.complexity = choice(["normal","rapid","subtle"])
    
    
class Tack():
    def generation(self, num):
        parts = []
        for i in range (0, num):
            part = TrackPart()
            
            parts.append(part)
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
    
     def time_for_part(self,my_terrain, my_car, my_pilot):
    	    
    	    if my_terrain.terrain is "asphalt" and my_terrain.complexity is "normal":
    	        speed = 1 + my_pilot.normal_speed * my_car.asphalt_speed
    	        time = my_terrain.length / speed
    	    elif  my_terrain.terrain is "asphalt" and my_terrain.complexity is "rapid":
    	        speed = 1 + my_pilot.rapid_speed * my_car.asphalt_speed
    	        time = my_terrain.length / speed
    	    elif my_terrain.terrain is "asphalt" and my_terrain.complexity is "subtle":       
    	        speed = 1 + my_pilot.subtle_speed * my_car.asphalt_speed
    	        time = my_terrain.length / speed
    	    elif my_terrain.terrain is "sand" and my_terrain.complexity is "normal":       
    	        speed = 1 + my_pilot.normal_speed * my_car.sand_speed
    	        time = my_terrain.length / speed
    	    elif  my_terrain.terrain is "sand" and my_terrain.complexity is "rapid":
    	        speed = 1 + my_pilot.rapid_speed * my_car.sand_speed
    	        time = my_terrain.length / speed
    	    elif my_terrain.terrain is "sand" and my_terrain.complexity is "subtle":       
    	        speed = 1 + my_pilot.subtle_speed * my_car.sand_speed
    	        time = my_terrain.length / speed
    	    elif my_terrain.terrain is "mud" and my_terrain.complexity is "normal":       
    	        speed = 1 + my_pilot.normal_speed * my_car.mud_speed
    	        time = my_terrain.length / speed
    	    elif  my_terrain.terrain is "mud" and my_terrain.complexity is "rapid":
    	        speed = 1 + my_pilot.rapid_speed * my_car.mud_speed
    	        time = my_terrain.length / speed
    	    elif my_terrain.terrain is "mud" and my_terrain.complexity is "subtle":       
    	        speed = 1 + my_pilot.subtle_speed * my_car.mud_speed
    	        time = my_terrain.length / speed
    	    elif my_terrain.terrain is "rocky" and my_terrain.complexity is "normal":       
    	        speed = 1 + my_pilot.normal_speed * my_car.rocky_speed
    	        time = my_terrain.length / speed
    	    elif  my_terrain.terrain is "rocky" and my_terrain.complexity is "rapid":
    	        speed = 1 + my_pilot.rapid_speed * my_car.rocky_speed
    	        time = my_terrain.length / speed
    	    elif my_terrain.terrain is "rocky" and my_terrain.complexity is "subtle":       
    	        speed = 1 + my_pilot.subtle_speed * my_car.rocky_speed
    	        time = my_terrain.length / speed
    	  
    	    return time


     def time_for_track(self,track,car,pilote):
        time = 0
        for troncons in track:
            time = time + self.time_for_part(troncons, car, pilote)
        return time


def main():

	####### Génération d'une piste de 20 troncons
	print ("#### Génération d'une piste de 20 troncons #### \n")

	mes_troncons= Tack()
	piste= mes_troncons.parts
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
	    
	        time1 = car.time_for_track(piste , voiture, pilot)
	        times.append([time1,(voiture.name,pilot.name)])
	#print (times)
	        
	for time in times:
	    print("["+str(time[0]),", Car",time[1][0],"with Pilot",time[1][1]+"]")
	    
	print ("\n")
	print ("#### Affichage du vainqueur  ####\n")

	small_time = times[0][0]
	index = times[0]
	for time in times:
	    if time[0] < small_time:
	        small_time=time[0]
	        index= time
	print ("the winner is Car :",index[1][0], "with Pilot",index[1][1],"with time :",index[0] )
main()