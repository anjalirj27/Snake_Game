import turtle
import time
import random

# --- Game Settings ---
delay = 0.1  # Initial speed
score = 0
high_score = 0

# --- Set Up the Screen ---
wn = turtle.Screen()
wn.title("Classic Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turn off auto screen updates for smoother gameplay

# --- Snake Head ---
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# --- Snake Food ---
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# --- Snake Body Segments ---
segments = []

# --- Score Display ---
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# --- Movement Functions ---
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# --- Keyboard Controls ---
wn.listen()
wn.onkeypress(go_up, "u")
wn.onkeypress(go_down, "d")
wn.onkeypress(go_left, "l")
wn.onkeypress(go_right, "r")

# --- Main Game Loop ---
while True:
    wn.update()

    # Collision with wall
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide all segments off screen
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset game
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Collision with food
    if head.distance(food) < 20:
        # Move food to new random location
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

        # Add new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Update score and speed
        score += 10
        delay = max(0.02, delay - 0.005)  # Cap speed increase

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move the body (from last to first)
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].pos())

    # Move first segment to where the head is
    if segments:
        segments[0].goto(head.pos())

    move()

    # Collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
