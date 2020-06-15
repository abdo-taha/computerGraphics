from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math
import pygame
import  ObjLoader as ol
import skyboxcoord
from ourfunctions import *
from ourtextures import *
from objects import *



### globals ###

height = 600
width = 800

camera_xyz =[5,5,5]
ch_xyx = [1,0,1]
look_at_xyz = [0,0,-1]
camera_up = [0,1,0]
mouse_xy = [height//2,width//2]
time_interval = 10
# angles for mouse view
pitch = 0
yaw = -90
first_mouse = True # for first mouse response
first_init = True # for loading textures once
global texture

###########################

### loading objects ###
obj = ol.ObjLoader().load_model('chibi.obj') # test
sky = skybox()

mp = map(20)
mp.random_map(35)
map = mp.get_map()
########################

def valid_xy(x,y,mx):
    return  x>=0 and y>= 0 and x<mx and y<mx
def draw_map():
    l = 5 # cube length
    glColor3f(1,0,0)
    for i in range(20):
        for j in range(20):
            if map[i][j] == 1:
                glLoadIdentity()
                glTranslate(i*l,0,j*l)
                glScale(1,10,1)
                glutSolidCube(l)
def draw_terrain():
    l = 100 # half of terrain side length
    t = 25 # texture co-ordenate
    glBindTexture(GL_TEXTURE_2D, texture[2])
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)
    glTexCoord(t,t)
    glVertex3d(l,0,l)
    glTexCoord(-t, t)
    glVertex3d(-l, 0, l)
    glTexCoord(-t,-t)
    glVertex3d(-l, 0, -l)
    glTexCoord(t,-t)
    glVertex3d(l, 0, -l)
    glEnd()
    glDisable(GL_TEXTURE_2D)
def can_move(x,y,l,r):
    x += l/2
    y += l/2
    x_i = int( x//l)
    y_i= int(y//l)
    dx = [1,1,0,-1,-1,-1,0,1]
    dy = [0,1,1,1,0,-1,-1,-1]
    # print(x, " ", y , " ",x_i , " ", y_i," ", map[x_i][y_i])
    if map[x_i][y_i] == 1 :
        return False
    x -= l / 2
    y -= l / 2
    for i in range(8):
        if valid_xy(x_i+dx[i],y_i+dy[i],20) and map[x_i+dx[i]][y_i+dy[i]] == 1 and  math.sqrt( (x-(x_i+dx[i])*l)**2 + (y-(y_i+dy[i])*l)**2 ) <= 0.5*l + r :
            return False
    return True


def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(80,1,0.1,200)
    gluLookAt(camera_xyz[0],camera_xyz[1],camera_xyz[2],
              look_at_xyz[0]+camera_xyz[0],look_at_xyz[1]+camera_xyz[1],look_at_xyz[2]+camera_xyz[2],
              camera_up[0], camera_up[1], camera_up[2])
    glMatrixMode(GL_MODELVIEW)
    ##############################################
    glClearDepth(1.0)  #  Depth Buffer Setup
    glDepthFunc(GL_LEQUAL)  #  The Type Of Depth Testing
    glEnable(GL_DEPTH_TEST)
    ##############################################
    ### load textures here ###########
    global  first_init
    if first_init:
        first_init = False
        global texture
        texture= tex()
    ###############################################

def draw():
    myInit()
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glDisable(GL_TEXTURE_2D)

    ###########################    map and earth    ###################################
    glLoadIdentity()
    draw_terrain()
    draw_map()
    ###########################  example  ################################

    # glColor3f(1, 1, 1)
    # glLoadIdentity()
    # glBindTexture(GL_TEXTURE_2D, texture[0])
    # glEnable(GL_TEXTURE_2D)
    # glBegin(GL_TRIANGLES)
    # for i in range(len(obj) // 8):
    #     glTexCoord(obj[i * 8 + 3], obj[i * 8 + 4])
    #     glVertex3d(obj[i * 8], obj[i * 8 + 1], obj[i * 8 + 2])
    # glEnd()

    ########################      charachter   ##############################
    glDisable(GL_TEXTURE_2D)
    glColor4f(1,1,1,0.2)
    glLoadIdentity()
    tmp = [i for i in look_at_xyz]
    tmp[1] = 0
    # glTranslate(camera_xyz[0] + normalize(tmp)[0] * 2, 0, camera_xyz[2] + normalize(tmp)[2] * 2)
    glTranslate(camera_xyz[0] , 0, camera_xyz[2] )
    glRotate(-yaw, 0, 1, 0)
    glutSolidCube(2)
    glEnable(GL_TEXTURE_2D)
    ##########################   sky box     ################################
    glLoadIdentity()
    glTranslate(camera_xyz[0],camera_xyz[1],camera_xyz[2])
    glBindTexture(GL_TEXTURE_2D, texture[1])
    sky.draw()
    #########################################################################

    glDisable(GL_TEXTURE_2D)

    glutSwapBuffers()

def MouseMotion(x, y):
    global mouse_xy , yaw , pitch , look_at_xyz,first_mouse,camera_up
    if first_mouse:
        first_mouse = False
        mouse_xy[0] = x
        mouse_xy[1] = y

    sense = 1
    deltax = (x-mouse_xy[0])*sense
    deltay = (mouse_xy[1]-y)*sense
    mouse_xy[0] = x
    mouse_xy[1] = y

    yaw += deltax
    pitch += deltay
    tmplook = [0,0,0]

    if pitch >89:
        pitch = 89
    if pitch < -89:
        pitch = -89

    tmplook[0] = np.cos(np.radians(yaw))*np.cos(np.radians(pitch))
    tmplook[1] = np.sin(np.radians(pitch))
    tmplook[2] = np.sin(np.radians(yaw))*np.cos(np.radians(pitch))

    look_at_xyz = normalize(tmplook)

def keyboard(key, xx, yy):
    global camera_xyz
    old_xyz = camera_xyz[:]
    speed = 0.5

    proj = look_at_xyz
    proj[1] = 0
    proj = normalize(proj)


    if key == b"w":
        for i in range(3):
            camera_xyz[i] += speed * proj[i]


    if key == b"s":
        for i in range(3):
         camera_xyz[i] -= speed * look_at_xyz[i]
    if key == b"a":
        tmp = normalize(cross(look_at_xyz,camera_up))
        for i in range(3):
            camera_xyz[i] -=tmp[i] * speed

    if key == b"d":
        tmp = normalize(cross(look_at_xyz, camera_up))
        for i in range(3):
            camera_xyz[i] += tmp[i] * speed
    MouseMotion(xx,yy)
    ###########    check collision #############

    if not can_move(camera_xyz[0],camera_xyz[2],5,1) : ##### make l r global

        camera_xyz = old_xyz

    # glutPostRedisplay()

def Timer(v):
    draw()
    glutTimerFunc(time_interval, Timer, 1)


glutInit()
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
glutInitWindowSize(width,height)
glutCreateWindow(b"abdo")
glutDisplayFunc(draw)
glutKeyboardFunc(keyboard)
glutPassiveMotionFunc(MouseMotion)
glutIdleFunc(draw)
glutTimerFunc(time_interval, Timer, 1)
glutMainLoop()