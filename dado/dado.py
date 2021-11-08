from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import png

# Number of the glut window.
window = 0

# Rotations for cube. 
xrot = yrot = zrot = 0.0
dx = 0
dy = 0
dz = 0

# texture = []

def LoadTextures():
    global texture
    texture = glGenTextures(2) # Gera 2 IDs para as texturas

    ################################################################################
    reader = png.Reader(filename='dado.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist()) #carrega a textura
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

def InitGL(Width, Height):
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global xrot, yrot, zrot, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0,0.1,0.2,1.0)
    glTranslatef(0.0,0.0,-5.0)
    glRotatef(xrot,1.0,0.0,0.0)
    glRotatef(yrot,0.0,1.0,0.0)
    glRotatef(zrot,0.0,0.0,1.0)
    
    glBindTexture(GL_TEXTURE_2D, texture[0]) #escolhe textura 1
    glBegin(GL_QUADS)
    #mapeamento da textura

    #Front Face
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0) #associação do 2d p 3d
    glTexCoord2f(1/3, 0.0 ); glVertex3f( 1.0, -1.0,  1.0)
    glTexCoord2f(1/3, 1/2); glVertex3f( 1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 1/2); glVertex3f(-1.0,  1.0,  1.0)

    #Back Face
    glTexCoord2f(2/3, 1/2); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1/2); glVertex3f(-1.0,  1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)
    glTexCoord2f(2/3, 1.0); glVertex3f( 1.0, -1.0, -1.0)
    
    #Top Face
    glTexCoord2f(1/3, 1/2); glVertex3f(-1.0,  1.0, -1.0)
    glTexCoord2f(2/3, 1/2); glVertex3f(-1.0,  1.0,  1.0)
    glTexCoord2f(2/3, 1); glVertex3f( 1.0,  1.0,  1.0)
    glTexCoord2f(1/3, 1); glVertex3f( 1.0,  1.0, -1.0)

    #Bottom Face       
    glTexCoord2f(1/3, 0.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(2/3, 0.0); glVertex3f( 1.0, -1.0, -1.0)
    glTexCoord2f(2/3, 1/2); glVertex3f( 1.0, -1.0,  1.0)
    glTexCoord2f(1/3, 1/2); glVertex3f(-1.0, -1.0,  1.0)

    #Right face
    glTexCoord2f(0.0, 1/2); glVertex3f( 1.0, -1.0, -1.0)
    glTexCoord2f(1/3, 1/2); glVertex3f( 1.0,  1.0, -1.0)
    glTexCoord2f(1/3, 1.0); glVertex3f( 1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, -1.0,  1.0)
    
    #Left Face
    glTexCoord2f(2/3, 0.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 1/2); glVertex3f(-1.0,  1.0,  1.0)
    glTexCoord2f(2/3, 1/2); glVertex3f(-1.0,  1.0, -1.0)

    glEnd()                #Done Drawing The Cube
    
    xrot = xrot + 0.05                # X rotation
    yrot = yrot + 0.01                 # Y rotation
    zrot = zrot + 0.01                 # Z rotation

    glutSwapBuffers()

def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    # get a 640 x 480 window 
    glutInitWindowSize(640, 480)
    
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Dado")

    glutDisplayFunc(DrawGLScene)
    
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(glutPostRedisplay) #sempre q o processador estiver de bobs re-desenha a cena

    # Initialize our window. 
    InitGL(640, 480)

    # Start Event Processing Engine    
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    main()
