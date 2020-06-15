from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import randint
import math
import pygame

global texture
first_init = True

FROM_RIGHT = 1
FROM_LEFT = 2
FROM_TOP = 4
FROM_BOTTOM = 8

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

deltaX = 1
deltaY = 1

time_interval = 4
update_interval = 20000

playerWidth = 100

score = 0


def tex():
    texture = glGenTextures(10) ## change the number
    # repeat for any texture
    ##################################################################################
    imgload = pygame.image.load("bricks1.png") ### change to your texture
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[1])## change the index
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    ####################################################################################
    imgload = pygame.image.load("bricks2.png")  ### change to your texture
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[2])  ## change the index
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    ####################################################################################
    imgload = pygame.image.load("bricks3.png")  ### change to your texture
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[3])  ## change the index
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    ####################################################################################
    imgload = pygame.image.load("bricks4.png")  ### change to your texture
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[4])  ## change the index
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    ####################################################################################
    imgload = pygame.image.load("bricks5.png")  ### change to your texture
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[5])  ## change the index
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    ####################################################################################
    imgload = pygame.image.load("bricks6.png")  ### change to your texture
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[6])  ## change the index
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    ####################################################################################
    imgload = pygame.image.load("bricks7.png")  ### change to your texture
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[7])  ## change the index
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    ####################################################################################
    imgload = pygame.image.load("player.png")  ### change to your texture
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[0])  ## change the index
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    ####################################################################################
    imgload = pygame.image.load("ball.png")  ### change to your texture
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[8])  ## change the index
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    ####################################################################################
    imgload = pygame.image.load("back.png")  ### change to your texture
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[9])  ## change the index
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    ####################################################################################
    glEnable(GL_TEXTURE_2D)
    return texture

class RECT:
    def __init__(self, left, right, bottom, top):
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top

    def collision(self, Rec):
        global FROM_RIGHT
        global FROM_LEFT
        global FROM_TOP
        global FROM_BOTTOM
        ret = 0
        check = False
        if self.top >= Rec.bottom and self.top <= Rec.top:
            ret |= FROM_TOP
        if self.bottom <= Rec.top and self.bottom >= Rec.bottom:
            ret |= FROM_BOTTOM
        if self.right >= Rec.left and self.right <= Rec.right:
            ret |= FROM_RIGHT
        if self.left <= Rec.right and self.left >= Rec.left:
            ret|= FROM_LEFT
        if  (ret&(FROM_LEFT|FROM_RIGHT)) and (ret&(FROM_BOTTOM|FROM_TOP))  :
            check = True
        # print(ret&(FROM_LEFT|FROM_RIGHT), " " ,ret&(FROM_BOTTOM|FROM_TOP))
        if not check:
            return None
        return ret
    def render(self):
        glLoadIdentity()
        glBegin(GL_QUADS)
        glVertex(self.left, self.bottom, 0)
        glVertex(self.right, self.bottom, 0)
        glVertex(self.right, self.top, 0)
        glVertex(self.left, self.top, 0)
        glEnd()
    def render_t(self,n_tex):
        glLoadIdentity()
        glBindTexture(GL_TEXTURE_2D, texture[n_tex])
        glEnable(GL_TEXTURE_2D)
        glBegin(GL_QUADS)
        glTexCoord(0, 0)
        glVertex(self.left, self.bottom, 0)
        glTexCoord(1, 0)
        glVertex(self.right, self.bottom, 0)
        glTexCoord(1, 1)
        glVertex(self.right, self.top, 0)
        glTexCoord(0, 1)
        glVertex(self.left, self.top, 0)
        glEnd()
        glDisable(GL_TEXTURE_2D)
    def print(self):
        print(self.left," ",self.right," ",self.bottom," ",self.top)

