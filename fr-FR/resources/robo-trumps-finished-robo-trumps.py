#!/bin/python3

from turtle import *
from random import choice

ecran = Screen()
ecran.bgcolor('white')
penup()
cachertortue()
robots = {}

fichier = open('cartes.txt', 'r')

for line in fichier.read().splitlines():
  nom, batterie, intelligence, utilité, vitesse, image, couleur = line.split(', ')
  robots[nom] = [batterie, intelligence, utilité, vitesse, image, couleur]
  ecran.register_shape(image)
fichier.close()

print('Robots: ', ', '.join(robots.keys()), ' (or random)')

while True:
  robot = input("Choisir un robot : ")
  if(robot == "random"):
    robot = choice(robots.keys())
    print(robot)
  
  if robot in robots:
    stats = robots[robot]
    style = ('Courier', 14, 'bold')
    clear()
    color(stats[5])
    goto(0, 100)
    shape(stats[4])
    setheading(90)
    stamp()
    setheading(-90)
    forward(60)
    write('Nom: ' + robot, font=style, align='center')
    forward(25)
    write('Batterie : ' + stats[0], font=style, align='center')
    forward(25)
    write('Intelligence: ' + stats[1], font=style, align='center')
    forward(25)
    write('Utilité : ' + stats[2], font=style, align='center')
    forward(25)
    write('Vitesse : ' + stats[3], font=style, align='center')
    
  else:
    print("Le robot n'existe pas!")
