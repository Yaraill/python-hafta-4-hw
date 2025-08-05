import pygame
import sys

# --- Renkler ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255) 
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

screen = pygame.display.set_mode((600,400))
game_name = pygame.display.set_caption("Oyun İsmi")
clock = pygame.time.Clock()
screen.fill((YELLOW))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.flip() # Ekrandaki değişiklikleri ekrana yansıtan kod satırı
    clock.tick(60)

