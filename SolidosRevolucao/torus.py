from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

n1 = 50  # Não deixa a rosquinha parecendo uma porca
raioMaior = 2
raioMenor = 1
a = 0


def torus(u, v):
    theta = (u * 2 * pi) / (n1 - 1)
    phi = (v * 2 * pi) / (n1 - 1)
    x = (raioMaior + raioMenor * cos(theta)) * cos(phi)
    y = (raioMaior + raioMenor * cos(theta)) * sin(phi)
    z = (raioMenor * sin(theta))

    return x, y, z


def desenha_torus():
    glRotatef(a, 1, 1, 0)

    for i in range(n1):
        glBegin(GL_QUAD_STRIP)
        for j in range(n1):
            glColor3f(i / n1, 0, 0)
            glVertex3fv(torus(i, j))
            glVertex3fv(torus(i - 1, j))
        glEnd()


def desenha():
    global a

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    desenha_torus()
    glPopMatrix()

    glutSwapBuffers()

    a += 1


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Rosquinha")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.4, 0.2, 0, 1)
gluPerspective(45, 800.0 / 600.0, 0.1, 100.0)
glTranslatef(0, 0, -10)
glutTimerFunc(10, timer, 1)
glutMainLoop()

