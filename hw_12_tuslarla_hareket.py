import pygame
import sys

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
game_name = pygame.display.set_caption("Tuşlarla Hareket Eden Kutu")

kutu = pygame.Surface((50,50))
kutu_rect = kutu.get_rect()
kutu_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
kutu.fill((255,0,0))
kutu_speed = 10

while True:
    screen.fill((64,64,64))

    keys = pygame.key.get_pressed() # Tuşa basılı tutarkende gitmesi için 
    if keys[pygame.K_LEFT]:
        kutu_rect.x -= kutu_speed
    if keys[pygame.K_RIGHT]:
        kutu_rect.x += kutu_speed
    if keys[pygame.K_UP]:
        kutu_rect.y -= kutu_speed
    if keys[pygame.K_DOWN]:
        kutu_rect.y += kutu_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.KEYDOWN: # Tuşa basıldığında tek tek gitmesi için
        #     if event.key == pygame.K_LEFT:
        #         kutu_rect.x -= kutu_speed 
        #     if event.key == pygame.K_RIGHT:
        #         kutu_rect.x += kutu_speed
        #     if event.key == pygame.K_UP:
        #         kutu_rect.y -= kutu_speed
        #     if event.key == pygame.K_DOWN:
        #         kutu_rect.y += kutu_speed
        
    if kutu_rect.left < 0:
        kutu_rect.left = 0
    if kutu_rect.right > screen.get_width():
        kutu_rect.right = screen.get_width()
    if kutu_rect.top < 0:
        kutu_rect.top = 0
    if kutu_rect.bottom > screen.get_height():
        kutu_rect.bottom = screen.get_height()



    screen.blit(kutu,kutu_rect)
    pygame.display.flip()
    clock.tick(60)


