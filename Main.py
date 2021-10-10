import pygame

pygame.init()
pygame.display.set_mode((400, 400))
pygame.display.update()
pygame.display.set_caption("Snake Game")

game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)

pygame.quit()

