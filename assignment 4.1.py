import turtle
import random

# Function to control the tortoise's movements
def tortoise_move(position):
    num = random.randint(1, 10)
    if 1 <= num <= 5:
        position += 3  # Fast Plod
    elif 6 <= num <= 7:
        position -= 5  # Slip
    else:
        position += 1  # Slow Plod

    # Check boundaries
    if position < -100:
        position = -100
    elif position > 100:
        position = 100

    return position

# Function to control the hare's movements
def hare_move(position):
    num = random.randint(1, 10)
    if num <= 2:
        pass  # Sleep
    elif 3 <= num <= 4:
        position += 7  # Big Hop
    elif num == 5:
        position -= 10  # Big Slip
    else:
        position += 1  # Small Hop

    # Check boundaries
    if position < -100:
        position = -100
    elif position > 100:
        position = 100

    return position

# Set up the race track
window = turtle.Screen()
window.title("Tortoise and Hare Race")
window.bgcolor("white")




text_display = turtle.Turtle()
text_display.penup()
text_display.hideturtle()
text_display.setpos(0, 100)
text_display.write("ON YOUR MARK... GET SET GO... GO!!!!!!\n AND THEY'RE OFF!", align="center", font=("Arial", 12, "normal"))



# Create turtles for the tortoise and hare
tortoise = turtle.Turtle()
hare = turtle.Turtle()

# Set turtle shapes
tortoise.shape("turtle")
tortoise.shapesize(2, 2, 1)
hare.shape("classic")
hare.shapesize(2, 2, 1)

# Initialize positions
tortoise_pos = -100
hare_pos = -100



# Draw the start lines
tortoise.penup()
tortoise.setpos(-100, 0)
tortoise.pendown()
tortoise.setpos(-100, 50)

hare.penup()
hare.setpos(-100, 0)
hare.pendown()
hare.setpos(-100, 50)

# Draw the finish lines
tortoise.penup()
tortoise.setpos(100, 0)
tortoise.pendown()
tortoise.setpos(100, 50)

hare.penup()
hare.setpos(100, 0)
hare.pendown()
hare.setpos(100, 50)

# Create a time display
time_display = turtle.Turtle()
time_display.penup()
time_display.hideturtle()
time_display.setpos(0, -80)
time_display.write("Time: 0 seconds", align="center", font=("Arial", 12, "normal"))

# Main race loop
clock = 0
while tortoise_pos < 100 and hare_pos < 100:
    tortoise_pos = tortoise_move(tortoise_pos)
    hare_pos = hare_move(hare_pos)
    
    # Update turtle positions
    tortoise.penup()
    tortoise.setpos(tortoise_pos, 0)
    tortoise.pendown()
    
    hare.penup()
    hare.setpos(hare_pos, 50)
    hare.pendown()
    
    clock += 1
    time_display.clear()
    

# Determine the winner
if tortoise_pos >= 100 and hare_pos >= 100:
    winner = "It's a tie!"
else:
    winner = "Tortoise" if tortoise_pos >= 100 else "Hare"


turtle.penup()
turtle.setpos(200, 0)
turtle.hideturtle()

turtle.write(f"{winner} wins !", align="center", font=("Arial", 16, "bold"))

# Display the winner
turtle.penup()
turtle.setpos(0, -120)
turtle.hideturtle()

turtle.write(f"'Time' of race: {clock} 'seconds'", align="center", font=("Arial", 16, "bold"))

# Close the turtle graphics window when clicked
window.exitonclick()
