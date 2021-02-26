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

print('ロボット: ', ', '.join(robots.keys()), ' (またはランダム)')

while True:
  robot = input("ロボットを選んで下さい: ")
  if(robot == "ランダム"):
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
    write('名前: ' + robot, font=style, align='center')
    forward(25)
    write('バッテリー: ' + stats[0], font=style, align='center')
    forward(25)
    write('インテリジェンス: ' + stats[1], font=style, align='center')
    forward(25)
    write('使いやすさ: ' + stats[2], font=style, align='center')
    forward(25)
    write('スピード: ' + stats[3], font=style, align='center')
    
  else:
    print("そのロボットは存在しません!")
