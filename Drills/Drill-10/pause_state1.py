import game_framework
from pico2d import *

name = "PauseSate"
image = None

def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del (image)

def update():
    pass

def draw():
    pass
def handle_events():
    pass

def pause():
    pass

def resume():
    pass

