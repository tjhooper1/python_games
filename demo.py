import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
gameScreen = pygame.display.set_mode((display_width, display_height))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

clock = pygame.time.Clock()
FPS = 15

pygame.display.set_caption("Old snake")


def message_to_screen(msg, type):
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(msg, True, type)
    gameScreen.blit(screen_text, [display_width / 2, display_height / 2])


def our_snake(size_of_block, snakelist):
    for XY in snakelist:
        pygame.draw.rect(gameScreen, green, [XY[0], XY[1], size_of_block, size_of_block])


def gameLoop():
    gameClose = False
    gameOver = False

    size_of_block = 10
    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    randAppleX = round(random.randrange(0, display_width - size_of_block) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - size_of_block) / 10.0) * 10.0

    while not gameClose:
        while gameOver == True:
            gameScreen.fill(white)
            message_to_screen("Game Over. Press SPACE to play again or Q to quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameClose = True
                        gameOver = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameClose = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -size_of_block
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = size_of_block
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -size_of_block
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = size_of_block
                    lead_x_change = 0

            lead_x += lead_x_change
            lead_y += lead_y_change
            if lead_x >= 800 or lead_x < 10 or lead_y >= 600 or lead_y < 0:
                gameOver = True

        gameScreen.fill(white)
        pygame.draw.rect(gameScreen, red, (randAppleX, randAppleY, 10, 10))
        pygame.draw.rect(gameScreen, green, (lead_x, lead_y, 10, 10))
        pygame.display.update()
        snakeList = []
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - size_of_block) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, display_width - size_of_block) / 10.0) * 10.0
            our_snake(size_of_block, snakeList)
        clock.tick(FPS)


    # message_to_screen("You lose", red)
    # pygame.display.update()
    # time.sleep(2)
    pygame.quit()

    quit()


gameLoop()
