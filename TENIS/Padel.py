import turtle


# make the windows
wn= turtle.Screen()
wn.title("Tenis and Padel")
wn.bgcolor("black")	#color fondo
wn.setup(width=800, height=600)	#tamaño pantalla	
wn.tracer(0)


marcadorA = 0
marcadorB = 0



#Players
kingfisher = turtle.Turtle()
kingfisher.speed(0)
kingfisher.shape("square")
kingfisher.color("blue")
kingfisher.penup()	#por defecto el cuadrado se crea en el centro, entonces al poner el goto de abajo quedaría una linea, este comando borra esa linea
kingfisher.goto(-350,0)	#le doy coordenadas al cuadrado
kingfisher.shapesize(stretch_wid=5, stretch_len=1) #nuestro cuadrado tiene 20 pixeles, aqui multiplicamos ese tamaño por cinco y por uno, de esta forma sale esa pala alargada
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()	#por defecto el cuadrado se crea en el centro, entonces al poner el goto de abajo quedaría una linea, este comando borra esa linea
ball.goto(0,0)	#le doy coordenadas al cuadrado
ball.dx = 1 # hará que la ball se mueva cada 3 pixeles
ball.dy = 1



#ball
europeanRobin = turtle.Turtle()
europeanRobin.speed(0)
europeanRobin.shape("square")
europeanRobin.color("red")
europeanRobin.penup()	#por defecto el cuadrado se crea en el centro, entonces al poner el goto de abajo quedaría una linea, este comando borra esa linea
europeanRobin.goto(350,0)	#le doy coordenadas al cuadrado
europeanRobin.shapesize(stretch_wid=5, stretch_len=1) #nuestro cuadrado tiene 20 pixeles, aqui multiplicamos ese tamaño por cinco y por uno, de esta forma sale esa pala alargada








#linea division central
division = turtle.Turtle()
division.color("white")
division.pensize(5)
division.goto(0,400)
division.goto(0,-400)

#linea division2
division2 = turtle.Turtle()
division2.color("red")
#division2.goto(0,600)
division2.goto(300,0)
division2.goto(300,400)
division2.goto(300,-400)

#linea division3
division3 = turtle.Turtle()
division3.color("blue")
division3.goto(-300,0)
division3.goto(-300,400)
division3.goto(-300,-400)


# generate counter
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #para que no salga la imagen
pen.goto(0,260)
pen.write("Kingfisher: 0		European Robin: 0", align ="center", font=("Comic Sans MS", 15, "normal"))



# move
def kingfisher_up():
	y= kingfisher.ycor()
	y += 20
	kingfisher.sety(y)

def kingfisher_down():
	y= kingfisher.ycor()
	y -= 20
	kingfisher.sety(y)

def europeanRobin_up():
	y= europeanRobin.ycor()
	y += 20
	europeanRobin.sety(y)

def europeanRobin_down():
	y= europeanRobin.ycor()
	y -= 20
	europeanRobin.sety(y)

wn.listen()
wn.onkeypress(kingfisher_up, "w")
wn.onkeypress(kingfisher_down, "s")
wn.onkeypress(europeanRobin_up, "p")
wn.onkeypress(europeanRobin_down, "l")









# THE GAME WHILE
while True:
	wn.update()

	#start to move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)



	# bordes
	if ball.ycor()>290:	#si la coordenada es mayor que 290, haré que la direccion se invierta
		ball.dy *= -1
	if ball.ycor()< -290:	#son 290 porque mi pantalla es de 600 pero la propia ball tiene 20px y si pongo más se perdería dentro y no veríamos el rebote
		ball.dy *= -1

	#bordes derecha/izquierda
	if ball.xcor() > 390:		#si la ball llega a los 390 que es el fondo, haré que la ball vuelva al principio, a la coordenada 0,0
		ball.goto(0,0)
		ball.dx *= -1
		marcadorA += 1	# para que aumente los puntos
		pen.clear()	#limpiará el programa para que no se sobreescriba el texto
		pen.write("Kingfisher: {}		European Robin: {}".format(marcadorA,marcadorB), align ="center", font=("Comic Sans MS", 15, "normal"))

	#bordes derecha/izquierda
	if ball.xcor() < -390:		#si la ball llega a los 390 que es el fondo, haré que la ball vuelva al principio, a la coordenada 0,0
		ball.goto(0,0)
		ball.dx *= -1
		marcadorB += 1	# para que aumente los puntos
		pen.clear()
		pen.write("Kingfisher: {}		European Robin: {}".format(marcadorA,marcadorB), align ="center", font=("Comic Sans MS", 15, "normal"))


	#cuando la ball toque la pala derecha
	if ((ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < europeanRobin.ycor() + 50 and ball.ycor() > europeanRobin.ycor() -50)):
		ball.dx *= -1


	#cuando la ball toque la pala izquierda
	if ((ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < kingfisher.ycor() + 50 and ball.ycor() > kingfisher.ycor() -50)):
		ball.dx *= -1
