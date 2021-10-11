import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
game_over = False
color = (255, 255, 255)
color_snake = (0, 128, 0)
screen.fill(color)
pygame.display.update()
pygame.display.set_caption("Snake Game")

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        pygame.draw.rect(screen, color_snake, pygame.Rect(200, 200, 10, 10))
    pygame.display.update()

pygame.quit()

