import random
import json
import pickle
import os

from pico2d import *
import game_framework
import world_build_state
import main_state
name = "NameState"
font = None
final_rank = None
def enter():
    global font
    global final_rank
    with open('rank_data.json', 'rt') as f:
        final_rank = json.load(f)
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
    global final_rank
    clear_canvas()
    for a in range(0,10):
        font.draw(600, 800 - (a * 30),'#%d. ' %(a+1), (0, 0, 0))
        font.draw(660, 800 - (a * 30), '%.2f'  % (final_rank[a]), (0, 0, 0))

    update_canvas()

def exit():
    pass