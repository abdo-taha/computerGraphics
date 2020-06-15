from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

FROM_RIGHT = 1
FROM_LEFT = 2
FROM_TOP = 3
FROM_BOTTOM = 4

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600

deltaX = 1
deltaY = 1

time_interval = 10  # try  1000 msec


class RECTA:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top


ball = RECTA(100, 100, 120, 120)  # initial position of the ball
wall = RECTA(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
player = RECTA(0, 0, 60, 10)  # initial position of the bat


# Initialization
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)  # l,r,b,t,n,f

    glMatrixMode(GL_MODELVIEW)


def DrawRectangle(rect):
    glLoadIdentity()
    glBegin(GL_QUADS)
    glVertex(rect.left, rect.bottom, 0)  # Left - Bottom
    glVertex(rect.right, rect.bottom, 0)
    glVertex(rect.right, rect.top, 0)
    glVertex(rect.left, rect.top, 0)
    glEnd()


def drawText(string, x, y):
    glLineWidth(2)
    glColor(1, 1, 0)  # Yellow Color
    glLoadIdentity()  # remove the previous transformations
    #       glScale(0.13,0.13,1)  # Try this line
    glTranslate(x, y, 0)  # try comment this line
    glScale(0.13, 0.13, 1)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:  # render character by character starting from the origin
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)


def Test_Ball_Wall(ball, wall):  # Collision Detection between Ball and Wall
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM

    # print(ball.right)

    if ball.right >= wall.right:
        return FROM_RIGHT
    if ball.left <= wall.left:
        return FROM_LEFT
    if ball.top >= wall.top:
        return FROM_TOP
    if ball.bottom <= wall.bottom:
        return FROM_BOTTOM

    # Otherwise this function returns None


def Test_Ball_Player(ball, player):  # Collision Detection between Ball and Bat
    if ball.bottom <= player.top and ball.left >= player.left and ball.right <= player.right:
        return True
    return False


# Key Board Messages
def keyboard(key, x, y):
    if key == b"q":
        sys.exit(0)


mouse_x = 0


def MouseMotion(x, y):  # returns the mouse coordinates in "pixel"
    global mouse_x
    mouse_x = x


# print("mouse_x= ",x, "pixels")
# print("mouse_y= ",y, "pixels")


def Timer(v):
    Display()

    glutTimerFunc(time_interval, Timer, 1)


pcResult = 0
playerResult = 0


def Display():
    global pcResult
    global playerResult
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM
    global deltaX
    global deltaY

    glClear(GL_COLOR_BUFFER_BIT)

    string = "PC : " + str(pcResult)
    drawText(string, 10, 440)
    string = "Player :  " + str(playerResult)
    drawText(string, 10, 400)

    ball.left = ball.left + deltaX  # updating ball's coordinates
    ball.right = ball.right + deltaX
    ball.top = ball.top + deltaY
    ball.bottom = ball.bottom + deltaY

    glColor(1, 1, 1)  # White color

    DrawRectangle(ball)

    # print(Test_Ball_Wall(ball,wall))

    if Test_Ball_Wall(ball, wall) == FROM_RIGHT:
        deltaX = -1

    if Test_Ball_Wall(ball, wall) == FROM_LEFT:
        deltaX = 1

    if Test_Ball_Wall(ball, wall) == FROM_TOP:
        deltaY = -1

    if Test_Ball_Wall(ball, wall) == FROM_BOTTOM:
        deltaY = 1
        pcResult = pcResult + 1

    player.left = mouse_x - 30  # remember that "mouse_x" is a global variable
    player.right = mouse_x + 30
    DrawRectangle(player)

    if Test_Ball_Player(ball, player) == True:
        deltaY = 1
        playerResult = playerResult + 1

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)  # mouse coordinates inbetween [WINDOW_WIDTH=800,WINDOW_HEIGHT=500]
    # glutInitWindowSize (1100, 600) # try and notice the bat; mouse coordinates inbetween [1100,600] (where 1100 pixels = 800 in openGL)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Simple Ball Bat OpenGL game")
    glutDisplayFunc(Display)
    glutTimerFunc(time_interval, Timer, 1)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(MouseMotion)
    init()
    glutMainLoop()


main()
