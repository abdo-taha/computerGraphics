"""
here we have our implemented functions
"""
import math

## cross and dot product
def cross(a , b):
    c =[0,0,0]
    c[0] = a[1]*b[2]-a[2]*b[1]
    c[1] = a[2]*b[0]-a[0]*b[2]
    c[2] = a[0]*b[1]-a[1]*b[0]
    return c


def dot(a,b):
    x = 0
    for i in  range(len(a)):
        x += a[i]*b[i]
    return math.sqrt(x)

############
### normalize a vector ###
def normalize(a):
    div = math.sqrt(a[0] ** 2 + a[1] ** 2 + a[2] ** 2)
    a[0] /= div
    a[1] /= div
    a[2] /= div
    return  a
#########
# it rotate look at about up vector
# need modifications to rotate vector vect about vector about by theta if needed

"""


def rotationmatrix(theta,vect,about):
   
    
    
    global  lookatxyz
    x=about[0]
    y=about[1]
    z=about[2]

    m = [[0,0,0],
        [0,0,0],
        [0,0,0]]
    t0 =[[1,0,0],
        [0,1,0],
        [0,0,1]]
    t1 =[[x**2,x*y,x*z],
        [x*y,y**2,y*z],
        [x*z,y*z,z**2]]
    t2= [[0,-z,y],
        [z,0,-x],
        [-y,x,0]]

    for i in range(3):
        for j in range(3):
            m[i][j] = math.cos(theta)*t0[i][j]+(1-math.cos(theta))*t1[i][j]+math.sin(theta)*t2[i][j]
    tmp = [0,0,0]
    for i in range(3):
        for j in range(3):
            tmp[i] += vect[j]*m[j][i]
    if tmp[2] >= 1 or tmp[2] <= -1:
        tmp[0] *= -1
    vect = normalize(tmp)

"""
