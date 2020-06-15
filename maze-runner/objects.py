import  skyboxcoord
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
class skybox:
    def __init__(self):
        skyload = skyboxcoord.skyboxcoord()
        self.sky = skyload.coord()
    def draw(self):
        glBegin(GL_QUADS)
        for i in range(len(self.sky) // 5):
            glTexCoord(self.sky[i * 5 + 3], self.sky[i * 5 + 4])
            glVertex3d(self.sky[i * 5], self.sky[i * 5 + 1], self.sky[i * 5 + 2])
        glEnd()

class map:
    def __init__(self,n):
        self.n = n
        self.map = [ [0 for i in range(n)] for j in range(n) ]
        for i in range(n):
            self.map[0][i] = 1
            self.map[n-1][i] = 1
            self.map[i][0] = 1
            self.map[i][n-1] = 1
        self.map[1][1] = 2
        self.map[n-2][n-2] = 3

    def get_map(self):
        return  self.map

    def valid_xy(self,x,y):
        return  x > 0 and y > 0 and x < self.n -1 and y < self.n-1

    def is_solvable(self):
        vst = [[False for i in range(self.n)] for j in range(self.n)]
        queue =[]
        queue.append((1,1))
        solvable = False
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        while queue:
            front = queue.pop(0)
            # print(front[0]," ",front[1] )

            vst[front[0]][front[1]] = True
            if front[0] == self.n-2 and front[1] == self.n-2:
                solvable = True
                break
            for i in range(4):
                x = front[0]+dx[i]
                y = front[1]+dy[i]
                if self.valid_xy(x,y) and vst[x][y] == False and self.map[x][y] != 1:
                    queue.append((x,y))
                    vst[x][y] = True
        return solvable

    def clear_map(self):
        for i in range(1,self.n-1):
            for j in range(1,self.n-1):
                self.map[i][j] = 0
        self.map[1][1] = 2
        self.map[self.n-2][self.n-2] = 3

    def random_map(self,percent):
        m = int(min(percent,70)/100 * (self.n**2)  )
        while True :
            tmp = m
            self.clear_map()
            while tmp > 0 :
                x = random.randint(1,self.n-2)
                y = random.randint(1,self.n-2)
                if self.map[x][y] == 0 :
                    self.map[x][y] = 1
                    tmp -= 1
            if self.is_solvable():
                break
