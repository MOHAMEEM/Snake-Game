from turtle import Turtle,Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game 🐍🐍🐍")

starting_position = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_position:
    segment_1 = Turtle("square")
    segment_1.color("white")
    segment_1.goto(position)