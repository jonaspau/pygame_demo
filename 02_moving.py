# Top Chunk
import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Pygame Shapes")

# Chunk 01
# while True:
    # surface.fill((0,0,0))
    # pygame.draw.rect(surface, (255,0,0), (random.randint(
    # 0, windowWidth), random.randint(0, windowHeight), 10, 10))

# Chunk 02
# greenSquareX = windowWidth / 2
# greenSquareY = windowHeight / 2

# while True:
#     surface.fill((0, 0, 0))
#     pygame.draw.rect(surface, (0, 255, 0),
#                      (greenSquareX, greenSquareY, 10, 10))
#     greenSquareX += 1
#     greenSquareY += 1
    
# Chunk 03
# blueSquareX = 0.0
# blueSquareY = 0.0
# blueSquareVX = 8
# blueSquareVY = 8

# while True:
#    surface.fill((0, 0, 0))
#     pygame.draw.rect(surface, (0, 0, 255),
#                      (blueSquareX, blueSquareY, 10, 10))
#     blueSquareX += blueSquareVX
#     blueSquareY += blueSquareVY
#     blueSquareVX -= 0.2
#     blueSquareVY += 0.1

# Chunk 04
# rectX = windowWidth / 2
# rectY = windowHeight / 2
# rectWidth = 50
# rectHeight = 50

# while True:
#     surface.fill((0, 0, 0))
#     pygame.draw.rect(surface, (255, 255, 0),
#                      (rectX - rectWidth / 2, rectY - rectHeight / 2,rectWidth, rectHeight))
#     rectWidth += 1
#     rectHeight += 1

# Chunk 05
squaresRed = random.randint(0, 255)
squaresBlue = random.randint(0, 255)
squaresGreen = random.randint(0, 255)

while True:
    surface.fill((0, 0, 0))
    pygame.draw.rect(surface, (squaresRed, squaresGreen, squaresBlue),
                     (50, 50, windowWidth / 2, windowHeight / 2))
    if squaresRed >= 255:
        squaresRed = random.randint(0, 255)
    else:
        squaresRed += 1
    if squaresGreen >= 255:
        squaresGreen = random.randint(0, 255)
    else:
        squaresGreen += 1
    if squaresBlue >= 255:
        squaresBlue = random.randint(0, 255)
    else:
        squaresBlue += 1



# Bottom
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()