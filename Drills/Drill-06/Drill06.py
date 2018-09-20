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
            mouseX, mouseY = event.x, KPU_HEIGHT - 1 - event.y
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


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
mouse = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
mouseX, mouseY = KPU_WIDTH // 2, KPU_HEIGHT // 2
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.draw(mouseX, mouseY)
    Idle_Left()
    update_canvas()



    delay(0.02)
    handle_events()


close_canvas()




