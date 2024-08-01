from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*
def init():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,100,0,100)
    glClearColor(1.0,1.0,1.0,1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    
def draw():
    glColor3f(0.0,1.0,0.0)
    glPointSize(10.0)
    glBegin(GL_POLYGON)
    glVertex2i(10,20)
  
    glVertex2i(80,20)

    glVertex2i(80,60)
  
    glVertex2i(10,60)
  
    glEnd()
    glFlush()
  
    
def main():
    glutInit()
    glutInitWindowSize(500,500)
    glutCreateWindow("OpenGL Window")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()