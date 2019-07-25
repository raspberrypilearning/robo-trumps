#!/bin/python3

from turtle import *
from random import choice

hintergrund = Screen()
hintergrund.bgcolor('white')
penup()
hideturtle()
roboter = {}

datei = open('cards.txt', 'r')

for zeile in datei.read().splitlines():
  name, batterie, intelligenz, nuetzlichkeit, geschwindigkeit, bild, farbe = line.split(', ')
  roboter[name] = [batterie, intelligenz, nuetzlichkeit, geschwindigkeit, bild, farbe]
  hintergrund.register_shape(bild)
datei.close()

print('Roboter: ', ', '.join(roboter.keys()), '(oder Zufall)')

while True:
  robot = input('Wähle einen Roboter: ')
  if robot == "Zufall":
    robot = choice(list(roboter.keys()))
    print(robot)
  
  if robot in roboter:
    daten = roboter[robot]
    stil = ('Arial', 14, 'bold')
    clear()
    color(daten[5])
    goto(0, 100)
    shape(daten[4])
    setheading(90)
    stamp()
    setheading(-90)
    forward(60)
    write('Name: '+ robot, font=stil, align='center')
    forward(25)
    write('Batterie: ' + daten[0], font=stil, align='center')
    forward(25)
    write('Intelligenz: ' + daten[1], font=stil, align='center')
    forward(25)
    write('Nützlichkeit: ' + daten[2], font=stil, align='center')
    forward(25)
    write('Geschwindigkeit: ' + daten[3], font=stil, align='center')
    
  else:
    print('Dieser Roboter existiert nicht!')
