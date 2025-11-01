##Name: Moosa Shehzad Abbasi
##UID# U37033529
## Program Description: Tortoise vs Hare


import turtle
import random


def tortoise_move(position):
    num = random.randint(1, 10)
    if 1 <= num <= 5:
        position += 3  
    elif 6 <= num <= 7:
        position -= 5  
    else:
        position += 1
        
    
    if position < -100:
        position = -100
    elif position > 100:
        position = 100

    return position

def hare_move(position):
    num = random.randint(1, 10)
    if num <= 2:
        pass  
    elif 3 <= num <= 4:
        position += 7  
    elif num == 5:
        position -= 10  
    else:
        position += 1  

    if position < -100:
        position = -100
    elif position > 100:
        position = 100

    return position


window = turtle.Screen()
window.title("Tortoise and Hare Race")
window.bgcolor("blue")




text_display = turtle.Turtle()
text_display.penup()
text_display.hideturtle()
text_display.setpos(0, 100)
text_display.write("ON YOUR MARK... GET SET GO... GO!!!!!!\n AND THEY'RE OFF!", align="center", font=("Arial", 12, "normal"))



tortoise = turtle.Turtle()
hare = turtle.Turtle()


tortoise.shape("turtle")
tortoise.shapesize(2, 2, 1)
hare.shape("classic")
hare.shapesize(2, 2, 1)


tortoise_pos = -100
hare_pos = -100


start = turtle.Turtle()
start.penup()
start.hideturtle()
start.setpos(-100, 60)
start.write("START", align="center", font=("Arial", 12, "normal"))




start = turtle.Turtle()
start.penup()
start.hideturtle()
start.setpos(100, 60)
start.write("END", align="center", font=("Arial", 12, "normal"))




tortoise.penup()
tortoise.setpos(-100, 0)
tortoise.pendown()
tortoise.setpos(-100, 50)

hare.penup()
hare.setpos(-100, 0)
hare.pendown()
hare.setpos(-100, 50)


tortoise.penup()
tortoise.setpos(100, 0)
tortoise.pendown()
tortoise.setpos(100, 50)

hare.penup()
hare.setpos(100, 0)
hare.pendown()
hare.setpos(100, 50)


time_display = turtle.Turtle()
time_display.penup()
time_display.hideturtle()
time_display.setpos(0, -80)
time_display.write("Time: 0 seconds", align="center", font=("Arial", 12, "normal"))


clock = 0
while tortoise_pos < 100 and hare_pos < 100:
    tortoise_pos = tortoise_move(tortoise_pos)
    hare_pos = hare_move(hare_pos)
    
    
    tortoise.penup()
    tortoise.setpos(tortoise_pos, 0)
    tortoise.pendown()
    
    hare.penup()
    hare.setpos(hare_pos, 50)
    hare.pendown()
    
    clock += 1
    time_display.clear()
    


if tortoise_pos >= 100 and hare_pos >= 100:
    winner = "It's a tie!"
else:
    winner = "Tortoise" if tortoise_pos >= 100 else "Hare"


turtle.penup()
turtle.setpos(200, 0)
turtle.hideturtle()

turtle.write(f"{winner} wins !", align="center", font=("Arial", 16, "bold"))


turtle.penup()
turtle.setpos(0, -120)
turtle.hideturtle()

turtle.write(f"'Time' of race: {clock} 'seconds'", align="center", font=("Arial", 16, "bold"))


window.exitonclick()
