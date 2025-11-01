import turtle
import random

# Create a turtle screen
screen = turtle.Screen()
screen.title("Tortoise vs. Hare")
screen.bgcolor("white")

# Create the tortoise and hare turtle objects
tortoise = turtle.Turtle()
hare = turtle.Turtle()

# Set the initial positions of the tortoise and hare
tortoise.penup()
tortoise.shape("turtle")
tortoise.color("green")
tortoise.setpos(-100, 0)

hare.penup()
hare.shape("turtle")
hare.color("brown")
hare.setpos(-100, 50)

# Function to move the tortoise
def move_tortoise():
    num = random.randint(1, 10)
    if 1 <= num <= 5:
        tortoise.forward(3)  # Fast Plod
    elif 6 <= num <= 7:
        tortoise.backward(5)  # Slip
    else:
        tortoise.forward(1)  # Slow Plod

    # Ensure the tortoise stays within the race boundaries
    if tortoise.xcor() < -100:
        tortoise.setx(-100)
    if tortoise.xcor() > 100:
        tortoise.setx(100)

# Function to move the hare
def move_hare():
    num = random.randint(1, 10)
    if num <= 2:
        pass  # Sleep
    elif 3 <= num <= 4:
        hare.forward(7)  # Big Hop
    elif 5 <= num <= 5:
        hare.backward(10)  # Big Slip
    else:
        hare.forward(1)  # Small Hop

    # Ensure the hare stays within the race boundaries
    if hare.xcor() < -100:
        hare.setx(-100)
    if hare.xcor() > 100:
        hare.setx(100)

# Main race loop
clock = 0
while tortoise.xcor() < 100 and hare.xcor() < 100:
    move_tortoise()
    move_hare()
    clock += 1

# Determine the winner
if tortoise.xcor() >= 100:
    winner = "Tortoise"
else:
    winner = "Hare"

# Print the result
print(f"The winner is {winner} in {clock} seconds!")

# Close the turtle graphics window when clicked
screen.exitonclick()
