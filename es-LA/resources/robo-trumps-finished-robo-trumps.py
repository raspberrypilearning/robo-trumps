#!/bin/python3

from turtle import *
from random import choice

pantalla = Screen()
pantalla.bgcolor('white')
penup()
hideturtle()
robots = {}

archivo = open ('cards.txt', 'r')

for linea in archivo.read().splitlines():
  nombre, bateria, inteligencia, utilidad, velocidad, imagen, colores = linea.split(', ')
  robots[nombre] = [bateria, inteligencia, utilidad, velocidad, imagen, colores]
  pantalla.register_shape(imagen)
archivo.close()

print('Robots: ', ', '.join(robots.keys()), ' (o aleatorio)')

while True:
  robot = input ("Elige un robot:")
  if(robot == "aleatorio"):
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
