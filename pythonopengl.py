
import pyglet
from pyglet.gl import *
from pyglet.window import mouse
from pyglet.window import key

__author__ = 'Bhupendra Aole'
__version__ = '0.1.0'

window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
                          
vertex_list = pyglet.graphics.vertex_list_indexed(6, [0, 1, 2, 3, 4, 5],
    ('v2i', (100, 100,
             150, 100,
             100, 150,
             150, 150,
             100, 250,
             150, 250)),
    ('c3B', (0, 0, 255, 0, 255, 0, 255,0,0, 255,255,255, 0, 0, 0, 0, 0, 0))
)

@window.event
def on_draw():
    window.clear()
    label.draw()

    vertex_list.draw(pyglet.gl.GL_QUAD_STRIP)

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        for i in range(0,6*2,2):
            y = vertex_list.vertices[i+1:i+2][0]
            vertex_list.vertices[i+1:i+2] = [y+10]
            

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')
        
pyglet.app.run()
