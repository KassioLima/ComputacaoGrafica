from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

a = 0  # vai controlar o angulo da piramide em torno do eixo do y

cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5), (0.8, 0.8, 0.9))


def prisma():
    raio = 2
    N = 6  # Lados
    H = 4  # Altura
    pontosBaseBaixo = []
    pontosBaseCima = []
    angulo = (2 * math.pi) / N

    glPushMatrix()
    glTranslatef(0, -2, -3)  # posiciona o prisma
    glRotatef(a, 0, 1, 0)  # roda o prisma
    glRotatef(-60, 1, 0, 0)  # inclinar o prisma

    # Base de cima
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, N):
        x = raio * math.cos(i * angulo)  # * 0 para formar uma pirâmide
        y = raio * math.sin(i * angulo)  # * 0 para formar uma pirâmide
        pontosBaseCima += [(x, y)]
        glVertex3f(x, y, H)
        glColor3fv(cores[(i) % len(cores)])
    glEnd()

    # Base de baixo
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, N):
        x = raio * math.cos(i * angulo)
        y = raio * math.sin(i * angulo)
        pontosBaseBaixo += [(x, y)]
        glVertex3f(x, y, 0)
        glColor3fv(cores[(i) % len(cores)])
    glEnd()

    # Lados
    glBegin(GL_QUAD_STRIP)
    for i in range(0, N):

        glVertex3f(pontosBaseCima[i][0], pontosBaseCima[i][1], H)
        glVertex3f(pontosBaseBaixo[i][0], pontosBaseBaixo[i][1], 0.0)
        glColor3fv(cores[i % len(cores)])

        glVertex3f(pontosBaseCima[(i + 1) % N][0], pontosBaseCima[(i + 1) % N][1], H)
        glVertex3f(pontosBaseBaixo[(i + 1) % N][0], pontosBaseBaixo[(i + 1) % N][1], 0.0)
        glColor3fv(cores[i % len(cores)])

    glEnd()

    glPopMatrix()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    prisma()
    a += 1
    glutSwapBuffers()


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("PRISMA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0, 0.1, 0.125, 1)
gluPerspective(45, 800.0 / 600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -10)
glutTimerFunc(10, timer, 1)
glutMainLoop()
