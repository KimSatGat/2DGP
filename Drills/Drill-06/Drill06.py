from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global  running
    global  mouseX, mouseY
    global  x, y
    global  dir
    global  frame

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouseX, mouseY = event.x - 30, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if(SDL_BUTTON_LEFT):
                Move()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def Idle_Right():
        global frame
        global x, y
        character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
        frame = (frame + 1) % 8

def Idle_Left():
    global frame
    global x, y
    character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)
    frame = (frame + 1) % 8

def Move():
    global x, y, mouseX, mouseY
    global dir
    global frame
    if(mouseX - x > 0):
        dir = 1
    else:
        dir = -1
    if(dir > 0):
        moveX = (mouseX - x) / 20
        moveY = (mouseY - y) / 20
        cnt = 0
        frame = 0
        while (cnt < 20):
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
            mouse.draw(mouseX, mouseY)
            update_canvas()
            frame = (frame + 1) % 8
            x += moveX
            y += moveY
            cnt = cnt + 1
            delay(0.05)
            handle_events()
    else:
        moveX = (mouseX - x) / 20
        moveY = (mouseY - y) / 20
        cnt = 0
        frame = 0
        while (cnt < 20):
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
            mouse.draw(mouseX, mouseY)
            update_canvas()
            frame = (frame + 1) % 8
            x += moveX
            y += moveY
            cnt = cnt + 1
            delay(0.05)
            handle_events()

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
mouse = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
mouseX, mouseY = KPU_WIDTH // 2, KPU_HEIGHT // 2
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.draw(mouseX, mouseY)
    Idle_Right()
    update_canvas()



    delay(0.02)
    handle_events()


close_canvas()




