
import turtle
def draw_square(some_turtle):
	for j in range(1,30):

		for i  in range(1,5):
			some_turtle.forward(100)
			some_turtle.right(90)
		some_turtle.right(10)
	some_turtle.right(90)
	some_turtle.forward(360)
def draw_shapes():
	window=turtle.Screen()
	window.bgcolor("red")

	#Creat some squares
	square= turtle.Turtle()
	square.shape("arrow")
	square.color("green")
	square.speed(2)
	draw_square(square)
	#for i in range (1,30):
	#	draw_square(square)
	#	square.right(10)
	#square.left(90)
	#square.setposition(0,-200)
	#square.backward(350)

	#Create some circles
	#circles=turtle.Turtle()
	#circles.shape("arrow")
	#circles.color("yellow")
	#circles.circle(50)

	window.exitonclick()
draw_shapes()
#draw_square()