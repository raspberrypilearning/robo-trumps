#!/bin/python3

from turtle import *
from random import choice

tela = Screen()
tela.bgcolor('white')
penup()
hideturtle()
robos = {}

arquivo = open('cartas.txt', 'r')

for linha in arquivo.read().splitlines():
  nome, bateria, inteligencia, utilidade, velocidade, imagem, cor = linha.split(', ')
  robos[nome] = [bateria, inteligencia, utilidade, velocidade, imagem, cor]
  tela.register_shape(imagem)
arquivo.close()

print('Robôs: ', ', '.join(robos.keys()), ' (ou sortear)')

while True:
  robo = input("Escolha um robô: ")
  if(robo == "sortear"):
    robo = choice(list(robos.keys()))
    print(robo)
  
  if robo in robos:
    informacoes = robos[robo]
    style = ('Courier', 14, 'bold')
    clear()
    color(informacoes[5])
    goto(0, 100)
    shape(informacoes[4])
    setheading(90)
    stamp()
    setheading(-90)
    forward(60)
    write('Nome: ' + robo, font=fonte, align='center')
    forward(25)
    write('Bateria: ' + informacoes[0], font=fonte, align='center')
    forward(25)
    write('Inteligência: ' + informacoes[1], font=fonte, align='center')
    forward(25)
    write('Utilidade: ' + informacoes[2], font=fonte, align='center')
    forward(25)
    write('Velocidade: ' + informacoes[3], font=fonte, align='center')
    
  else:
    print("Este robô não existe!")
