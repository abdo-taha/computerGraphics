
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import numpy as np
import math
def cir(dx = 0, dy = 0 , r = 1 ):
    glTranslate(dx, dy, 0)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 360, 0.1):
        glColor3f(random.randrange(0,51)/50,random.randrange(0,51)/50,random.randrange(0,51)/50)
        y = math.cos(theta * math.pi / 180) * r
        x = math.sin(theta * math.pi / 180) * r
        glVertex2d(x, y)
    glEnd()
    glLoadIdentity()



def draw():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0.3)

    glBegin(GL_LINES)
    glVertex2d(-1,0)
    glVertex2d(1,0)
    glVertex2d(0,-1)
    glVertex2d(0,1)
    glEnd()
    glColor3f(0, 0, 0)



    glBegin(GL_POINTS)
    for x in np.arange(-1,1,0.001):
        y = math.sin(x*np.pi)
        glVertex2d(x,y)
    glEnd()
    glColor3f(0,1,0)
    cir(0.5,0.5,0.25)
    cir(-0.5,-0.5,0.25)

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"abdo is practicing")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()