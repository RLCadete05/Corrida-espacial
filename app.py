from turtle import *
from random import *
import turtle
import random

print('>>>>> Bem vindo a corrida espacial das Tartarugas Ninjas!<<<<< ')

print('Escolha sua tartaruga e em seguida informe o valor de sua aposta.')
print('  [ 1 ] - Leonardo (azul)\n  [ 2 ] - Raphael (vermelho)\n  [ 3 ] - Donatello (roxo)\n  [ 4 ] - Michelangelo (laranja) ')
escolha = int(input('Tartaruga: '))
aposta = float(input('Aposta R$: '))

while escolha > 4:
	if escolha == 1:
		1 > CHEGADA
		print("Leonardo ganhou a corrida!")
	else:		
		print("Leonardo perdeu!\nVocê perdeu sua aposta.")



tela = turtle.Screen()
tela.bgcolor('black')

penup()
speed(0)
goto(300,180)
for CHEGADA in range(2):
	write(CHEGADA, align='CHEGADA')
	color("pink")
	pensize(2)
	right(90)
	fd(12)
	pendown()
	fd(200)
	penup()
	back(210)
	left(90)
	fd(30)
	

#tartaruga em lugar aleatória
def moveToRandomLocation():
    penup()
    setpos( randint(-400,400) , randint(-400,400) )
    pendown()


#estrela de tamanho específico
def drawStar(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starSize)
    end_fill()
    penup()

#galáxia de estrelas
def drawGalaxy(numberOfStars):
    starColours = ["#058396","#0275A6","#827E01"]
    moveToRandomLocation()
    #pequenas estrelas coloridas
    for star in range(numberOfStars):
        penup()
        left( randint(-180,180) )
        forward( randint(5,20) )
        pendown()       
        #estrela de cor aleatória
        drawStar( 2, choice(starColours) )

#constelação de estrelas
def drawConstellation(numberOfStars):
    moveToRandomLocation()
    for star in range(numberOfStars-1):
        drawStar( randint(7,15) , "white")
        pendown()
        left( randint(-90,90) )
        forward( randint(30,70) )
    #última estrela
    drawStar( randint(7,15) , "White")

speed(0)

#30 estrelas brancas (tamanhos/posições aleatórias)
for star in range(30):
    moveToRandomLocation()
    drawStar( randint(5,25) , "White")
		
'''def drawPlanet:
    color(pink)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(PlanetSize)
    end_fill()
    penup()
'''

#3 pequenas galáxias de 30 estrelas
for galaxy in range(3):
    drawGalaxy(30)
		

#2 constelações com números aleatórios de estrelas
for constellation in range(2):
    drawConstellation(randint(6,9))

speed(0)

pendown()
leonardo = Turtle('Leonardo')
leonardo.color('blue')
leonardo.shape('turtle')
leonardo.pensize(5)

leonardo.penup()
#leonardo.drawStar(10, 'white')
leonardo.goto(-160,10)
leonardo.pendown()

raphael = Turtle('Raphael')
raphael.color('red')
raphael.shape('turtle')
raphael.pensize(5)

raphael.penup()
#raphael.drawStar(10, 'white')
raphael.goto(-160,50)
raphael.pendown()

donatello = Turtle('Donatello ')
donatello.color('purple')
donatello.shape('turtle')
donatello.pensize(5)

donatello.penup()
donatello.goto(-160,90)
donatello.pendown()

michelangelo = Turtle('Michelangelo ')
michelangelo.color('OrangeRed')
michelangelo.shape('turtle')
michelangelo.pensize(5)

michelangelo.penup()
michelangelo.goto(-160,130)
michelangelo.pendown()

for corre in range(50):
	leonardo.forward(random.randint(1,18))
	raphael.forward(random.randint(1,18))
	donatello.forward(random.randint(1,18))
	michelangelo.forward(random.randint(1,18))

#hideturtle()
#done()
