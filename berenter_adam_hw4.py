#Assignment: Assignment #4
#
#Description: Draw circles, Draw squares
#
#Author: Adam Berenter
#WSU ID: 011440727
#Completion Time: Approximate 1 hour
#
#
#In completing this program, I obtained help or worked with the following: Erin Mullen (TA),
# and the website http://www.eg.bucknell.edu/~hyde/Python3/TurtleDirections.html#colour
#

from turtle import *
from random import *

#TODO: implement squares function
def squares(num_squares, width):
    for i in range(num_squares):
        #set colors to random
        a = randint(0, 255)
        b = randint(0, 255)
        c = randint(0, 255)
        color(a/255, b/255, c/255)

        #Fill and draw squares
        begin_fill()
        forward (width)
        right (90)
        forward (width)
        right (90)
        forward (width)
        right (90)
        forward (width)
        end_fill()

        #Rotate squares
        right (360 / num_squares)
    return

#TODO: implement circles function
import random

def circles(num_circles, radius):
    d = radius / num_circles
    for x in range(num_circles):

        #set colors to random integers
        a = randint(0, 255)
        b = randint(0, 255)
        c = randint(0, 255)

        #move pen to beginning of circle
        up()
        goto(0, -radius)
        down()
        color(a/255, b/255, c/255)

        #Fill circle and draw
        begin_fill()
        circle(radius)
        end_fill()

        #smaller circle
        radius -= d
    return

#main function is provided for you.  All you have to do is implement
#squares() and circles()!
def main():
    print("***Turtle Graphics Shape Generator***")
    print("1. Draw squares")
    print("2. Draw circles")
    selection = int(input("Selection: "))
    if selection == 1:
        num_squares = int(input("Enter number of squares to draw: "))
        width = int(input("Enter square width: "))
        squares(num_squares, width)
    else:
        num_circles = int(input("Enter the number of circles to draw: "))
        radius = int(input("Enter a starting radius: "))
        circles(num_circles, radius)

main()
    
    
    
