from pico2d import *
import game_framework
import world_build_state

name = "NameState"
font = None

def enter():
    global font
    font = load_font('ENCR10B.TTF', 20)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)
def update():
    pass

def draw():
    global font
    clear_canvas()
    font.draw(600, 800, 'TEST', (0, 0, 0))
    update_canvas()

def exit():
    pass