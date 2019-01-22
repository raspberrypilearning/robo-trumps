#!/bin/python3

from turtle import *
from random import choice

ekran = Screen()
ekran.bgcolor('white')
penup()
hideturtle()
roboti = {}

datoteka = open('cards.txt', 'r')

for red in datoteka.read().splitlines():
  ime, baterija, inteligencija, korisnost, brzina, slika, boja = red.split(', ')
  roboti[ime] = [baterija, inteligencija, korisnost, brzina, slika, boja]
  ekran.register_shape(slika)
datoteka.close()

print('Roboti: ', ', '.join(roboti.keys()), ' (ili nasumičan)')

while True:
  robot = input("Odaberi robota: ")
  if(robot == "nasumičan"):
    robot = choice(roboti.keys())
    print(robot)
  
  if robot in roboti:
    podaci = roboti[robot]
    stil = ('Courier', 14, 'bold')
    clear()
    color(podaci[5])
    goto(0, 100)
    shape(podaci[4])
    setheading(90)
    stamp()
    setheading(-90)
    forward(60)
    write('Ime: ' + robot, font=stil, align='center')
    forward(25)
    write('Baterija: ' + podaci[0], font=stil, align='center')
    forward(25)
    write('Inteligencija: ' + podaci[1], font=stil, align='center')
    forward(25)
    write('Korisnost: ' + podaci[2], font=stil, align='center')
    forward(25)
    write('Brzina: ' + podaci[3], font=stil, align='center')
    
  else:
    print("Robot ne postoji!")
