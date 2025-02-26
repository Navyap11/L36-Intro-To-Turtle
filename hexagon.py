import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(500,600)
hexagon= turtle.Turtle()

numofsides=6
sidelength=60
angle=360.0/numofsides

for i in range(numofsides):
    hexagon.forward(sidelength)
    hexagon.right(angle)

turtle.done()