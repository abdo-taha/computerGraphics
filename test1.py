from OpenGL.GL import *
from OpenGL.GLUT import *


def draw():
    glClearColor(0.7, 0.5, 0.3, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(.2, .9, 0.6)

    glTranslate(0.25, 0.25, 0.25)
    glRotate(30, 1, 0, 0)
    # glScale(1.5, 1.5, 1.5)

    glutWireTeapot(0.8)
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Tea pot Program")
glutDisplayFunc(draw)
glutMainLoop()