import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import*

angle = 0.0
scale_factor = 1.0
translate_x = 0.0
translate_y = 0.0

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def draw_square():
    glBegin(GL_POLYGON)
    glVertex2f(-0.1, -0.1)
    glVertex2f(0.1, -0.1)
    glVertex2f(0.1, 0.1)
    glVertex2f(-0.1, 0.1)
    glEnd()

def display():
    global angle, scale_factor, translate_x, translate_y
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(translate_x, translate_y, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)
    glScalef(scale_factor, scale_factor, 1.0)

    glColor3f(0.0, 0.0, 1.0)
    draw_square()
    glutSwapBuffers()

def keyboard(key, x, y):
    global angle, scale_factor, translate_x, translate_y
    if key == b'q' or key == b'Q':
        sys.exit()
    elif key == b'r' or key == b'R':
        angle += 10.0
    elif key == b's' or key == b'S':
        scale_factor += 0.1
    elif key == b't' or key == b'T':
        translate_x += 0.1
    elif key == b'f' or key == b'F':
        translate_x -= 0.1
    elif key == b'g' or key == b'G':
        translate_y += 0.1
    elif key == b'h' or key == b'H':
        translate_y -= 0.1

    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"2D Transformation")
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()