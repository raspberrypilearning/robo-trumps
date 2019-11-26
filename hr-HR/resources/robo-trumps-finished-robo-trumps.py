#!/bin/python3

from turtle import *
from random import choice

ekran = Screen()
ekran.bgcolor('white')
penup()
hideturtle()
roboti = {}

datoteka = open('cards.txt', 'r')

for linija in datoteka.read().splitlines():
  ime, baterija, inteligencija, korisnost, brzina, slika, boja = linija.split(', ')
  roboti[ime] = [baterija, inteligencija, korisnost, brzina, slika, boja]
  ekran.register_shape(slika)
datoteka.close()

print('Roboti: ', ', '.join(roboti.keys()), ' (or random)')

while True:
  robot = input("Odaberi robota: ")
  if(robot == "random"):
    robot = choice(roboti.keys())
    print(robot)
  
  if robot in roboti:
    karak = roboti[robot]
    stil = ('Courier', 14, 'bold')
    clear()
    color(karak[5])
    goto(0, 100)
    shape(karak[4])
    setheading(90)
    stamp()
    setheading(-90)
    forward(60)
    write('Ime: ' + robot, font=stil, align='center')
    forward(25)
    write('Baterija: ' + karak[0], font=stil, align='center')
    forward(25)
    write('Inteligencija: ' + karak[1], font=stil, align='center')
    forward(25)
    write('Korisnost: ' + karak[2], font=stil, align='center')
    forward(25)
    write('Brzina: ' + karak[3], font=stil, align='center')
    
  else:
    print("Robot ne postoji!")
