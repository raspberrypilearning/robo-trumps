#!/bin/python3

from turtle import *
from random import choice

screen = Screen()
screen.bgcolor('white')
penup()
hideturtle()
robots = {}

file = open('cards.txt', 'r')

for line in file.read().splitlines():
  name, battery, intelligence, usefulness, speed, image, colour = line.split(', ')
  robots[name] = [battery, intelligence, usefulness, speed, image, colour]
  screen.register_shape(image)
file.close()

print('Ρομπότ: ', ', '.join(robots.keys()), ' (ή random)')

while True:
  robot = input("Επίλεξε ένα ρομπότ: ")
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
    write('Όνομα: ' + robot, font=style, align='center')
    forward(25)
    write('Μπαταρία: ' + stats[0], font=style, align='center')
    forward(25)
    write('Εξυπνάδα: ' + stats[1], font=style, align='center')
    forward(25)
    write('Χρησιμότητα: ' + stats[2], font=style, align='center')
    forward(25)
    write('Ταχύτητα: ' + stats[3], font=style, align='center')
    
  else:
    print("Το ρομπότ δεν υπάρχει!")
