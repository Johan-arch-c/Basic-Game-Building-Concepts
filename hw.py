import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game Screen")

font = pygame.font.SysFont(None, 48)

text_surface = font.render("Hello, Game World!", True, (255, 255, 255))

rect = pygame.Rect(200, 150, 400, 300)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    pygame.draw.rect(screen, (0, 150, 255), rect)

    screen.blit(text_surface, (250, 50))

    pygame.display.flip()

pygame.quit()
sys.exit()
