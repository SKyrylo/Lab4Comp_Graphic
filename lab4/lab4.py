import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random


def draw_cube(color):
    glBegin(GL_QUADS)
    glColor3fv(color)
    # Front face
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)

    # Back face
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)

    # Right face
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)

    # Left face
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)

    # Top face
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)

    # Bottom face
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    
    glEnd()


def toggle_rotation():
    global angle
    global rotation
    rotation = not rotation
    if angle == 0:
        angle = 2
    else:
        angle = 0


def cube_light():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 1.0, 1.0, 1.0))


def rotation_speed_up():
    global angle
    angle += 1


def rotation_speed_down():
    global angle

    if angle > 1:
        angle -= 1
 

rotation = True

rotation_x = [1, 0, 0]
rotation_y = [0, 1, 0]
current_rotation_axis = rotation_x
angle = 2
figure_color = [random.random(), random.random(), random.random()]


def change_color():
    global figure_color
    figure_color = [random.random(), random.random(), random.random()]


def main():
    global current_rotation_axis, angle

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    cube_light()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    current_rotation_axis = (
                        rotation_y if current_rotation_axis == rotation_x else rotation_x
                    )
                elif event.key == pygame.K_UP:
                    rotation_speed_up()
                elif event.key == pygame.K_DOWN:
                    rotation_speed_down()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_color()
                elif event.button == 3:
                    toggle_rotation()
        if rotation:
            glRotatef(angle, *current_rotation_axis) 

        glRotatef(angle, *current_rotation_axis)  
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        draw_cube(figure_color)
        
        pygame.display.flip()
        pygame.time.wait(10)

        
if __name__ == "__main__":
    main()
