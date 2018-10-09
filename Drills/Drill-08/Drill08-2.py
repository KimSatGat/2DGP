from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
running = True
pointNumber = 10    #목적지 개수
nextPoint = 1       #목적지 인덱스
frame = 0       #프레임
dir = 0         #방향
countTump = 0
points = [(random.randint(0, 1280), random.randint(0, 1024)) for i in range(pointNumber)]

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def MoveRandomPoints(p1, p2, p3, p4):
    global  countTump
    DetermineDirection(p2,p3)
    for i in range(0, 100 + 1, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2 , KPU_HEIGHT // 2)
        myTump()
        t = i / 100
        characterX = ( (-t**3 + 2*t**2 - t) * p1[0] + (3*t**3 - 5*t**2 + 2) * p2[0] + (-3*t**3 + 4*t**2 + t) * p3[0] + (t**3 - t**2) * p4[0] ) / 2
        characterY = ( (-t**3 + 2*t**2 - t) * p1[1] + (3*t**3 - 5*t**2 + 2) * p2[1] + (-3*t**3 + 4*t**2 + t) * p3[1] + (t**3 - t**2) * p4[1] ) / 2

        MoveAnimation(characterX, characterY)


def myTump():
    global  countTump
    if (countTump > 10):
        countTump = 10
    for j in range(0,countTump + 1):
        positon = points[j]
        character.clip_draw(100, 100, 100, 100, positon[0], positon[1])
def DetermineDirection(p1,p2):
    global dir
    if (p2[0] - p1[0] > 0):
        dir = 1
    else:
        dir = -1
def MoveAnimation(characterX, characterY):
    global frame
    if (dir == 1):
        character.clip_draw(frame * 100, 100, 100, 100, characterX, characterY)
        update_canvas()
        handle_events()
        delay(0.02)
        frame = (frame + 1) % 8
    else:
        character.clip_draw(frame * 100, 0, 100, 100, characterX, characterY)
        update_canvas()
        handle_events()
        delay(0.02)
        frame = (frame + 1) % 8

while running:
    if(nextPoint == 9):
        MoveRandomPoints(points[nextPoint-2], points[nextPoint-1], points[nextPoint], points[0])
        nextPoint = (nextPoint + 1) % pointNumber
    MoveRandomPoints(points[nextPoint-2], points[nextPoint-1], points[nextPoint], points[nextPoint+1])
    nextPoint = (nextPoint + 1) % pointNumber
    countTump = countTump + 1
close_canvas()