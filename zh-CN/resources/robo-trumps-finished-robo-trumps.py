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

print('机器人： ', ', '.join(robots.keys()), ' (or random)')

while True:
  robot = input("选择一个机器人: ")
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
    write('名称： ' + robot, font=style, align='center')
    forward(25)
    write('续航时间： ' + stats[0], font=style, align='center')
    forward(25)
    write('智能等级： ' + stats[1], font=style, align='center')
    forward(25)
    write('有用性： ' + stats[2], font=style, align='center')
    forward(25)
    write('速度： ' + stats[3], font=style, align='center')
    
  else:
    print("此机器人不存在！")
