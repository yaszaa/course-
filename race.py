# -*- coding: utf-8 -*-
""" missing doctring """
from string import ascii_uppercase
from random import randint, choice, uniform as randchoice

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]

class TrackPart:
    """ missing doctring """
    # pylint: disable=R0903
    def __init__(self, length=None, terrain=None, complexity=None):
        # pylint: disable=W0612,W0613
        self.length = randint(0, 10)
        self.terrain = choice(["asphalt", "sand", "mud", "rocky"])
        self.complexity = choice(["normal", "rapid", "subtle"])

class Track():
    """ class Track """
    # pylint: disable=R0903
    @staticmethod
    def generation(num):
        """ je suis generation """
        parts = []
        for _ in range(0, num):
            part = TrackPart()
            parts.append(part)
        return parts

    def __init__(self, parts=None):
        """ je suis init """
        if parts is None:
            self.parts = self.generation(20)
        else:
            self.parts = self.generation(parts)

class Pilot():
    """ class Pilot """
    # pylint: disable=R0903
    def __init__(self):
        # pylint: disable=W0612,W0613
        self.name = choice(ascii_uppercase)
        self.normal_speed = randchoice(0.5, 1.5)
        self.rapid_speed = randchoice(0.5, 1.5)
        self.subtle_speed = randchoice(0.5, 1.5)

class Car():
    """ class Car """
    # pylint: disable=too-many-arguments
    def __init__(self,
                 name=None,
                 pilot=Pilot(),
                 asphalt_speed=None,
                 sand_speed=None,
                 mud_speed=None,
                 rocky_speed=None):
    # pylint: disable=W0613
        if name is None:
            self.name = randint(1, 20)
        else:
            self.name = name
        self.pilot = Pilot()
        if asphalt_speed is None:
            self.asphalt_speed = randchoice(0.5, 1.5)
        else:
            self.asphalt_speed = asphalt_speed
        if sand_speed is None:
            self.sand_speed = randchoice(0.5, 1.5)
        else:
            self.sand_speed = sand_speed
        if mud_speed is None:
            self.mud_speed = randchoice(0.5, 1.5)
        else:
            self.mud_speed = mud_speed
        if rocky_speed is None:
            self.rocky_speed = randchoice(0.5, 1.5)
        else:
            self.rocky_speed = rocky_speed
    def time_for_part(self, part, pilot):
        """ fonction time for part """
        # pylint: disable=W0613, R0912
        speed = 1
        if part.terrain == "asphalt":
            speed *= self.asphalt_speed
            if part.complexity == "normal":
                speed *= self.pilot.normal_speed
                time = part.length / speed
            elif part.complexity == "rapid":
                speed *= self.pilot.rapid_speed
                time = part.length / speed
            elif part.complexity == "subtle":
                speed *= self.pilot.subtle_speed
                time = part.length / speed
        elif part.terrain == "sand":
            speed *= self.sand_speed
            if part.complexity == "normal":
                speed *= self.pilot.normal_speed
                time = part.length / speed
            elif part.complexity == "rapid":
                speed *= self.pilot.rapid_speed
                time = part.length / speed
            elif part.complexity == "subtle":
                speed *= self.pilot.subtle_speed
                time = part.length / speed
        elif part.terrain == "mud":
            speed *= self.mud_speed
            if part.complexity == "normal":
                speed *= self.pilot.normal_speed
                time = part.length / speed
            elif part.complexity == "rapid":
                speed *= self.pilot.rapid_speed
                time = part.length / speed
            elif part.complexity == "subtle":
                speed *= self.pilot.subtle_speed
                time = part.length / speed
        elif part.terrain == "rocky":
            speed *= self.rocky_speed
            if part.complexity == "normal":
                speed *= self.pilot.normal_speed
                time = part.length / speed
            elif part.complexity == "rapid":
                speed *= self.pilot.rapid_speed
                time = part.length / speed
            elif part.complexity == "subtle":
                speed *= self.pilot.subtle_speed
                time = part.length / speed
        return time




    def time_for_track(self, track, pilote):
        """ fonction time for track """

        time = 0
        for part in track.parts:
            time = time + self.time_for_part(part, pilote)
        return time


def main():
    """ fonction main """

    ####### Génération d'une piste de 20 troncons
    print("#### Génération d'une piste de 20 troncons #### \n")

    mes_troncons = Track()
    piste = mes_troncons.parts
    for pis in piste:
        print(pis.complexity, ",", pis.terrain, "(", pis.length, ")")
    print("\n")
    ###### Génération 5 voitures avec pilotes
    print("#### Génération 5 voitures avec pilotes ####\n")
    list_car = []

    for _ in range(0, 5):
        car = Car()
        list_car.append(car)
        print("Car", car.name, "with Pilot", car.pilot.name)
    print("\n")
    print("#### Affichage du temps ####\n")
    times = []

    for car in list_car:
        time1 = car.time_for_track(mes_troncons, car.pilot)
        times.append([time1, (car.name, car.pilot.name)])
    #print (times)
    for time in times:
        print("["+str(time[0]), "Car", time[1][0], "with Pilot", time[1][1]+"]")

    print("\n")
    print("#### Affichage du vainqueur  ####\n")

    small_time = times[0][0]
    index = times[0]
    for time in times:
        if time[0] < small_time:
            small_time = time[0]
            index = time
    print("the winner is Car :", index[1][0], "with Pilot", index[1][1], "with time :", index[0])
main()
