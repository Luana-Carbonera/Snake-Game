import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
game_over = False
color = (255, 255, 255)
color_snake = (0, 128, 0)
x1 = 200
y1 = 200
x = 0
y = 0
clock = pygame.time.Clock()
screen.fill(color)
pygame.display.update()
pygame.display.set_caption("Snake Game")

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = -10
                x = 0
            elif event.key == pygame.K_DOWN:
                y = 10
                x = 0
            elif event.key == pygame.K_LEFT:
                x = -10
                y = 0
            elif event.key == pygame.K_RIGHT:
                x = 10
                y = 0


    x1 += x
    y1 += y
    screen.fill(color)

    pygame.draw.rect(screen, color_snake, pygame.Rect(x1, y1, 10, 10))
    pygame.display.update()
    clock.tick(15)

pygame.quit()