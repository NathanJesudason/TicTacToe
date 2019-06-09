import pygame
import random
from time import sleep

pygame.init()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
B = 0
X = 1
O = 2
tilemap = [
    [B,B,B],
    [B,B,B],
    [B,B,B]
]
rectangle = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]
def init():
    for row in range(3):
        for column in range(3):
            tilemap[row][column] = B
    main()

def main():
    """
    for each row in range(3):
        if ((tilemap[row][0] == O OR X) AND (tilemap[row][1] == O) AND (tilemap[row][2] == O))
    """
    compMove = False
    screen = pygame.display.set_mode((643, 643))
    pygame.display.set_caption('Divine Intellect')
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # This block is executed once for each MOUSEBUTTONDOWN event.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for row in range(3):
                    for column in range(3):
                        if rectangle[row][column].collidepoint(event.pos):
                            if tilemap[row][column] == B:
                                tilemap[row][column] = O
                                compMove = True
            while compMove == True:
                compMove2 = False
                for row in range(3):
                    for column in range(3):
                        if tilemap[row][column] == B:
                            compMove2 = True
                if compMove2:
                    while compMove:
                        ax = random.randint(0,2)
                        ay = random.randint(0,2)
                        if tilemap[ax][ay] == B:
                            tilemap[ax][ay] = X
                            compMove = False
                compMove = False
        #432
        screen.fill(RED)
        pygame.draw.rect(screen, BLACK, pygame.Rect(211,0,5,640))
        pygame.draw.rect(screen, BLACK, pygame.Rect(427,0,5,640))
        pygame.draw.rect(screen, BLACK, pygame.Rect(0,211,640,5))
        pygame.draw.rect(screen, BLACK, pygame.Rect(0,427,640,5)) 
        for row in range(3):
            for column in range(3):
                if tilemap[row][column] == B:
                    rectangle[row][column] = pygame.draw.rect(screen, WHITE, (216*row, 216*column, 211, 211))
                #elif tilemap[row][column] == X:
                    #draw an X
                #pass
                elif tilemap[row][column] == O:
                    rectangle[row][column] = pygame.draw.rect(screen, WHITE, (216*row, 216*column, 211, 211))
                    pygame.draw.circle(screen, BLACK, (((216*row)+108),((216*column)+108)), 100)
                elif tilemap[row][column] == X:
                    rectangle[row][column] = pygame.draw.rect(screen, WHITE, (216*row, 216*column, 211, 211))
                    pygame.draw.circle(screen, RED, (((216*row)+108),((216*column)+108)), 100)
        pygame.display.update()
        clock.tick(30)
        endGame = True
        for row in range(3):
            for column in range(3):
                if tilemap[row][column] == B:
                    endGame = False
        for row in range(3):
            if (((tilemap[row][0] == O) and (tilemap[row][1] == O) and (tilemap[row][2] == O)) or ((tilemap[row][0] == X) and (tilemap[row][1] == X) and (tilemap[row][2] == X))):
                endGame = True
        for column in range (3):
            if (((tilemap[0][column] == O) and (tilemap[1][column] == O) and (tilemap[2][column] == O)) or ((tilemap[0][column] == X) and (tilemap[1][column] == X) and (tilemap[2][column] == X))):
                endGame = True
        if (((tilemap[0][0] == O) and (tilemap[1][1] == O) and (tilemap[2][2] == O)) or ((tilemap[0][0] == X) and (tilemap[1][1] == X) and (tilemap[2][2] == X))):
            endGame = True
        if (((tilemap[2][0] == O) and (tilemap[1][1] == O) and (tilemap[0][2] == O)) or ((tilemap[2][0] == X) and (tilemap[1][1] == X) and (tilemap[0][2] == X))):
            endGame = True
        if endGame:
            sleep(1)
            init()



init()
pygame.quit()


