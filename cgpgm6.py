from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
angle = 0
scale = 1.0
scale_direction = 1
translation = [0.0, 0.0, 0.0]
translation_direction = [1, 1, 1]
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
def draw_cube():
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
 global angle, scale, translation
 glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 glLoadIdentity()
 glTranslatef(0.0, 0.0, -10)
 glScalef(scale, scale, scale)
 glTranslatef(*translation)
 glRotatef(angle, 1, 1, 1)
 draw_cube()
 glutSwapBuffers()
 angle += 0.5
def animate():
 global scale, scale_direction, translation, translation_direction
 # Update scale
 scale += 0.01 * scale_direction
 if scale >= 1.5 or scale <= 0.5:
   scale_direction *= -1
 # Update translation
 for i in range(3):
   translation[i] += 0.01 * translation_direction[i]
   if translation[i] >= 1 or translation[i] <= -1:
      translation_direction[i] *= -1
 glutPostRedisplay()
 time.sleep(0.01)
def keyboard(key, x, y):
  if key == b'\x1b': # ESC key
    glutLeaveMainLoop()
def reshape(width, height):
 if height == 0:
    height = 1
 glViewport(0, 0, width, height)
 glMatrixMode(GL_PROJECTION)
 glLoadIdentity()
 gluPerspective(45, width / height, 0.1, 50.0)
 glMatrixMode(GL_MODELVIEW)
 glLoadIdentity()
def main():
 glutInit()
 glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
 glutInitWindowSize(800, 600)
 glutCreateWindow("Cube with Animation")
 glEnable(GL_DEPTH_TEST)
 glutDisplayFunc(display)
 glutIdleFunc(animate)
 glutReshapeFunc(reshape)
 glutKeyboardFunc(keyboard)
 glutMainLoop()
if __name__ == "__main__":
 main()