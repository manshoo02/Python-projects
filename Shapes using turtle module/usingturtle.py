from turtle import Turtle, Screen
import random
ninja = Turtle()
ninja.shape("turtle")
ninja.color("pink")
ninja.pencolor("red")

colors = ['red','green','blue','firebrick','ForestGreen' ,'pink' ,'black', 'purple' ,'grey']
def draw(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        ninja.forward(100)
        ninja.right(angle)
for side in range(3,11):
    ninja.color(random.choice(colors))
    draw(side)




screen = Screen()
screen.exitonclick()