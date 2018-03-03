import pygame
import random


class Enemy:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.r = random.randint(10, 20)
        self.color = (random.randint(10, 240), random.randint(10, 240), random.randint(10, 240))
        self.time = 0
        self.num = num

    def update(self, mouse_pos, time):
        x1, y1, r1 = self.x, self.y, self.r
        x2, y2, r2 = mouse_pos[0], mouse_pos[1], 10

        # move
        speed = int((100+random.randint(-70, +80))*time)
        if x1 < x2:
            self.x += speed
        elif x1 > x2:
            self.x -= speed
        if y1 < y2:
            self.y += speed
        elif y1 > y2:
            self.y -= speed

        # check collision
        if ((abs(x1 - x2))**2 + (abs(y1 - y2))**2)**(1/2)+5 <= (r1 + r2):
            global Game
            Game = False

        self.time += time
        if self.time >= Max_time:
            Enemy_list.pop(self.num)
            Enemy_list.append(Enemy(
                random.choice([random.randint(50, max(int(mouse_pos[0]) - 150, 51)),
                               random.randint(min(int(mouse_pos[0]) + 150, width-60), width-40)]),
                random.choice([random.randint(50, max(int(mouse_pos[1]) - 150, 51)),
                               random.randint(min(int(mouse_pos[1]) + 150, height-60), height-40)]), self.num))
            self.time = 0

        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


def draw():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Click to start the game", 1, (100, 100, 255))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.flip()
running, Game, first = True, False, True
clock = pygame.time.Clock()

position = (400, 400)
color = (random.randint(100, 240), random.randint(100, 240), random.randint(100, 240))
Enemy_list = []
Max_time = 3

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not Game:
                Game = True
                Enemy_list = []
            for i in range(20):
                Enemy_list.append(Enemy(
                    random.choice([random.randint(50, max(int(event.pos[0]) - 70, 51)),
                                   random.randint(int(event.pos[0]) + 70, 750)]),
                    random.choice([random.randint(50, max(int(event.pos[1]) - 70, 51)),
                                   random.randint(int(event.pos[1]) + 70, 750)]), i))
        if event.type == pygame.MOUSEMOTION:
            position = event.pos
    time = clock.tick(60)/1000
    if Game:
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, color, (position[0], position[1]), 10)
        for i in Enemy_list:
            i.update(position, time)
    else:
        draw()
    pygame.display.flip()

pygame.quit()
