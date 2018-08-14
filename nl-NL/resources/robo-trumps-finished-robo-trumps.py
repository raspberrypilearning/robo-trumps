#!/bin/python3

from turtle import *
from random import choice

scherm = Screen()
scherm.bgcolor('white')
penup()
hideturtle()
robots = {}

file = open('cards.txt', 'r')

for regel in file.read().splitlines():
  naam, batterij, intelligentie, bruikbaarheid, snelheid, afbeelding, kleur = regel.split(', ')
  robots[naam] = [batterij, intelligentie, bruikbaarheid, snelheid, afbeelding, kleur]
  scherm.register_shape(afbeelding)
file.close()

print('Robots: ', ', '.join(robots.keys()), ' (of willekeurig)')

while True:
  robot = input("Kies een robot: ")
  if(robot == "willekeurig"):
    robot = choice(robots.keys())
    print(robot)
  
  if robot in robots:
    gegevens = robots[robot]
    stijl = ('Courier', 14, 'bold')
    clear()
    color(gegevens[5])
    goto(0, 100)
    shape(gegevens[4])
    setheading(90)
    stamp()
    setheading(-90)
    forward(80)
    write('Naam: ' + robot, font=stijl, align='center')
    forward(25)
    write('Batterij: ' + gegevens[0], font=stijl, align='center')
    forward(25)
    write('Intelligentie: ' + gegevens[1], font=stijl, align='center')
    forward(25)
    write('Bruikbaarheid: ' + gegevens[2], font=stijl, align='center')
    forward(25)
    write('Snelheid: ' + gegevens[3], font=stijl, align='center')
    
  else:
    print("Robot bestaat niet!")
