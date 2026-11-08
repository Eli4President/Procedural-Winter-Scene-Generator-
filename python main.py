import turtle

# 2. Give the drawing window a clear title
screen = turtle.Screen()
turtle.title("Function Based Geometric Art")


def drawPolygon(sides: int, position: tuple[float, float], side_length: float, color: str, fill_color: str):
#YOUR CODE HERE to calculate the 'angle' variable using 'sides'
    angle = 180-(sides-2)*180/sides

    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    my_turtle.penup()
    my_turtle.goto(position[0], position[1])
    my_turtle.pendown()
    #my_turtle.teleport(position[0], position[1])
    my_turtle.color(color)
    my_turtle.color(color, color)
    my_turtle.begin_fill() 

    for _ in range(6):
        my_turtle.forward(side_length)
        my_turtle.left(angle)

    my_turtle.end_fill()


def drawTriangle(side_1: float, side_2: float, angle_1: float, angle_2: float, position: tuple[float, float], color: str, fill_color: str):
    my_turtle = turtle.Turtle()
    #angle = 180-(side_1-2)*180/sides
    my_turtle.speed(0)
    my_turtle.penup()
    my_turtle.goto(position[0], position[1])
    my_turtle.pendown()
    #my_turtle.teleport(position[0], position[1])
    my_turtle.color(color, fill_color)
    #my_turtle.color(color, color)
    my_turtle.begin_fill()

    #for _ in range(3):
    my_turtle.forward(side_1)
    my_turtle.right(180 - angle_1)
    my_turtle.forward(side_2)
    my_turtle.goto(position[0], position[1])

    my_turtle.end_fill()


drawTriangle(side_1=120, side_2=90, angle_1=90, angle_2 =53.13, position= [-250, -100], color = 'red', fill_color ='red')

drawPolygon(6,(0,0), 100, 'pink', 'pink')


def drawCircle(radius: float, color: str, position: list[float, float], semi = None):
    my_turtle = turtle.Turtle()
    my_turtle.hideturtle()
    my_turtle.speed(0)
    my_turtle.teleport(position[0], position[1])
    my_turtle.color(color)
    my_turtle.begin_fill()
    
    if semi:
        my_turtle.circle(radius, semi)
        pass 
    else: 
        my_turtle.circle(radius)
        pass
        
    my_turtle.end_fill()

x_locations = [-400, -350, -300, -250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250, 300]
y_locations = [150, 75, 0, -75, 575, -75, 0, 75, 150, 75, -75, 0, 150, -75, 550]

def createSnow(x_positions, y_positions):
    for i in range(len(x_positions)):
        drawCircle(10, "#c6e2ff", (x_positions[i], y_positions[i]))
    
createSnow(x_locations, y_locations)



def drawSemiCircle(radius: float, color: str, position: list[float, float]):
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    my_turtle.teleport(position[0], position[1])
    my_turtle.color(color)
    my_turtle.begin_fill()
    
    # 1. Draw the straight base of the semi-circle
    my_turtle.forward(radius)
    my_turtle.right(90)
    
    # 2. Draw the 180-degree curved part
    my_turtle.circle(-radius, 180) 
    
    # 3. Use setup commands to quickly close the shape (the original code uses these)
    my_turtle.right(-270)
    my_turtle.right(radius) # Note: this is a simple turn, not a forward move!
    
    my_turtle.end_fill()


def createSnowman():
#BODY
    drawCircle(150, '#f0f8ff', (0, -400))
    drawCircle(100, '#f0f8ff', (0, -150))
    drawCircle(75, '#f0f8ff', (0, 0))

#EYES
    drawCircle(8, '#000000', (-25,80))
    drawCircle(8, '#000000', (25,80))

#NOSE 
    drawSemiCircle(10, '#ffa500', (0,60))

createSnow(x_locations, y_locations)
createSnowman()



turtle.done()

screen.mainloop()
