import pygame
from sys import exit
import random

WIDTH = 800
HEIGHT = 400

class Button(): # Butonların oluşturulma fonksiyonu
    def __init__(self,x,y,width,height,text,font,color,hover_color,click_sound=None):
        self.rect = pygame.Rect(x,y,width,height)
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.current_color = self.color
        self.click_sound = click_sound

    def draw(self,surface): # Fare üzerindeyken rengini değiştiren fonksiyon
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color

        pygame.draw.rect(surface, self.current_color, self.rect)
        text_surface = self.font.render(self.text, True, (255,255,255))
        text_rect = text_surface.get_rect(center = self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self,event): # Fare ile butona basma fonksiyonu
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    if self.click_sound:
                        self.click_sound.play()
                    return True

        return False

player_surf = pygame.Surface((50,50))
player_surf.fill((255,0,0))
player_rect = player_surf.get_rect(center = (WIDTH / 2, HEIGHT / 2))
player_speed = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Buton Ses Testi")
test_font = pygame.font.Font("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/font/Pixeltype.ttf", 50) 

sky_surface = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/Sky.png").convert()
ground_surface = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/ground.png").convert()

sound_f_button = pygame.mixer.Sound("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/audio/jump.mp3")
sound_f_button.set_volume(0.2)

button_font = test_font

sound_button = Button( # Sound Butonu
    x=0, y=00 ,
    width=100,height=100,
    text="Sound", font=button_font,
    color=(60,179,113),
    hover_color=(50,150,100),
    click_sound=sound_f_button
) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if sound_button.is_clicked(event):
            print("Butona tıklandı")
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(player_surf, player_rect)
    sound_button.draw(screen)

    pygame.display.update()
    clock.tick(60)

