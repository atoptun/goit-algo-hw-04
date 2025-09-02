import argparse
from turtle import Screen, Turtle


parser = argparse.ArgumentParser(description="The Koch snowflake")
parser.add_argument("-o", "--order", type=int, default=3, help="Order")
parser.add_argument("-s", "--size", type=int, default=300, help="Size")

args = parser.parse_args()


def koch_curve(t: Turtle, order: int, size: float):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order: int, size: float=300):
    window = Screen()
    window.bgcolor("white")

    t = Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / 4)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

if __name__ == '__main__':
    draw_koch_curve(args.order, args.size)
