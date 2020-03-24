from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math
def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1,1,100)
    gluLookAt(10,10, 10,
              0, 0, 0,
              0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    # glEnable(GL_DEPTH_TEST)

def drawXYZ():
    glBegin(GL_LINES)
    # X
    glColor3f(1, 0, 0)
    glVertex3d(0, 0, 0)
    glVertex3d(100, 0, 0)

    # Y
    glColor3f(0, 1, 0)
    glVertex3d(0, 0, 0)
    glVertex3d(0, 100, 0)

    # Z
    glColor3f(0, 0, 1)
    glVertex3d(0, 0, 0)
    glVertex3d(0, 0, 100)

    glEnd()

x = 0
theta = 0
forward = True

def drawRound(theta1 , theta2 ,r, x,y,z , dz):
    glBegin(GL_LINES)
    dtheta = 15
    for dr in np.arange(theta1, theta2  , dtheta):
        glVertex3d(r*math.cos(dr * np.pi / 180)+x, r*math.sin(dr * np.pi / 180)+y, z+dz/2)
        glVertex3d(r * math.cos((dr+dtheta) * np.pi / 180) + x, r * math.sin((dr+dtheta) * np.pi / 180) + y,z+ dz/2)

        glVertex3d(r * math.cos(dr * np.pi / 180) + x, r * math.sin(dr * np.pi / 180) + y, z+dz/2)
        glVertex3d(r * math.cos(dr * np.pi / 180) + x, r * math.sin(dr * np.pi / 180) + y, z-dz/2)

        glVertex3d(r * math.cos(dr * np.pi / 180) + x, r * math.sin(dr * np.pi / 180) + y, z - dz / 2)
        glVertex3d(r * math.cos((dr + 20) * np.pi / 180) + x, r * math.sin((dr + 20) * np.pi / 180) + y, z - dz / 2)
    glEnd()

def drawTree(x,y,z,r,l1,l2):
    dth = 30
    glColor3f(0.4, 0.2, 0.2)
    glBegin(GL_LINES)
    for dr in np.arange(0,360,dth):
        glVertex3d(r * math.cos(dr * np.pi / 180) + x, y, r * math.sin(dr * np.pi / 180)+z )
        glVertex3d(r * math.cos((dr+dth) * np.pi / 180) + x, y, r * math.sin((dr+dth) * np.pi / 180) + z)
        glVertex3d(r * math.cos(dr * np.pi / 180) + x, y, r * math.sin(dr * np.pi / 180) + z)
        glVertex3d(r * math.cos(dr * np.pi / 180) + x, y+l1, r * math.sin(dr * np.pi / 180) + z)
        glVertex3d(r * math.cos(dr * np.pi / 180) + x, y+l1, r * math.sin(dr * np.pi / 180) + z)
        glVertex3d(r * math.cos((dr + dth) * np.pi / 180) + x, y+l1, r * math.sin((dr + dth) * np.pi / 180) + z)
    glEnd()
    glColor3f(0, 1, 0)
    glLoadIdentity()
    glTranslate(x,y+l1,z)
    glRotate(90,-1,0,0)
    glutWireCone(2*r,l2,5,5)
    glLoadIdentity()

def drawWheel(dx,dy,dz , theta):
    glTranslate(dx, dy, dz)
    glRotate(theta, 0, 0, -1)
    glutWireTorus(0.15, 0.35, 10, 12)


def drawCar():
    global x
    global theta
    global forward
    glLoadIdentity()
    glColor3f(1, 0, 0)

    drawRound(90,180,1,x-2.5,0,0,3)
    drawRound(0,90,1,x+2.5,0,0,3)
    drawRound(20,160,3,x+0,0,0,3)

    glColor3f(0, 0, 1)
    glLoadIdentity()
    drawWheel(x-2.5,0.5,1.5,theta)
    glLoadIdentity()
    drawWheel(x - 2.5, 0.5, -1.5, theta)
    glLoadIdentity()
    drawWheel(x + 2.5, 0.5, 1.5, theta)
    glLoadIdentity()
    drawWheel(x + 2.5, 0.5, -1.5, theta)
    glLoadIdentity()

    glColor3f(1, 1, 0)
    glLoadIdentity()

    glTranslate(x + 6, 0.5, 1.2)
    glRotate(90, 0, -1, 0)
    glRotate(15, -1, 0, 0)
    glutWireCone(1, 3, 10, 5)
    glLoadIdentity()
    glTranslate(x + 6, 0.5, -1.2)
    glRotate(90, 0, -1, 0)
    glRotate(15, -1, 0, 0)
    glutWireCone(1, 3, 10, 5)
    glLoadIdentity()


    if forward:
        x = x + 0.05
        theta = theta + 2
    else:
        x = x - 0.05
        theta = theta - 2

    if x >= 5.5:
        forward = False
    if x <= -15:
        forward = True

def drawRoad(ox,oy,oz,dx,dy,dz):

    glTranslate(ox,oy,oz)
    glBegin(GL_POLYGON)
    glVertex3d(dx/2,dy,dz/2)
    glVertex3d(dx/2, dy, -dz/2)
    glVertex3d(-dx/2, dy, -dz/2)
    glVertex3d(-dx/2, dy, dz/2)
    glEnd()
    glTranslate(-ox, -oy, -oz)

def draw():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glColor3f(0,0,0)
    drawRoad(0,0,0,70,0,10)
    glColor3f(0.3, 0.8, 0.3)
    drawRoad(0, 0, -15, 70, 0, 21)
    drawRoad(0, 0, 15, 70, 0, 21)

    for i in range(-25,10,5):
        glColor3f(1, 1, 1)
        drawRoad(i, 0, 0, 3, 0, 1)
        drawTree(i, 0, -5, 0.5, 2, 3)
        drawTree(i, 0, 5, 0.5, 2, 3)

    drawCar()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()