#!/bin/python3

from turtle import *
from random import choice

schermo = Screen()
schermo.bgcolor('white')
penup()
hideturtle()
robots = {}

file = open('cards.txt', 'r')

for riga in file.read().splitlines():
  nome, batteria, intelligenza, utilita, velocita, immagine, colore = riga.split(',')
  robots[nome] = [batteria, intelligenza, utilita, velocita, immagine, colore]
  schermo.register_shape(immagine)
file.close()

print('Robot: ', ', '.join(robots.keys()), ' (oppure random)')

while True:
  robot = input("Scegli un robot: ")
  if(robot == "random"):
    robot = choice(list(robots.keys()))
    print(robot)
  
  if robot in robots:
    statistiche = robots[robot]
    stile = ('Courier', 14, 'bold')
    clear()
    color(statistiche[5])
    goto(0, 100)
    shape(statistiche[4])
    setheading(90)
    stamp()
    setheading(-90)
    forward(60)
    write('Nome: ' + robot, font=stile, align='center')
    forward(25)
    write('Batteria: ' + statistiche[0], font=stile, align='center')
    forward(25)
    write('Intelligenza: ' + statistiche[1], font=stile, align='center')
    forward(25)
    write('Utilità: ' + statistiche[2], font=stile, align='center')
    forward(25)
    write('Velocita: ' + statistiche[3], font=stile, align='center')
    
  else:
    print("Questo robot non esiste!")
