#!/bin/python3

from turtle import *
from random import choice

ekran = Screen()
screen.bgcolor('white')
penup()
hideturtle()
roboty = {}

plik = open('cards.txt', 'r')

for linia in plik.read().splitlines():
  imie, bateria, inteligencja, użyteczność, prędkość, obraz, kolor = linia.split(', ')
  roboty[imie] = [bateria, inteligencja, użyteczność, prędkość, obraz, kolor]
  ekran.register_shape(obraz)
plik.close()

print('Roboty: ', ', '.join(roboty.keys()), ' (or random)')

while True:
  robot = input("Wybierz robota: ")
  if(robot == "random"):
    robot = choice(roboty.keys())
    print(robot)
  
  if robot in roboty:
    statystyki = roboty[robot]
    styl = ('Courier', 14, 'bold')
    clear()
    color(statystyki[5])
    goto(0, 100)
    shape(statystyki[4])
    setheading(90)
    stamp()
    setheading(-90)
    forward(60)
    write('Imie: ' + robot, font=style, align='center')
    forward(25)
    write('Bateria: ' + statystyki[0], font=style, align='center')
    forward(25)
    write('Inteligencja: ' + statystyki[1], font=style, align='center')
    forward(25)
    write('Użyteczność: ' + statystyki[2], font=style, align='center')
    forward(25)
    write('Prędkość: ' + statystyki[3], font=style, align='center')
    
  else:
    print("Robot nie istnieje!")
