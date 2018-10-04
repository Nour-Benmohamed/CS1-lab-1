#  Author: Nour Benmohamed
# 10/2/2017
# program to play the game Pong

from cs1lib import *
from random import*

# By changing the Y-coordinates of the paddles, This function will move the paddles up and down depending on the
# states of the boolean variables without mixing up the actions of the buttons (i.e simultaneous movement)


def move():
    global yp1, yp2
    if kz is True and yp1 < 320:
        yp1 = yp1+SPEED
    if ka is True and yp1 > 0:
        yp1 = yp1-SPEED
    if km is True and yp2 < 320:
        yp2 = yp2+SPEED
    if kk is True and yp2 > 0:
        yp2 = yp2-SPEED


#  This call back function will change the boolean state variables to true if the buttons are pressed.


def press(key):
    global ka, kk, km, kz, play
    if key == L_DOWN:
        kz = True
    if key == L_UP:
        ka = True
    if key == R_DOWN:
        km = True
    if key == R_UP:
        kk = True
    move()
    if key == " ":
        play = True
    if key == "q":
        cs1_quit()


#  This call back function will change the boolean state variable to false when the buttons are released


def release(key):
    global kk, kz, km, ka
    if key == L_DOWN:
        kz = False
    if key == L_UP:
        ka = False
    if key == R_DOWN:
        km = False
    if key == R_UP:
        kk = False
    move()

# This function will return True if the ball touches one of the paddle or the horizontal wall allowing the condition
# in draw() to execute and bounce the ball


def collision():
    if x >= 379-R and y <= yp2+80 and y >= yp2:  # the ball touches the right paddle
        return True
    elif x <= 21+R and y <= yp1+80 and y >= yp1:  # the ball touches the left paddle
        return True
    elif x <= 380-R and y >= 399-R:  # the ball touches the bottom horizontal wall
        return True
    elif x >= 20+R and y <= 11:  # the ball touches the top horizontal wall
        return True
    else:
        return False

# This function will draw the paddles depending on the values of the y-coordinates of paddles 1 and 2
# It will also draw theb all depending on the x and y coordinates of the center. if the ball touches one of the vertical
# wall, the function will stop the game and a message with "GAME OVER" will appear.


def draw():

    global yp1, yp2, y, x, vx, vy, test, R, stop, red, g, b, play

    set_clear_color(0.9, 0, 0.9)  # red
    clear()
    enable_stroke()
    set_fill_color(0, 0, 0)  # black
    draw_rectangle(0, yp1, P_WIDTH, P_HEIGHT)
    draw_rectangle(380, yp2, P_WIDTH, P_HEIGHT)
    set_fill_color(red, g, b)
    set_stroke_color(0, 0, 0)  # black
    draw_circle(x, y, R)

    if stop is False:
        x = x+vx
        y = y+vy
    if x >= 389 or x <= 9:
        disable_stroke()
        set_fill_color(1, 0, 0)
        draw_rectangle(100, 145, 200, 100)
        set_fill_color(0, 1, 0)
        draw_rectangle(110, 155, 180, 80)
        set_fill_color(0, 0, 1)
        draw_rectangle(120, 165, 160, 60)
        enable_stroke()
        set_stroke_color(1, 1, 1)
        set_font_bold()
        set_font_size(15)
        draw_text("GAME OVER", 123, 200)
        stop = True

    elif collision() is True:
        if test is True:
            vx = -1*vx
            red = uniform(0, 1)
            g = uniform(0, 1)
            b = uniform(0, 1)
            test = False
        else:
            vy = -1*vy
            test = True
    if play is True:
        x = 200
        y = 200
        vx = randint(0, 1)*5
        if vx == 0:
            vx = -5
        vy = randint(0, 1)*5
        if vy == 0:
            vy = -5
        play = False
        stop = False


WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
P_WIDTH = 20  # paddle width
P_HEIGHT = 80  # paddle height
L_UP = 'a'  # right_up
L_DOWN = 'z'  # right_down
R_UP = 'k'  # Left_up
R_DOWN = 'm'  # left_down
SPEED = 10
yp1 = 0  # Y-coordinate of left paddle
yp2 = 0  # Y-coordinate of right paddle
kz = False  # state variable for when z is pressed
ka = False  # state variable for when a is pressed
kk = False  # state variable for when k is pressed
km = False  # state variable for when m is pressed
x = 200
y = 200
R = 10
vx = randint(0, 1)*5
if vx == 0:
    vx = -5
vy = randint(0, 1)*5
if vy == 0:
    vy = -5
test = True  # boolean used to alternate the change of the x and y velocities
stop = False  # boolean to stop the game when player looses
red = 1
g = 1
b = 0
play = False  # variable to allow the user to play again and reset the coordinates to initial values

start_graphics(draw, key_press=press, key_release=release)
