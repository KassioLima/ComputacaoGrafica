from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import pi, cos, sin
import sys
import png

# Number of the glut window.
window = 0

# Rotations for cube. 
xrot = yrot = zrot = 0.0
dx = 0
dy = 0
dz = 0

n1 = 50
n2 = 50
r = 1
a = 0

def s(phi):
    return phi/(2*pi)

def t(theta):
    return (theta+(pi/2))/pi

def LoadTextures():
    global texture
    texture = glGenTextures(2) # Gera 2 IDs para as texturas

    ################################################################################
    reader = png.Reader(filename='mapa.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

def InitGL(Width, Height):
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global xrot, yrot, zrot, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0, 0, 0.01, 1.0)
    glTranslatef(0.0, 0.0, -5.0)
    glRotatef(180, 0.0, 1.0, 0.0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(zrot, 0.0, 0.0, 1.0)
    
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_QUAD_STRIP)

    for i in range(0, n1): #theta
        for j in range(0, n2):
            theta = ((pi*i)/(n1-1))-(pi/2)
            phi = 2*pi*j/(n2-1)

            x = r*cos(theta)*cos(phi)
            y = r*sin(theta)
            z = r*cos(theta)*sin(phi)

            glTexCoord2f(s(phi), t(theta))
            glVertex3f(x, y, z)

            theta = ((pi*(i+1))/(n1-1))-(pi/2)
            x = r*cos(theta)*cos(phi)
            y = r*sin(theta)
            z = r*cos(theta)*sin(phi)
            glTexCoord2f(s(phi), t(theta))
            glVertex3f(x, y, z)
    glEnd()   
    
    xrot = xrot + 0.5               # X rotation
    yrot = yrot + 0.5               # Y rotation
    zrot = zrot + 0.1               # Z rotation

    glutSwapBuffers()

def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    # get a 640 x 480 window
    glutInitWindowSize(640, 480)
    
    # the window starts at the upper left corner of the screen
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Globo")

    glutDisplayFunc(DrawGLScene)
    
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(glutPostRedisplay)

    # Initialize our window. 
    InitGL(640, 480)

    # Start Event Processing Engine    
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    main()
