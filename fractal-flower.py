import turtle
import random

def fractal_flower(t, branch_len, branch_factor, angle, angle_factor, petals):
    if branch_len > 10:
        for i in range(petals):
            t.forward(branch_len)
            t.right(angle)
            fractal_flower(t, branch_len * branch_factor, branch_factor, angle + angle_factor, angle_factor, petals)
            t.left(angle * 2)
            fractal_flower(t, branch_len * branch_factor, branch_factor, angle + angle_factor, angle_factor, petals)
            t.right(angle)
            t.backward(branch_len)
            t.left(360/petals)

def generate_flower():
    t = turtle.Turtle()
    t.speed(0)
    t.up()
    t.goto(0, 0)
    t.down()

    # Generate random parameters for the fractal flower
    branch_len = random.randint(50, 100)
    branch_factor = random.uniform(0.5, 0.8)
    angle = random.randint(15, 45)
    angle_factor = random.uniform(1, 2)
    petals = random.randint(6, 12)

    fractal_flower(t, branch_len, branch_factor, angle, angle_factor, petals)
    turtle.done()

generate_flower()
