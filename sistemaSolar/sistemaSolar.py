from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

n1 = 30
rotation_speed = 1
radius = 2
a = 0
auxMoon_X = [-6, 1, 1]
auxMoon_Y = [-6, 1]



def esfera(u, v, corpo):

    radiusAux = radius
    if corpo == 'lua':
        radiusAux /= 3

    if corpo == 'sol':
        radiusAux *= 1.5

    theta = (u * pi / (n1 - 1)) - (pi / 2)
    phi = (v * 2 * pi) / (n1 - 1)

    x = radiusAux * cos(theta) * cos(phi)
    y = radiusAux * sin(theta)
    z = radiusAux * cos(theta) * sin(phi)

    return x, y, z


def desenha_esfera(corpo='default'):
    rgb = [1, 0, 0]
    if corpo == 'lua':
        rgb = [0.9, 0.9, 1]

    if corpo == 'terra':
        rgb = [0, 0.3, 0.8]

    if corpo == 'sol':
        rgb = [0.9, 0.9, 0.2]

    for i in range(n1):
        glBegin(GL_QUAD_STRIP)
        for j in range(n1):
            glColor3f(rgb[0], rgb[1], rgb[2])
            glVertex3fv(esfera(i, j, corpo))
            glColor3f(rgb[0], rgb[1], rgb[2])
            glVertex3fv(esfera(i - 1, j, corpo))
        glEnd()

def desenha():
    global a, auxMoon

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Sol
    glPushMatrix()
    glTranslate(0, 0, 0)
    glRotatef(a, 0, 0.2, 0)
    desenha_esfera('sol')
    glPopMatrix()

    # Terra
    glPushMatrix()
    glRotatef(a, 0, 0, 1)
    glTranslate(16, 0, 0)
    desenha_esfera('terra')
    glPopMatrix()

    # Lua
    glPushMatrix()
    glRotatef(a, 0, 0, 1)
    glTranslate(10 + (0 if auxMoon_X[2] == 1 else 16) + auxMoon_X[2] * ((auxMoon_X[0] ** 2) / 5), auxMoon_Y[0], 0)
    desenha_esfera('lua')
    glPopMatrix()

    glutSwapBuffers()

    a += rotation_speed

    auxMoon_X[0] += auxMoon_X[1]
    auxMoon_Y[0] += auxMoon_Y[1]

    auxMoon_Y[1] /= 1

    if auxMoon_X[0] >= 6:
        auxMoon_X[1] = -1
        auxMoon_X[2] = -1
    else:
        if auxMoon_X[0] <= -6:
            auxMoon_X[1] = 1
            auxMoon_X[2] = 1

    if auxMoon_Y[0] == 6:
        auxMoon_Y[1] = -1
    else:
        if auxMoon_Y[0] == -6:
            auxMoon_Y[1] = 1


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(1000, 800)
glutCreateWindow("Sistema Solar")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0, 0, 0.01, 1)
gluPerspective(45, 1.3333333, 0.1, 150.0)
glTranslatef(0, 0, -70)
glutTimerFunc(50, timer, 1)
glutMainLoop()

