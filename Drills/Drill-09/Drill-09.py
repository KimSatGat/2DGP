from pico2d import *
import random

class smallBall:

    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0 + 25, 800), 599
        self.speed = random.randrange(5, 10)
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if (self.y > 55):
            self.y -= self.speed
class bigBall:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0 + 40, 800), 599
        self.speed = random.randrange(5, 10)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if (self.y > 55):
            self.y -= self.speed
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

smallBall_number = random.randrange(1, 20)
bigBall_number = 20 - smallBall_number

team = [Boy() for i in range(11)]
grass = Grass()
smallBalls = [smallBall() for i in range(smallBall_number)]
bigBalls = [bigBall() for i in range(bigBall_number)]

running = True

# game main loop code
while running:
    handle_events()

    for boy in team:
        boy.update()
    for smallBall in smallBalls:
        smallBall.update()
    for bigBall in bigBalls:
        bigBall.update()

    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()
    for boy in team:
        boy.draw()
    for smallBall in smallBalls:
        smallBall.draw()
    for bigBall in bigBalls:
        bigBall.draw()
    update_canvas()

    delay(0.05)
# finalization code
close_canvas()