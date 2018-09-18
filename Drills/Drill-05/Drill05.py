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
    pass

def Move4to5():
    pass

def Move5to6():
    pass

def Move6to7():
    pass

def Move7to8():
    pass

def Move8to9():
    pass

def Move9to10():
    pass

def Move10to1():
    pass


def MoveCheckPoint():
    #Move1to2()
    Move2to3()
    #Move3to4()
    #Move4to5()
    #Move5to6()
    #Move6to7()
    #Move7to8()
    #Move8to9()
    #Move9to10()
    #Move10to1()


while (True):
    MoveCheckPoint()



close_canvas()
