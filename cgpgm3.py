from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

vertices = (
 (1, -1, -1),
 (1, 1, -1),
 (-1, 1, -1),
 (-1, -1, -1),
 (1, -1, 1),
 (1, 1, 1),
 (-1, -1, 1),
 (-1, 1, 1)
)
edges = (
 (0, 1),
 (1, 2),
 (2, 3),
 (3, 0),
 (4, 5),
 (5, 6),
 (6, 7),
 (7, 4),
 (0, 4),
 (1, 5),
 (2, 6),
 (3, 7)
)
surfaces = (
 (0, 1, 2, 3),
 (3, 2, 7, 6),
 (6, 7, 5, 4),
(4, 5, 1, 0),
 (1, 5, 7, 2),
 (4, 0, 3, 6)
)
colors = (
 (1, 0, 0),
 (0, 1, 0),
 (0, 0, 1),
 (1, 1, 0),
 (1, 0, 1),
 (0, 1, 1)
)
def Cube():
 glBegin(GL_QUADS)
 for i, surface in enumerate(surfaces):
     glColor3fv(colors[i])
     for vertex in surface:
         glVertex3fv(vertices[vertex])
 glEnd()
 glBegin(GL_LINES)
 glColor3fv((0, 0, 0))
 for edge in edges:
     for vertex in edge:
         glVertex3fv(vertices[vertex])
 glEnd()
def display():
 glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 glRotatef(1, 3, 1, 1)
 Cube()
 glutSwapBuffers()
def timer(value):
 glutPostRedisplay()
 glutTimerFunc(10, timer, 0)
def main():
 glutInit()
 glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
 glutInitWindowSize(800, 600)
 glutCreateWindow("Rotating Cube")
 glEnable(GL_DEPTH_TEST)
 gluPerspective(45, (800 / 600), 0.1, 50.0)
 glTranslatef(0.0, 0.0, -5)
 glutDisplayFunc(display)
 glutTimerFunc(10, timer, 0)
 glutMainLoop()
if __name__ == "__main__":
 main()