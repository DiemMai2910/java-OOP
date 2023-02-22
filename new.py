import pygame

pygame.init()

WIDTH, HEIGHT = 800, 500

 screen = pygame.display.set_mode((WIDTH, HEIGHT))

GREY = (150, 150, 150)

while True:
    screen.fill(GREY)

    for event in pygame.event.get():
        pass

    pygame.display.flip()
pygame.quit()
