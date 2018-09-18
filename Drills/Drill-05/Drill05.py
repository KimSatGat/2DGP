from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def Move1to2():
    x = 203
    y = 535
    moveX = (132 - x) / 20
    moveY = (243 - y) / 20
    cnt = 0
    frame = 0
    while (cnt < 20):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += moveX
        y += moveY
        cnt = cnt + 1
        delay(0.05)
        get_events()

def Move2to3():
    x = 132
    y = 243
    moveX = (535 - x) / 20
    moveY = (470 - y) / 20
    cnt = 0
    frame = 0
    while (cnt < 20):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += moveX
        y += moveY
        cnt = cnt + 1
        delay(0.05)
        get_events()

def Move3to4():
    x = 535
    y = 470
    moveX = (477 - x) / 20
    moveY = (203 - y) / 20
    cnt = 0
    frame = 0
    while (cnt < 20):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += moveX
        y += moveY
        cnt = cnt + 1
        delay(0.05)
        get_events()

def Move4to5():
    x = 477
    y = 203
    moveX = (715 - x) / 20
    moveY = (136 - y) / 20
    cnt = 0
    frame = 0
    while (cnt < 20):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += moveX
        y += moveY
        cnt = cnt + 1
        delay(0.05)
        get_events()

def Move5to6():
    x = 715
    y = 136
    moveX = (316 - x) / 20
    moveY = (225 - y) / 20
    cnt = 0
    frame = 0
    while (cnt < 20):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += moveX
        y += moveY
        cnt = cnt + 1
        delay(0.05)
        get_events()

def Move6to7():
    x = 316
    y = 225
    moveX = (510 - x) / 20
    moveY = (92 - y) / 20
    cnt = 0
    frame = 0
    while (cnt < 20):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += moveX
        y += moveY
        cnt = cnt + 1
        delay(0.05)
        get_events()

def Move7to8():
    x = 510
    y = 92
    moveX = (692 - x) / 20
    moveY = (518 - y) / 20
    cnt = 0
    frame = 0
    while (cnt < 20):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += moveX
        y += moveY
        cnt = cnt + 1
        delay(0.05)
        get_events()

def Move8to9():
    x = 692
    y = 518
    moveX = (682 - x) / 20
    moveY = (336 - y) / 20
    cnt = 0
    frame = 0
    while (cnt < 20):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += moveX
        y += moveY
        cnt = cnt + 1
        delay(0.05)
        get_events()

def Move9to10():
    x = 682
    y = 336
    moveX = (712 - x) / 20
    moveY = (349 - y) / 20
    cnt = 0
    frame = 0
    while (cnt < 20):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += moveX
        y += moveY
        cnt = cnt + 1
        delay(0.05)
        get_events()

def Move10to1():
    pass


def MoveCheckPoint():
    #Move1to2()
    #Move2to3()
    #Move3to4()
    #Move4to5()
    #Move5to6()
    #Move6to7()
    #Move7to8()
    #Move8to9()
    Move9to10()
    #Move10to1()


while (True):
    MoveCheckPoint()



close_canvas()
