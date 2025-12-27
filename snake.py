import random
import turtle as t

t.bgcolor('yellow')

# Create the snake (main character)
snake = t.Turtle()
snake.shape('square')
snake.color('orange')
snake.speed(0)
snake.penup()
snake.hideturtle()

# Create the apple shape with rounder coordinates
apple = t.Turtle()
apple_shape = ((0, -10), (5, -7), (10, 0), (5, 10), (0, 12), (-5, 10), (-10, 0), (-5, -7))
t.register_shape('apple', apple_shape)
apple.shape('apple')
apple.color('red')
apple.penup()
apple.hideturtle()
apple.speed(0)

game_started = False

# Display start text
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align='center', font=('Times New Roman', 25, 'bold'))
text_turtle.hideturtle()

# Display score
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = snake.pos()
    outside = \
        x < left_wall or \
        x > right_wall or \
        y < bottom_wall or \
        y > top_wall
    return outside

def game_over():
    snake.color('yellow')
    apple.color('yellow')
    game_over_turtle = t.Turtle()
    game_over_turtle.penup()
    game_over_turtle.hideturtle()
    game_over_turtle.write('GAME OVER!', align='center', font=('Times New Roman', 35, 'normal'))
    return game_over_turtle

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right', font=('Times New Roman', 40, 'bold'))

def place_apple():
    apple.ht()
    apple.setx(random.randint(-200, 200))
    apple.sety(random.randint(-200, 200))
    apple.st()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    score = 0
    text_turtle.clear()
    score_turtle.clear()  # clear old score
    snake_speed = 2
    snake_length = 3
    snake.shapesize(1, snake_length, 1)
    snake.showturtle()
    display_score(score)
    place_apple()
    while True:
        snake.forward(snake_speed)
        if snake.distance(apple) < 20:
            place_apple()
            snake_length = snake_length + 0.5
            snake.shapesize(1, snake_length, 1)
            snake_speed = snake_speed + 0.33
            score = score + 10
            display_score(score)
        if outside_window():
            game_over_turtle = game_over()

            yes_button = t.Turtle()
            yes_button.shape('circle')
            yes_button.color('green')
            yes_button.shapesize(3)
            yes_button.penup()
            yes_button.goto(-80, -100)
            yes_button.write('YES', align='center', font=('Arial', 16, 'bold'))
            
            no_button = t.Turtle()
            no_button.shape('circle')
            no_button.color('red')
            no_button.shapesize(3)
            no_button.penup()
            no_button.goto(80, -100)
            no_button.write('NO', align='center', font=('Arial', 16, 'bold'))
            
            def restart(x, y):
                global game_started
                game_started = False
                yes_button.clear()
                yes_button.hideturtle()
                no_button.clear()
                no_button.hideturtle()
                game_over_turtle.clear()
                snake.goto(0, 0)
                snake.setheading(0)
                snake.color('orange')
                apple.color('red')
                start_game()
            
            def quit_game(x, y):
                t.bye()
            
            yes_button.onclick(restart)
            no_button.onclick(quit_game)
            break

def move_up():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(90)

def move_down():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(270)

def move_left():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(180)

def move_right():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(0)

t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.listen()
t.mainloop()