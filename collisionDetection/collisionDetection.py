import pygame
import sys
import random

from pygame.locals import *

# Set up pygame
pygame.init()
mainClock = pygame.time.Clock() # 可以对于任何计算机都暂停适当的时间。

# Set up the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection')

# Set up the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Set up the player and food data structures.
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50) #先位置（左上角的XY坐标），都大小
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE),
                             FOODSIZE, FOODSIZE))
    #坐标减去一份FOODSIZE，是因为又可能会把食物方块推到了窗口之外

# Set up movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False


MOVESPEED = 6

# Run the game loop
while True:
    # Check for event.
    for event in pygame.event.get():
        if event.type == QUIT:  # 当用户关闭窗口时触发的事件
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:  # 当用户按下键盘时触发的事件， 还有一个mod属性来表明是否有Shift、Ctrl、Alt或其他的键和该键
                                    # 同时按下
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = True
                moveLeft = False
            if event.key == K_UP or event.key == K_w:
                moveUp = True
                moveDown = False
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:  # 当用户释放一个按键时触发的事件
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)

            if event.type == MOUSEBUTTONUP:
                foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

        foodCounter += 1
        if foodCounter >= NEWFOOD: # 自动新增食物的频率
            # Add new food.
            foodCounter = 0
            foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),
                                     random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

        # Draw the white background onto the surface.
        windowSurface.fill(WHITE)

        # Move the player
        if moveDown and player.bottom < WINDOWHEIGHT:
            player.top += MOVESPEED
        if moveUp and player.top > 0:
            player.top -= MOVESPEED
        if moveLeft and player.left > 0:
            player.left -= MOVESPEED
        if moveRight and player.right < WINDOWWIDTH:
            player.right += MOVESPEED

        # Draw the player onto the surface
        pygame.draw.rect(windowSurface, BLACK, player)

        # Check whether the player has intersected with any food squares.
        for food in foods[:]:  # food[:]复制列表的一种更为简便的方法
            if player.colliderect(food): # pyganme.Rect对象的colliderect（）碰撞检测方法
                foods.remove(food)
        # 如果对列表的一个副本进行迭代，那么向原始列表中添加元素或从中删除元素都不是问题

        # Draw the food.
        for i in range(len(foods)):
            pygame.draw.rect(windowSurface, GREEN, foods[i])


        # Draw the window onto the screen.
        pygame.display.update()
        mainClock.tick(40)




