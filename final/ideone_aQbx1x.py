from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import pygame

global texture
first_init = True
# coin = 0
FROM_RIGHT = 1
FROM_LEFT = 2
FROM_TOP = 3
FROM_BOTTOM = 4

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

deltaX = 1
deltaY = 1

time_interval = 1
update_interval = 10000

playerWidth = 100

score = 0
last_score = 0
best_score = 0
isPlaying = False
can_print = True
update_interval_p = 400


def tex():
    texture = glGenTextures(11)  ## change the number
    # repeat for any texture
    ##################################################################################
    imgload = pygame.image.load("bricks1.png")  ### change to your texture
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[1])  ## change the index
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
    imgload = pygame.image.load("back1.png")  ### change to your texture
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[9])  ## change the index
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    ####################################################################################

    imgload = pygame.image.load("menu.png")  ### change to your texture
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[10])  ## change the index
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
        rl = False
        tb = False
        if self.top >= Rec.bottom and self.top <= Rec.top:
            tb = True
        if self.bottom <= Rec.top and self.bottom >= Rec.bottom:
            tb = True
        if self.right >= Rec.left and self.right <= Rec.right:
            rl = True
        if self.left <= Rec.right and self.left >= Rec.left:
            rl = True
        return rl and tb

    def render(self):
        glLoadIdentity()
        glBegin(GL_QUADS)
        glVertex(self.left, self.bottom, 0)
        glVertex(self.right, self.bottom, 0)
        glVertex(self.right, self.top, 0)
        glVertex(self.left, self.top, 0)
        glEnd()

    def render_t(self, n_tex):
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


class BLOCKS:
    def __init__(self, x, y, lines):
        self.x = x
        self.y = y
        self.lines = lines
        self.width = WINDOW_WIDTH / self.x
        self.height = WINDOW_HEIGHT / self.y
        self.arr = [[0 for i in range(x)] for j in range(y)]

        for i in range(self.y - lines, self.y):
            for j in range(x):
                self.arr[i][j] = 5
        for i in range(self.y - 3 * lines, self.y - 2 * lines):
            for j in range(x):
                self.arr[i][j] = 4

        self.lose = False

    def getRect(self, x, y):
        x1 = x * self.width + 0.07 * self.width  # left
        x2 = x1 + self.width - 0.07 * self.width  # right
        y2 = y * self.height + 0.07 * self.height  # bottom
        y1 = y2 + self.height - 0.07 * self.height  # up

        return RECT(x1, x2, y2, y1)

    def renderBlock(self, x, y, n):
        self.getRect(x, y).render_t(n)

    def renderAll(self):
        for i in range(self.y):
            for j in range(self.x):
                if self.arr[i][j] != 0:
                    self.renderBlock(j, i, self.arr[i][j])

    def checkCollision(self, ball):
        global deltaX
        global deltaY
        count = 0
        x = (ball.left + ball.right) / 2  # center of ball
        y = (ball.top + ball.bottom) / 2

        x = int(x / self.width)
        y = int(y / self.height)
        # print(x, " ", y)
        dx = [1, 1, 0, -1, -1, -1, 0, 1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]

        for i in range(8):
            tmpx = x + dx[i]
            tmpy = y + dy[i]

            if tmpx >= self.x or tmpx < 0 or tmpy >= self.y or tmpy < 0:  # not valid index
                continue
            color = self.arr[tmpy][tmpx]
            score = self.value(color)
            if self.arr[tmpy][tmpx] != 0 and self.checkOneBlock(tmpx, tmpy, ball):
                if dx[i] != 0:
                    deltaX *= -dx[i]
                if dy[i] != 0:
                    deltaY = -dy[i]
                count += score
        return count

    def checkOneBlock(self, x, y, ball):
        global deltaX
        global deltaY
        block = self.getRect(x, y)
        check = ball.collision(block)

        if not check:
            return 0

        self.arr[y][x] = 0
        return 1

    def udate(self):
        for i in range(self.x):
            if self.arr[1][i] != 0:
                self.lose = True

        for i in range(0, self.y - 1):
            for j in range(self.x):
                if i < self.y - self.lines and i > self.y - 2 * self.lines:
                    if self.arr[i + 1][j] != 0:
                        self.arr[i + 1][j] = 2
                if i < self.y - 2 * self.lines and i > self.y - 3 * self.lines:
                    if self.arr[i + 1][j] != 0:
                        self.arr[i + 1][j] = 4
                if i < self.y - 3 * self.lines and i > self.y - 4 * self.lines:
                    if self.arr[i + 1][j] != 0:
                        self.arr[i + 1][j] = 3
                if i < self.y - 4 * self.lines:
                    if self.arr[i + 1][j] != 0:
                        self.arr[i + 1][j] = 7
                self.arr[i][j] = self.arr[i + 1][j]
        for i in range(self.x):
            if self.arr[self.y - 1 - self.lines][i] != 0:
                self.arr[self.y - 1][i] = 0
            else:
                self.arr[self.y - 1][i] = 5

    def check_lose(self):
        return self.lose

    def value(self, color):
        if color == 7:
            return 1
        if color == 3:
            return 2
        if color == 4:
            return 3
        if color == 2:
            return 4
        if color == 5:
            return 5
        return 0

    def get_color(self, i):

        if i // self.lines == 6:
            return 2
        if i // self.lines == 5:
            return 4
        if i // self.lines == 4:
            return 3
        if i // self.lines <= 3:
            return 7
        return 5

    def ball_color(self, ball):
        y = (ball.top + ball.bottom) / 2
        y = int(y / self.height)
        return self.get_color(y)


