import turtle

turtle.setup(500,1200,1410,0)
turtle.speed(5)

slutt = "1"

vinkel = 60
storrelse = 80

for i in range(6):
    turtle.forward(storrelse)
    turtle.right(vinkel)

slutt = input("Press Enter to clear graphic, or 'close' to close it: \n")
if slutt == "":
    turtle.clear()
    turtle.reset()
elif slutt == "close":
    turtle.bye()