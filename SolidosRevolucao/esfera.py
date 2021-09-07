from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

n1 = 50
rotation_speed = 2
radius = 2
a = 0


def esfera(u, v):
    theta = (u * pi / (n1 - 1)) - (pi / 2)
    phi = (v * 2 * pi) / (n1 - 1)

    x = radius * cos(theta) * cos(phi)
    y = radius * sin(theta)
    z = radius * cos(theta) * sin(phi)

    return x, y, z


def desenha_esfera():
    glTranslatef(-2.5, 0, 0)
    glRotatef(a, 1, 1, 1)

    for i in range(n1):
        glBegin(GL_QUAD_STRIP)
        for j in range(n1):
            glColor3f((i / n1) - 0.3, 0, 0)
            glVertex3fv(esfera(i, j))
            glColor3f(0, 0, 0)
            glVertex3fv(esfera(i - 1, j))
        glEnd()


def desenha():
    global a

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    desenha_esfera()
    glPopMatrix()

    glutSwapBuffers()

    a += 1


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Esfera")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.4, 0.2, 0, 1)
gluPerspective(45, 800.0 / 600.0, 0.1, 100.0)
glTranslatef(2.5, 0, -7)
glutTimerFunc(50, timer, 1)
glutMainLoop()