class BLOCKS:
    def __init__(self, x, y, percent):
        self.x = min(x,20)
        self.y = min(y,30)
        self.percent = percent
        self.width = WINDOW_WIDTH / self.x
        self.height = WINDOW_HEIGHT / self.y
        self.arr = [[0 for i in range(x)] for j in range(y)]

        for i in range(self.y//2,self.y):
            for j in range(x):
                if randint(0, 100) <= percent:
                    self.arr[i][j] = randint(1,7)

        self.lose = False

    def getRect(self,x,y):
        x1 = x * self.width + 0.05 * self.width # left
        x2 = x1 + self.width - 0.05 * self.width # right
        y2 = y * self.height + 0.05 * self.height   # bottom
        y1 = y2 + self.height - 0.05 * self.height  # up

        return RECT(x1,x2,y2,y1)

    def renderBlock(self,x,y,n):
        self.getRect(x,y).render_t(n)

    def renderAll(self):
        for i in range(self.y):
            for j in range(self.x):
                if self.arr[i][j] != 0:
                    self.renderBlock(j,i,self.arr[i][j])

    def checkCollision(self,ball):
        global deltaX
        global deltaY
        count = 0
        x = (ball.left + ball.right ) / 2 # center of ball
        y = (ball.top + ball.bottom) / 2

        x = int(x / self.width)
        y = int( y / self.height)
        # print(x, " ", y)
        dx = [1,1,0,-1,-1,-1,0,1]
        dy = [0,1,1,1,0,-1,-1,-1]

        for i in range(8):
            tmpx = x + dx[i]
            tmpy = y + dy[i]

            if tmpx >= self.x or tmpx < 0 or tmpy >= self.y or tmpy < 0: # not valid index
                continue
            if self.arr[tmpy][tmpx] != 0 and self.checkOneBlock(tmpx,tmpy,ball):
                if dx[i] != 0:
                    deltaX *= -dx[i]
                if dy[i] != 0:
                    deltaY = -dy[i]
                count += 1
        return count

    def checkOneBlock(self, x, y , ball):
        global  deltaX
        global  deltaY
        block = self.getRect(x,y)
        check = ball.collision(block)

        if check == None:
            return 0

        self.arr[y][x] = 0
        return  1

    def udate(self):
        for i in range(self.x):
            if self.arr[0][i] != 0:
                self.lose=True

        for i in range(0,self.y-1):
            for j in range(self.x):
                self.arr[i][j] = self.arr[i+1][j]
        for i in range(self.x):
            if randint(0,100) <= self.percent:
                self.arr[self.y-1][i] = randint(1,7)
            else:
                self.arr[self.y - 1][i] = 0


    def check_lose(self):
        return self.lose




ball = RECT(100, 110, 100, 110)
wall = RECT(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
player = RECT(0, playerWidth, 0, 10)
blocks = BLOCKS(10,20,40)


def init():
    global first_init
    global texture
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)  # l,r,b,t,n,f

    glMatrixMode(GL_MODELVIEW)
    if first_init:
        first_init = False
        texture = tex()

def drawText(string, x, y):
    glLineWidth(2)
    glColor3f(1,0,0)
    glLoadIdentity()
    glTranslate(x, y, 0)
    glScale(0.13, 0.13, 1)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:  # render character by character starting from the origin
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

def Test_Ball_Wall(ball, wall):
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM


    if ball.right >= wall.right:
        return FROM_RIGHT
    if ball.left <= wall.left:
        return FROM_LEFT
    if ball.top >= wall.top:
        return FROM_TOP
    if ball.bottom <= wall.bottom:
        return FROM_BOTTOM

def Test_Ball_Player(ball, player):
    global deltaX
    x_ball = (ball.left + ball.right) / 2  # center of ball
    x_player = (player.left+player.right) / 2
    if ball.bottom <= player.top and ball.left >= player.left and ball.right <= player.right:
        deltaX = math.sin((x_ball-x_player)/(player.right-player.left)*math.pi)
        return True
    return False

def updateBall():
    ball.left = ball.left + deltaX
    ball.right = ball.right + deltaX
    ball.top = ball.top + deltaY
    ball.bottom = ball.bottom + deltaY

def checkWall():
    global deltaX
    global deltaY
    if Test_Ball_Wall(ball, wall) == FROM_RIGHT:
        deltaX = -1*abs(deltaX)

    if Test_Ball_Wall(ball, wall) == FROM_LEFT:
        deltaX = 1*abs(deltaX)

    if Test_Ball_Wall(ball, wall) == FROM_TOP:
        deltaY = -1

    if Test_Ball_Wall(ball, wall) == FROM_BOTTOM:
        deltaY = 1
        return 1
    return 0

def keyboard(key, x, y):
    if key == b"q":
        sys.exit(0)

mouse_x = 0

def MouseMotion(x, y):
    global mouse_x
    if x + playerWidth/2 > WINDOW_WIDTH:
        x = WINDOW_WIDTH - playerWidth/2
    if x - playerWidth/2 < 0:
        x = playerWidth/2

    player.left = mouse_x - playerWidth/2
    player.right = mouse_x + playerWidth/2

    mouse_x = x

def Timer(v):
    Display()

    glutTimerFunc(time_interval, Timer, 1)
def Timer1(v):
    blocks.udate()
    glutTimerFunc(update_interval, Timer1, 1)

def Display():

    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM
    global deltaX
    global deltaY
    global score

    glClear(GL_COLOR_BUFFER_BIT)

    glColor(1, 1, 1)
    wall.render_t(9)

    updateBall()

    ball.render_t(8)

    glColor(1, 1, 1)
    score += blocks.checkCollision(ball)
    blocks.renderAll()

    if checkWall() or blocks.check_lose():
        sys.exit(0)


    player.render_t(0)

    if Test_Ball_Player(ball, player) == True:
        deltaY = 1

    drawText("score : ",10,WINDOW_HEIGHT-20)
    drawText(str(score), 100, WINDOW_HEIGHT - 20)

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"break")
    glutDisplayFunc(Display)
    glutTimerFunc(time_interval, Timer, 1)
    glutTimerFunc(update_interval, Timer1, 1)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(MouseMotion)
    init()
    glutMainLoop()


main()