import game_framework
import main_state
from pico2d import *

name = "PauseSate"
image = None

def enter():
    global image
    image = load_image('pause2.png')

def exit():
    global image
    del (image)

def update():
    pass

def draw():
    global image
    clear_canvas()
    main_state.boy.draw()
    main_state.grass.draw()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.pop_state()
        elif event.type == SDL_QUIT:
                game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

def pause():
    pass

def resume():
    pass