ball = RECT(100, 110, 100, 110)
wall = RECT(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
player = RECT(0, playerWidth, 0, 10)
blocks = BLOCKS(13, 32, 4)

frame1 = RECT(-15, 0, 10, 300)
frame2 = RECT(WINDOW_WIDTH, WINDOW_WIDTH + 15, 10, 300)
frame3 = RECT(-15, 0, 300, 375)
frame4 = RECT(WINDOW_WIDTH, WINDOW_WIDTH + 15, 300, 375)
frame5 = RECT(-15, 0, 375, 450)
frame6 = RECT(WINDOW_WIDTH, WINDOW_WIDTH + 15, 375, 450)
frame7 = RECT(-15, 0, 450, 525)
frame8 = RECT(WINDOW_WIDTH, WINDOW_WIDTH + 15, 450, 525)
frame9 = RECT(-15, WINDOW_WIDTH + 15, 525, 615)
frame10 = RECT(-15, 0, 0, 10)
frame11 = RECT(WINDOW_WIDTH, WINDOW_WIDTH + 15, 0, 10)


def frame():
    frame1.render_t(7)
    frame2.render_t(7)
    frame3.render_t(3)
    frame4.render_t(3)
    frame5.render_t(4)
    frame6.render_t(4)
    frame7.render_t(2)
    frame8.render_t(2)
    frame9.render_t(5)
    frame10.render_t(5)
    frame11.render_t(5)


def init():
    global first_init
    global texture
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-15, WINDOW_WIDTH + 15, 0, WINDOW_HEIGHT + 15, 0, 1)  # l,r,b,t,n,f

    glMatrixMode(GL_MODELVIEW)
    if first_init:
        first_init = False
        texture = tex()


def drawText(string, x, y):
    if not can_print:
        return
    glLineWidth(2)
    glColor3f(1, 0, 0)
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
    x_player = (player.left + player.right) / 2
    if ball.bottom <= player.top and ball.left >= player.left and ball.right <= player.right:
        deltaX = math.sin((x_ball - x_player) / (player.right - player.left) * math.pi)
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
        deltaX = -1 * abs(deltaX)

    if Test_Ball_Wall(ball, wall) == FROM_LEFT:
        deltaX = 1 * abs(deltaX)

    if Test_Ball_Wall(ball, wall) == FROM_TOP:
        deltaY = -1

    if Test_Ball_Wall(ball, wall) == FROM_BOTTOM:
        deltaY = 1
        return 1
    return 0


def keyboard(key, x, y):
    if key == b"q":
        sys.exit(0)


def reset():
    global deltaX
    global deltaY
    global last_score
    global best_score
    global score
    global ball
    global blocks
    global score
    # global coin
    deltaX = 1
    deltaY = 1
    last_score = score
    score = 0
    best_score = max(best_score, last_score)
    ball = RECT(100, 110, 100, 110)
    blocks = BLOCKS(13, 32, 4)


mouse_x = 0


def MouseMotion(x, y):
    # print(x," ",y)
    global mouse_x
    if x + playerWidth / 2 > WINDOW_WIDTH:
        x = WINDOW_WIDTH - playerWidth / 2
    if x - playerWidth / 2 < 0:
        x = playerWidth / 2

    player.left = mouse_x - playerWidth / 2
    player.right = mouse_x + playerWidth / 2

    mouse_x = x


def mousefunc(button, state, x, y):
    global isPlaying
    if isPlaying:
        return
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and x in range(256, 342) and y in range(292, 324):
        #playing()
        isPlaying = True
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and x in range(256, 342) and y in range(357, 384):
        sys.exit()


def Timer(v):
    if isPlaying:
        Display1()
    else:
        Display2()
    glutTimerFunc(time_interval, Timer, 1)


def Timer1(v):
    global isPlaying
    if isPlaying:
        blocks.udate()
    glutTimerFunc(update_interval, Timer1, 1)


def Timer2(v):
    global can_print
    can_print = not can_print
    glutTimerFunc(update_interval_p, Timer2, 1)


def Display2():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1, 1, 1)
    frame()
    wall.render_t(10)
    drawText("last score : ", 250, WINDOW_HEIGHT - 30)
    drawText(str(last_score), 400, WINDOW_HEIGHT - 30)
    drawText("best score : ", 250, WINDOW_HEIGHT - 70)
    drawText(str(best_score), 400, WINDOW_HEIGHT - 70)
    glutSwapBuffers()


def Display1():
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM
    global deltaX
    global deltaY
    global score
    global isPlaying
    # global coin

    glClear(GL_COLOR_BUFFER_BIT)

    glColor(1, 1, 1)
    frame()
    wall.render_t(9)

    updateBall()

    ball.render_t(blocks.ball_color(ball))

    glColor(1, 1, 1)
    score += blocks.checkCollision(ball)
    blocks.renderAll()

    if checkWall() or blocks.check_lose():
        isPlaying = False
        reset()
        # coin+=1

    player.render_t(5)

    if Test_Ball_Player(ball, player) == True:
        deltaY = 1

    drawText("Player : ", 10, WINDOW_HEIGHT - 20)
    drawText(str(score), 100, WINDOW_HEIGHT - 20)

    # drawText("Coin : ",10,WINDOW_HEIGHT-40)
    # drawText(str(coin), 100, WINDOW_HEIGHT - 40)

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"break")
    init()
    glutDisplayFunc(Display2)
    glutMouseFunc(mousefunc)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(MouseMotion)
    glutTimerFunc(time_interval, Timer, 1)
    glutTimerFunc(update_interval, Timer1, 1)
    glutTimerFunc(update_interval_p, Timer2, 1)
    glutMainLoop()

'''
def not_playing():
    glutDisplayFunc(Display2)


def playing():
    glutDisplayFunc(Display1)
'''

main()
