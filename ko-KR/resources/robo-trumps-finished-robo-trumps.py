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

print('로봇: ', ', '.join(robots.keys()), ' (or random)')

while True:
  robot = input("로봇을 선택하세요: ")
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
    write('이름: ' + robot, font=style, align='center')
    forward(25)
    write('배터리: ' + stats[0], font=style, align='center')
    forward(25)
    write('지능도: ' + stats[1], font=style, align='center')
    forward(25)
    write('사용가치: ' + stats[2], font=style, align='center')
    forward(25)
    write('속도: ' + stats[3], font=style, align='center')
    
  else:
    print("로봇이 존재하지 않습니다!")
