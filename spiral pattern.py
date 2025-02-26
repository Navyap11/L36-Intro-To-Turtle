import turtle

pennn= turtle.Turtle()
size=0

while True:
    for i in range(4):
        pennn.forward(size+1)
        pennn.left(90)
        size= size-5
    size= size+1