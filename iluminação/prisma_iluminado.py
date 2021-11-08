from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import sys

def calculaNormalFace(v0, v1, v2):
    x = 0
    y = 1
    z = 2

    U = (v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = (v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ((U[y]*V[z]-U[z]*V[y]), (U[z]*V[x]-U[x]*V[z]), (U[x]*V[y]-U[y]*V[x]))
    NLength = math.sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])  # modulo do vetor, tamanho do vetor, teorema de pitagoras
    return (N[x]/NLength, N[y]/NLength, N[z]/NLength)  # normaliza o vetor da normal

def prisma():

    raio = 2
    N = 6  # num de faces
    H = 5  # altura
    pontosBaseBaixo = []
    pontosBaseCima = []
    angulo = (2 * math.pi) / N

    glPushMatrix()
    glTranslatef(0, -2, 0)  # posiciona o prisma
    glRotatef(1, 0, 1, 0)  # roda o prisma
    glRotatef(-60, 1, 0, 0)  # inclinar o prisma

    # Base de baixo
    glBegin(GL_POLYGON)  # desenha um pentagono com preenchimento
    for i in range(0,N):
        x = raio * math.cos(i*angulo)
        y = raio * math.sin(i*angulo)
        pontosBaseBaixo += [ (x,y) ]
        glVertex3f(x, y, 0.0)

    glEnd()

    # Base de cima
    glBegin(GL_POLYGON)  # desenha um pentagono com preenchimento
    for i in range(0,N):
        x = raio * math.cos(i*angulo)
        y = raio * math.sin(i*angulo)
        pontosBaseCima += [ (x,y) ]
        glVertex3f(x, y, H)

    glEnd()

    # LATERAL
    glBegin(GL_QUAD_STRIP) #a cada 6 vertices formam-se 2 retangulos
    for i in range(0,N):

        a = (pontosBaseCima[i][0],pontosBaseCima[i][1],H)
        b = (pontosBaseCima[(i+1)%N][0],pontosBaseCima[(i+1)%N][1],H)
        c = (pontosBaseBaixo[i][0],pontosBaseBaixo[i][1],0.0)
        d = (pontosBaseBaixo[(i+1)%N][0],pontosBaseBaixo[(i+1)%N][1],0.0)

        glNormal3fv(calculaNormalFace(a, b, c))
        glVertex3fv(a)
        glVertex3fv(b)
        
        glVertex3fv(c)
        glVertex3fv(d)

    glEnd()

    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2, 1, 3, 0)
    prisma()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)

def reshape(w,h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Camera Virtual
    #             onde     Pra onde 
    gluLookAt( 10, 0, 0,   0, 0, 0,   0,1,0 )

def init():
    mat_ambient = (0.4, 0.4, 0.0, 1.0) #luz do ambiente, só silhueta, colocar cor mais escura
    mat_diffuse = (1.0, 1.0, 0.0, 1.0) #luz refletida, angulo do cos da normal
    mat_specular = (1.0, 0.5, 0.5, 1.0) #luz branca, brilho
    mat_shininess = (50,)
    light_position = (10, 0, 0)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Prisma")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50, timer, 1)
    init()
    glutMainLoop()

main()
