from tkinter import *

WIDTH = 900
HEIGHT = 300


PAD_W = 10
PAD_H = 100

BALL_RADIUS = 30

root = Tk()
root.title("PythonicWay Pong")

c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()

c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill="white")
c.create_line(WIDTH - PAD_W, 0, WIDTH - PAD_W, HEIGHT, fill="white")
c.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="white")

BALL = c.create_oval(WIDTH / 2 - BALL_RADIUS / 2,
                     HEIGHT / 2 - BALL_RADIUS / 2,
                     WIDTH / 2 + BALL_RADIUS / 2,
                     HEIGHT / 2 + BALL_RADIUS / 2, fill="white")

LEFT_PAD = c.create_line(PAD_W / 2, 0, PAD_W / 2, PAD_H, width=PAD_W, fill="yellow")

RIGHT_PAD = c.create_line(WIDTH - PAD_W / 2, 0, WIDTH - PAD_W / 2,
                          PAD_H, width=PAD_W, fill="yellow")

root.mainloop()
BALL_X_CHANGE = 20
BALL_Y_CHANGE = 0


def move_ball():
    c.move(BALL, BALL_X_CHANGE, BALL_Y_CHANGE)


def main():
    move_ball()
    root.after(30, main)

main()
PAD_SPEED = 20
LEFT_PAD_SPEED = 0
RIGHT_PAD_SPEED = 0

def move_pads():
    PADS = {LEFT_PAD: LEFT_PAD_SPEED,
            RIGHT_PAD: RIGHT_PAD_SPEED}
    for pad in PADS:
        c.move(pad, 0, PADS[pad])
        if c.coords(pad)[1] < 0:
            c.move(pad, 0, -c.coords(pad)[1])
        elif c.coords(pad)[3] > HEIGHT:
            c.move(pad, 0, HEIGHT - c.coords(pad)[3])


def main():
    move_ball()
    move_pads()
    root.after(30, main)


c.focus_set()


def movement_handler(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym == "w":
        LEFT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "s":
        LEFT_PAD_SPEED = PAD_SPEED
    elif event.keysym == "Up":
        RIGHT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "Down":
        RIGHT_PAD_SPEED = PAD_SPEED


c.bind("<KeyPress>", movement_handler)


def stop_pad(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym in "ws":
        LEFT_PAD_SPEED = 0
    elif event.keysym in ("Up", "Down"):
        RIGHT_PAD_SPEED = 0


c.bind("<KeyRelease>", stop_pad)
from tkinter import *

WIDTH = 900
HEIGHT = 300


PAD_W = 10
PAD_H = 100


BALL_RADIUS = 30

root = Tk()
root.title("PythonicWay Pong")

c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()

c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill="white")
c.create_line(WIDTH - PAD_W, 0, WIDTH - PAD_W, HEIGHT, fill="white")
c.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="white")

BALL = c.create_oval(WIDTH / 2 - BALL_RADIUS / 2,
                     HEIGHT / 2 - BALL_RADIUS / 2,
                     WIDTH / 2 + BALL_RADIUS / 2,
                     HEIGHT / 2 + BALL_RADIUS / 2, fill="white")

LEFT_PAD = c.create_line(PAD_W / 2, 0, PAD_W / 2, PAD_H, width=PAD_W, fill="yellow")

RIGHT_PAD = c.create_line(WIDTH - PAD_W / 2, 0, WIDTH - PAD_W / 2,
                          PAD_H, width=PAD_W, fill="yellow")

root.mainloop()
BALL_X_CHANGE = 20
BALL_Y_CHANGE = 0


def move_ball():
    c.move(BALL, BALL_X_CHANGE, BALL_Y_CHANGE)


def main():
    move_ball()
    root.after(30, main)


main()
PAD_SPEED = 20
LEFT_PAD_SPEED = 0
RIGHT_PAD_SPEED = 0

def move_pads():
    PADS = {LEFT_PAD: LEFT_PAD_SPEED,
            RIGHT_PAD: RIGHT_PAD_SPEED}
    for pad in PADS:
        c.move(pad, 0, PADS[pad])
        if c.coords(pad)[1] < 0:
            c.move(pad, 0, -c.coords(pad)[1])
        elif c.coords(pad)[3] > HEIGHT:
            c.move(pad, 0, HEIGHT - c.coords(pad)[3])

def main():
    move_ball()
    move_pads()
    root.after(30, main)

c.focus_set()

def movement_handler(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym == "w":
        LEFT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "s":
        LEFT_PAD_SPEED = PAD_SPEED
    elif event.keysym == "Up":
        RIGHT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "Down":
        RIGHT_PAD_SPEED = PAD_SPEED


c.bind("<KeyPress>", movement_handler)

def stop_pad(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym in "ws":
        LEFT_PAD_SPEED = 0
    elif event.keysym in ("Up", "Down"):
        RIGHT_PAD_SPEED = 0

c.bind("<KeyRelease>", stop_pad)
from tkinter import *

WIDTH = 900
HEIGHT = 300

PAD_W = 10
PAD_H = 100

BALL_RADIUS = 30

root = Tk()
root.title("PythonicWay Pong")

c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()

c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill="white")
c.create_line(WIDTH - PAD_W, 0, WIDTH - PAD_W, HEIGHT, fill="white")
c.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="white")

