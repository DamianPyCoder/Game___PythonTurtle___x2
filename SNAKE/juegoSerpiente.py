import turtle
import time 
import random


speed=0.1
points=0
record=0

#configure the windows
windows= turtle.Screen()
windows.title("Snake Eyes")
windows.bgcolor("black")
windows.setup(width=600, height=600)
windows.tracer(0)

#make the head
head=turtle.Turtle()
head.color("purple")
head.speed(0)
head.shape("circle")
head.penup()
head.goto(0,0) #para que la serpiente comience desde el centro, en el modo turtle el 0,0 no es en la esquina sino en el centro
head.direccion = "stop"

#food
food=turtle.Turtle()
food.color("cyan")
food.speed(0)
food.shape("turtle")
food.penup()
food.goto(0,100)

#body
#this list make grow the snake when eat
body=[]

#txt
txt = turtle.Turtle()
txt.speed(0)
txt.color("cyan")
txt.penup()
txt.hideturtle()
txt.goto(0,260)
txt.write("Puntuacion: 0    Record: ", align="center", font=("Courier",24,"normal") )



#functions change direction, functions keyboard, functions action moves
def goUp():
	head.direccion="up"
def goDown():
	head.direccion="down"
def turnLeft():
	head.direccion="left"
def turnRight():
	head.direccion="right"

windows.listen() #le digo a la windows que esté atenta a los eventos del teclado
windows.onkeypress(goUp, "Up")
windows.onkeypress(goDown, "Down")
windows.onkeypress(turnRight, "Right")
windows.onkeypress(turnLeft, "Left")

def actionMove():
	if head.direccion == "up":
		y = head.ycor()
		head.sety(y+20)
	if head.direccion == "down":
		y = head.ycor()
		head.sety(y-20)
	if head.direccion == "right":
		x = head.xcor()
		head.setx(x+20)
	if head.direccion == "left":
		x = head.xcor()
		head.setx(x-20)



#windows game
while True:
	windows.update()

	turtle.goto(-300,-300)
	turtle.forward(600)
	turtle.color("blue violet")
	turtle.left(90)
	turtle.color("blue violet")
	turtle.forward(600)
	turtle.color("blue violet")
	turtle.left(90)
	turtle.color("blue violet")
	turtle.forward(600)
	turtle.color("blue violet")
	turtle.left(90)
	turtle.color("blue violet")
	turtle.forward(600)
	turtle.color("blue violet")
	turtle.left(90)
	turtle.color("blue violet")
	turtle.hideturtle()


	# colissions border square
	if head.xcor() > 280 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
		time.sleep(1) #dar pausa al juego 
		head.goto(0,0)
		head.direction="stop"

		#hide the body
		for totalbody in body:
			totalbody.goto(1000,1000)

		#clean the body
		body.clear()

		#reset points
		points=0
		txt.clear()
		txt.write("Puntuacion: {}    Record: {}".format(points,record), align="center", font=("Courier",24,"normal") )



	# colissions food
	if head.distance(food) < 20: #el 20 es porque el tamaño de los pixeles del cuadrado, circulo... en el caso de que sea menor es porque se ha tocado y quiero que se transporte a otro sitio
		x=random.randint(-280,280)
		y=random.randint(-280,280)
		food.goto(x,y)


		bodyCrece=turtle.Turtle()
		bodyCrece.color("medium purple")
		bodyCrece.speed(0)
		bodyCrece.shape("circle")
		bodyCrece.penup()
		body.append(bodyCrece)

		#add points
		points += 10

		if points > record:
			record=points

		txt.clear()
		txt.write("Puntuacion: {}    Record: {}".format(points,record), align="center", font=("Courier",24,"normal") )

	#move the snake body 
	totalbody = len(body)
	for index in range(totalbody -1, 0, -1):
		x=body[index -1].xcor()
		y=body[index -1].ycor()
		body[index].goto(x,y)

	#move first body element in the snake
	if totalbody > 0:
		x=head.xcor()
		y=head.ycor()	
		body[0].goto(x,y)



	actionMove()

	#colissions with ourself
	for totalbody in body:
		if totalbody.distance(head) <20:
			time.sleep(1)
			head.goto(0,0)
			head.direction="stop"

			#hide body
			for totalbody in body:
				totalbody.goto(1000,1000)

			#Clean body
			body.clear()

			#reset points
			points=0
			txt.clear()
			txt.write("Puntuacion: {}    Record: {}".format(points,record), align="center", font=("Courier",24,"normal") )



	time.sleep(speed)
