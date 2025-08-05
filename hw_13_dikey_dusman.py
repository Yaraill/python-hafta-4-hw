import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((800,400))
game_name = pygame.display.set_caption("Dikey Hareket Eden Düşman")
clock = pygame.time.Clock()

player = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player.get_rect(center=(300,260))
player_speed = 5

enemy = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/Fly/Fly1.png").convert_alpha()
enemy_rect = enemy.get_rect(center=(400,200))
enemy_y_speed = 3
enemy_x_speed = 0

sky_surface = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/Sky.png").convert()
ground_surface = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/ground.png").convert()

while True:
    keys = pygame.key.get_pressed() # Tuşa basılı tutarkende gitmesi için 
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    enemy_rect.y += enemy_y_speed
    if enemy_rect.top > 400:
        enemy_rect.x = random.randint(0,800 - enemy_rect.width)
        enemy_rect.y = random.randint(-100,-50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if player_rect.colliderect(enemy_rect):
        print("Game Over")

    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > 800:
        player_rect.right = 800
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > 400:
        player_rect.bottom = 400

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(player,player_rect)
    screen.blit(enemy,enemy_rect)
    pygame.display.update()
    clock.tick(60)