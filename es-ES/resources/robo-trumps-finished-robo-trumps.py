#!/bin/python3

from turtle import *
from random import choice

screen = Screen()
screen.bgcolor('white')
penup()
hideturtle()
robots = {}

file = open ('cards.txt', 'r')

for line in file.read().splitlines():
  nombre, bateria, inteligencia, utilidad, velocidad, imagen, color_ = line.split(', ')
  robots[name] = [bateria, inteligencia, utilidad, velocidad, imagen, color_]
  screen.register_shape(Image)
file.Close()

print('Robots: ', ', '.join(robots.keys()), ' (or random)')

while True:
  robot = input ("Elige un robot:")
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
    write('Nombre: ' + robot, font=style, align='center')
    forward(25)
    write('Bateria: ' + stats[0], font=style, align='center')
    forward(25)
    write('Inteligencia: ' + stats[1], font=style, align='center')
    forward(25)
    write('Utilidad: ' + stats[2], font=style, align='center')
    forward(25)
    write('Velocidad: ' + stats[3], font=style, align='center')
    
  else:
    print("¡El robot no existe!")
