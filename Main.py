import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
game_over = False
color = (255, 255, 255)
screen.fill(color)
pygame.display.update()
pygame.display.set_caption("Snake Game")

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


pygame.quit()

