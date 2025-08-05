import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
game_name = pygame.display.set_caption("Çarpmayla Skor Arttırma Oyunu")

player = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player.get_rect(center=(300,260))
player_speed = 5

enemy = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/Fly/Fly1.png").convert_alpha()
enemy_rect = enemy.get_rect(center=(random.randint(0, 800), random.randint(-100, -50)))
enemy_speed = 3

sky_surface = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/Sky.png").convert()
ground_surface = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/ground.png").convert()

test_font = pygame.font.Font("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/font/Pixeltype.ttf", 50)

game_active = True
score = 0

while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    score_surf = test_font.render(f"Skor: {score}", True, "Red")
    score_rect = score_surf.get_rect(center=(400, 50))


    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        if player_rect.left < 0:
            player_rect.left = 0
        if player_rect.right > 800:
            player_rect.right = 800
        if player_rect.top < 0:
            player_rect.top = 0
        if player_rect.bottom > 400: 
            player_rect.bottom = 400

        enemy_rect.y += enemy_speed

        if enemy_rect.top > 400: # Ekran yüksekliği 400
            enemy_rect.x = random.randint(0, 800 - enemy_rect.width)
            enemy_rect.y = random.randint(-100, -50)

    if player_rect.colliderect(enemy_rect):
        score += 1
        enemy_rect.x = random.randint(0, 800 - enemy_rect.width)
        enemy_rect.y = random.randint(-100, -50)

    screen.blit(score_surf, score_rect)
    screen.blit(player,player_rect)
    screen.blit(enemy,enemy_rect)
    pygame.display.update()
    clock.tick(60)