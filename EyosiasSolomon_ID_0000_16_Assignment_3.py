# Question 1

import random

def gen_num():
    num = random.randint(0, 20)
    guesses = 7
    while True and guesses > 0:
        guess = int(input("Enter your guess! "))
        if guess == num:
            print("You win! You guessed correctly!")
            break
        guesses -= 1
        print(f"Your guess was {"higher" if guess > num else "lower"}! Guess again! You have {guesses} guesses left!")
    print(f"Game over! The correct number was {num}")
    
# Question 2

import turtle

def draw_a_rectangle(SideX, SideY):
    bob = turtle.Turtle()
    bob.goto(0, 0)
    bob.right(bob.heading())
    bob.forward(SideX)
    bob.right(90)
    bob.forward(SideY)
    bob.right(90)
    bob.forward(SideX)
    bob.right(90)
    bob.forward(SideY)
    bob.right(90)
    
def draw_ethiopian_flag(size):
    bob = turtle.Turtle()
    bob.goto(0, 0)
    bob.right(bob.heading())
    colors = [(1, 0, 0), (1, 1, 0), (0, 1, 0)]
    part = 3
    for col in colors:
        bob.fillcolor(col)
        bob.begin_fill()
        bob.forward(size)
        bob.right(90)
        bob.forward(size/5 * part)
        bob.right(90)
        bob.forward(size)
        bob.right(90)
        bob.forward(size/5 * part)
        bob.right(90)
        bob.end_fill()
        part -= 1
    bob.penup()
    bob.goto(size/2, size/5 * -2)
    bob.pendown()
    bob.fillcolor(0, 0, 1)
    bob.begin_fill()
    bob.circle(size/10)
    bob.end_fill()

# Question 3

def dice_roll(side):
    rolled = random.randint(1, side)
    return rolled

# Question 4

def exchange_digit(num):
    num_str = str(num)
    rev_str = num_str[::-1]
    return int(rev_str)

# Question 5

def distance(x1, y1, x2, y2):
    dist = (((x1 - x2)**2) + ((y1 - y2)**2))**(1/2)
    return dist

def collision(x1, y1, r1, x2, y2, r2):
    min_distance = r1 + r2
    dist = distance(x1, y1, x2, y2)
    if dist > min_distance:
        return False
    return True