BALL = c.create_oval(WIDTH / 2 - BALL_RADIUS / 2,
                     HEIGHT / 2 - BALL_RADIUS / 2,
                     WIDTH / 2 + BALL_RADIUS / 2,
                     HEIGHT / 2 + BALL_RADIUS / 2, fill="white")

LEFT_PAD = c.create_line(PAD_W / 2, 0, PAD_W / 2, PAD_H, width=PAD_W, fill="yellow")

RIGHT_PAD = c.create_line(WIDTH - PAD_W / 2, 0, WIDTH - PAD_W / 2,
                          PAD_H, width=PAD_W, fill="yellow")

root.mainloop()
BALL_X_CHANGE = 20
# по вертикали
BALL_Y_CHANGE = 0


def move_ball():
    c.move(BALL, BALL_X_CHANGE, BALL_Y_CHANGE)


def main():
    move_ball()
    root.after(30, main)


main()
PAD_SPEED = 20
LEFT_PAD_SPEED = 0
RIGHT_PAD_SPEED = 0

def move_pads():
    PADS = {LEFT_PAD: LEFT_PAD_SPEED,
            RIGHT_PAD: RIGHT_PAD_SPEED}
    for pad in PADS:
        c.move(pad, 0, PADS[pad])
        if c.coords(pad)[1] < 0:
            c.move(pad, 0, -c.coords(pad)[1])
        elif c.coords(pad)[3] > HEIGHT:
            c.move(pad, 0, HEIGHT - c.coords(pad)[3])

def main():
    move_ball()
    move_pads()
    root.after(30, main)


c.focus_set()


def movement_handler(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym == "w":
        LEFT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "s":
        LEFT_PAD_SPEED = PAD_SPEED
    elif event.keysym == "Up":
        RIGHT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "Down":
        RIGHT_PAD_SPEED = PAD_SPEED

c.bind("<KeyPress>", movement_handler)

def stop_pad(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym in "ws":
        LEFT_PAD_SPEED = 0
    elif event.keysym in ("Up", "Down"):
        RIGHT_PAD_SPEED = 0

c.bind("<KeyRelease>", stop_pad)
from tkinter import *

WIDTH = 900
HEIGHT = 300

PAD_W = 10
PAD_H = 100

BALL_RADIUS = 30

root = Tk()
root.title("PythonicWay Pong")

c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()

c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill="white")
c.create_line(WIDTH - PAD_W, 0, WIDTH - PAD_W, HEIGHT, fill="white")
c.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="white")

BALL = c.create_oval(WIDTH / 2 - BALL_RADIUS / 2,
                     HEIGHT / 2 - BALL_RADIUS / 2,
                     WIDTH / 2 + BALL_RADIUS / 2,
                     HEIGHT / 2 + BALL_RADIUS / 2, fill="white")

LEFT_PAD = c.create_line(PAD_W / 2, 0, PAD_W / 2, PAD_H, width=PAD_W, fill="yellow")

RIGHT_PAD = c.create_line(WIDTH - PAD_W / 2, 0, WIDTH - PAD_W / 2,
                          PAD_H, width=PAD_W, fill="yellow")
root.mainloop()
BALL_X_CHANGE = 20
BALL_Y_CHANGE = 0


def move_ball():
    c.move(BALL, BALL_X_CHANGE, BALL_Y_CHANGE)


def main():
    move_ball()
    root.after(30, main)


main()
PAD_SPEED = 20
LEFT_PAD_SPEED = 0
RIGHT_PAD_SPEED = 0


def move_pads():
    PADS = {LEFT_PAD: LEFT_PAD_SPEED,
            RIGHT_PAD: RIGHT_PAD_SPEED}
    for pad in PADS:
        c.move(pad, 0, PADS[pad])
        if c.coords(pad)[1] < 0:
            c.move(pad, 0, -c.coords(pad)[1])
        elif c.coords(pad)[3] > HEIGHT:
            c.move(pad, 0, HEIGHT - c.coords(pad)[3])

def main():
    move_ball()
    move_pads()
    root.after(30, main)

c.focus_set()

def movement_handler(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym == "w":
        LEFT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "s":
        LEFT_PAD_SPEED = PAD_SPEED
    elif event.keysym == "Up":
        RIGHT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "Down":
        RIGHT_PAD_SPEED = PAD_SPEED

c.bind("<KeyPress>", movement_handler)

def stop_pad(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym in "ws":
        LEFT_PAD_SPEED = 0
    elif event.keysym in ("Up", "Down"):
        RIGHT_PAD_SPEED = 0


c.bind("<KeyRelease>", stop_pad)