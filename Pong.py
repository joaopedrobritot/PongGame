# @Developed by
# João Pedro Brito Tomé
# github: https://github.com/joaopedrobritot/PongGame

import turtle
import time

jn = turtle.Screen()
jn.title("Pong by João Pedro Brito Tomé")
jn.bgcolor("black")
jn.setup(width=1000, height=600)
jn.tracer(5)

# Pontuação
pont_a = 0
pont_b = 0

####################################################

# Player 1
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("blue")
player_1.shapesize(stretch_wid=5,stretch_len=1)
player_1.penup()
player_1.goto(-450, 0)

####################################################

# Player 2
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("red")
player_2.shapesize(stretch_wid=5,stretch_len=1)
player_2.penup()
player_2.goto(450, 0)

####################################################

# Bola
veloc_bola = 0.3
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = veloc_bola
bola.dy = veloc_bola

####################################################

# Ajuste de velocidade da bola

def resetVelocBola():
    if bola.dx < 0:
        bola.dx = -veloc_bola
    if bola.dx >= 0:
        bola.dx = veloc_bola

    if bola.dy < 0:
        bola.dy = -veloc_bola
    if bola.dy >= 0:
        bola.dy = veloc_bola

def v_bolaUp():
    if bola.dx < 0:
        bola.dx -= 0.15
    if bola.dx >= 0:
        bola.dx += 0.15

    if bola.dy < 0:
        bola.dy -= 0.12
    if bola.dy >= 0:
        bola.dy += 0.12

def v_bolaDown():
    if abs(bola.dx) <= 0.15001:
        return
    if bola.dx < 0:
        bola.dx += 0.15
    if bola.dx >= 0:
        bola.dx -= 0.15

    if bola.dy < 0:
        bola.dy += 0.12
    if bola.dy >= 0:
        bola.dy -= 0.12

jn.onkeypress(v_bolaUp, "d")
jn.onkeypress(v_bolaDown, "a")

####################################################

# Placar
placar1 = turtle.Turtle()
placar1.speed(0)
placar1.color("blue")
placar1.penup()
placar1.hideturtle()
placar1.goto(-200, 260)
placar1.write("Player 1: 0", align="center", font=("Courier", 24, "bold"))

placar2 = turtle.Turtle()
placar2.speed(0)
placar2.color("red")
placar2.penup()
placar2.hideturtle()
placar2.goto(200, 260)
placar2.write("Player 2: 0", align="center", font=("Courier", 24, "bold"))

####################################################

# Logo
pong = turtle.Turtle()
pong.speed(0)
pong.color(.5, .5, .5)
pong.penup()
pong.hideturtle()
pong.goto(0, 0)
pong.write("PONG", align="center", font=("Courier New", 35, "bold"))
pong.goto(0, -38)
pong.write("Controles:", align="center", font=("Courier New", 15, "normal"))
pong.goto(20, -150)
pong.write(" W/S -> Controla player 1\n Setas Up/Down -> Controla player 2\n A/D -> Ajusta velocidade da bola\n Esc -> Fecha o jogo", align="center", font=("Courier New", 15, "normal"))
pong.goto(-340, -280)
pong.write("github: joaopedrobritot", align="center", font=("Courier New", 15, "normal"))

####################################################

# Movimentação de Players
def player_1_up():
    y = player_1.ycor()
    y += 20
    if y < 280:
        player_1.sety(y)

def player_1_down():
    y = player_1.ycor()
    y -= 20
    if y > -280:
        player_1.sety(y)

def player_2_up():
    y = player_2.ycor()
    y += 20
    if y < 280:
        player_2.sety(y)

def player_2_down():
    y = player_2.ycor()
    y -= 20
    if y > -280:
        player_2.sety(y)

jn.listen()
jn.onkeypress(player_1_up, "w")
jn.onkeypress(player_1_down, "s")
jn.onkeypress(player_2_up, "Up")
jn.onkeypress(player_2_down, "Down")
jn.onkeypress(jn.bye, "Escape")

####################################################

# Ajuste de fluidez entre frames do jogo
start_time = time.time()
segPframe = 0.000001

# Loop que atualiza a janela do jogo
while True:
    current_time = time.time()
    elapsed_time = abs(current_time - start_time)

    if elapsed_time > segPframe:
        jn.update()
        #print("Velocidade: ", abs(bola.dx))

        # Mover a bola
        bola.setx(bola.xcor() + bola.dx)
        bola.sety(bola.ycor() + bola.dy)

        # Checando extremos da janela do jogo

        # Colisões Cima e Baixo
        if bola.ycor() > 290:
            bola.sety(290)
            bola.dy *= -1
        
        elif bola.ycor() < -290:
            bola.sety(-290)
            bola.dy *= -1

        # Colisões Esquerda e Direita
        if bola.xcor() > 440:
            pont_a += 1
            placar1.clear()
            placar1.write("Player 1: {}".format(pont_a), align="center", font=("Courier", 24, "bold"))
            resetVelocBola()
            bola.goto(0, 290)
            bola.dx *= -1

        elif bola.xcor() < -440:
            pont_b += 1
            placar2.clear()
            placar2.write("Player 2: {}".format(pont_b), align="center", font=("Courier", 24, "bold"))
            resetVelocBola()
            bola.goto(0, 290)
            bola.dx *= -1

        # Colisões entre Player e Bola
        if bola.xcor() <= -430 and bola.ycor() <= player_1.ycor() + 50 and bola.ycor() >= player_1.ycor() - 50:
            bola.dx *= -1
        
        elif bola.xcor() >= 430 and bola.ycor() <= player_2.ycor() + 50 and bola.ycor() >= player_2.ycor() - 50:
            bola.dx *= -1
        
        elapsed_time = 0
        start_time = time.time()

####################################################    
