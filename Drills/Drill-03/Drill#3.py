import os
import math
from pico2d import *
os.chdir('C:\\Users\\김병완\\Desktop\\EClass\\18년2학기\\2D게임프로그래밍\\2018-2DGP-master\\2018-2DGP-master\\Labs\\Lecture03')
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
x = 400
y = 90
r = 0
rad = 0


while(True):
    
    #사각형 운동
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y+2
        delay(0.01)

    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x-2
        delay(0.01)

    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y-2
        delay(0.01)

    while(x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x+2
        delay(0.01)


    #원 운동
    while(r<180):    
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400+x,300+y)
        x = math.cos(math.radians(rad)) * 220
        y = math.sin(math.radians(rad)) * 220
        rad = rad+2
        r = r+1
        delay(0.01)
        
close_canvas()
