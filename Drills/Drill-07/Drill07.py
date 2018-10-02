from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
running = True
pointNumber = 10
nextPoint = 1
frame = 0       #프레임
dir = 0         #방향
points = [(random.randint(0, 1280), random.randint(0, 1024)) for i in range(pointNumber)]

def handle_events():
    global  running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def MoveRandomPoints(p1, p2):
    pass
def DetermineDirection(p1,p2):
    pass

def MoveAnimation(characterX, characterY):
    pass

while running:
    handle_events()
    MoveRandomPoints(points[nextPoint-1], points[nextPoint])
    nextPoint = (nextPoint + 1) % pointNumber

close_canvas()