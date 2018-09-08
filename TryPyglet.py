import pyglet
import math

window = pyglet.window.Window(fullscreen = True)
label = pyglet.text.Label("Pyg", font_size = 50, x = window.width//2, y = window.height//2, anchor_x = "center", anchor_y = "center")

pig_image = pyglet.image.load("pig2.png")
pig = pyglet.sprite.Sprite(img = pig_image)
pig.scale = 0.02
pig.visible = False

pig_rotation = 90

@window.event
def on_draw():
    window.clear()
    label.draw()
    pig.draw()

@window.event
def on_key_press(symbol, modifiers):
    updates_per_second = 60.0
    pyglet.clock.schedule_interval(update, 1.0/updates_per_second)

def update(dt):
    global pig_rotation
    degrees_per_second = 30.0
    pig_rotation += dt * degrees_per_second
    distance = 200.0
    relative_x = distance * math.cos(deg2rad(pig_rotation))
    relative_y = distance * math.sin(deg2rad(pig_rotation))
    absolute_x = label.x + relative_x
    absolute_y = label.y + relative_y
    pig.update(x = absolute_x, y = absolute_y, rotation = 90-pig_rotation)
    pig.visible = True

def deg2rad(degrees):
    return math.pi * degrees / 180.0

pyglet.app.run()
