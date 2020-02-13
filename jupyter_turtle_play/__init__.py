"""
Wrapper functions (around the "calysto" package) for easy turtle graphics in a jupyterhub environment
"""
from calysto.graphics import *
from calysto.display import display, clear_output
import math

CANVAS, TURTLE = None, None
RGB_WHITE = (255, 255, 255)
RGB_YELLOW = (255, 223, 51)
RGB_ORANGE = (255, 153, 51)
RGB_RED = (255, 0, 0)
RGB_GREEN = (0, 204, 51)
RGB_BLUE = (0, 0, 255)
RGB_PURPLE = (127, 0 , 255)
RGB_GREY = (127, 127, 127)
RGB_BLACK = (0, 0, 0)
RGB_BROWN = (153, 76, 0)

def update():
  clear_output(wait=True)
  display( CANVAS )

def initializeTurtle():
  global CANVAS, TURTLE
  clear_output(wait=True)
  CANVAS = Canvas(size=(800, 500))
  #CANVAS.fill_color( Color(255, 255, 255) )
  TURTLE = Turtle(CANVAS, (400, 250), -90)
  TURTLE.stroke_width = 3
  TURTLE.penup()
  return( CANVAS, TURTLE )

def forward( d ):
  TURTLE.forward( d )
  update()
  
def backward( d ):
  TURTLE.backward( d )
  update()
  
def right( d ):
  TURTLE.right( d )
  update()
  
def left( d ):
  TURTLE.left( d )
  update()
  
def penup():
  TURTLE.penup()
  update()
  
def pendown():
  TURTLE.pendown()
  update()
  
def heading():
  return( TURTLE.angle / (2*math.pi) * 360 )

def face(d):
  current = heading()
  desired = d
  diff = desired - current
  TURTLE.right( diff )# = (d - 270) % 360

def goto( x, y ):
  TURTLE.goto( x, y )
  #face(0)
  update()

def getx():
  return( TURTLE.x )

def gety():
  return( TURTLE.y )

def color( c ):
  cout = None
  if c == "black":
    cout = Color( *RGB_BLACK )
  if c == "white":
    cout = Color( *RGB_WHITE )
  if c == "brown":
    cout = Color( *RGB_BROWN )
  if c == "grey":
    cout = Color( *RGB_GREY )
  if c == "gray":
    cout = Color( *RGB_GREY )
  if c == "red":
    cout = Color( *RGB_RED )
  if c == "green":
    cout = Color( *RGB_GREEN )
  if c == "blue":
    cout = Color( *RGB_BLUE )
  if c == "yellow":
    cout = Color( *RGB_YELLOW )
  if c == "purple":
    cout = Color( *RGB_PURPLE )
  if c == "orange":
    cout = Color( *RGB_ORANGE )
  TURTLE.stroke = cout
        
if __name__ == "__main__":
  initializeTurtle()
  pendown()
  forward(200) # pixels
  left(90)     # degrees
  forward(100) # pixels
  penup()
