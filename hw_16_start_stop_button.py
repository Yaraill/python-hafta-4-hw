import pygame
import sys
import random

WIDTH = 800
HEIGHT = 400

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/Player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/Player/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk_1,player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/Player/jump.png").convert_alpha() 

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0
        self.speed = 7.5

        self.jump_sound = pygame.mixer.Sound("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/audio/jump.mp3")
        self.jump_sound.set_volume(0.1)

    def player_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            self.gravity = 0    

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 300:
            self.gravity = -20
            self.jump_sound.play()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def animation_state(self):
        if self.rect.bottom < 300: 
            self.image = self.player_jump
        else: 
            self.player_index += 0.1 
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.player_gravity()
        self.animation_state()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        fly_1 = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/Fly/Fly1.png").convert_alpha()
        fly_2 = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/Fly/Fly2.png").convert_alpha()
        self.frames = [fly_1,fly_2]
        random_y_pos = random.randint(150,275)
        self.animation_index = 0
        self.passed_player = False
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(WIDTH+50,WIDTH+175),random_y_pos))
        self.speed = random.randint(3,7)

    def enemy_animation(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.right <= 0:
            self.kill()

    def update(self):
        self.enemy_animation()
        self.rect.x -= self.speed
        self.destroy()

class Button(): # Butonların oluşturulma fonksiyonu
    def __init__(self,x,y,width,height,text,font,color,hover_color):
        self.rect = pygame.Rect(x,y,width,height)
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.current_color = self.color

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
                    return True
        return False

def display_score():
    global score
    score_surf = test_font.render(f"Score: {int(score)}",True,(255,0,128))
    score_rect = score_surf.get_rect(center = (WIDTH/2, 50))
    screen.blit(score_surf,score_rect)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_name = pygame.display.set_caption("Düşmanla Çarpışma")

sky_surface = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/Sky.png").convert()
ground_surface = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/ground.png").convert()

test_font = pygame.font.Font("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/font/Pixeltype.ttf", 50)

player_stand = pygame.image.load("C:/Kodlama/witcher5_demo/UltimatePygameIntro-main/graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2) 
player_stand_rect = player_stand.get_rect(center = (400,200)) 

game_title_surface = test_font.render("Witcher 5",False,(111,196,169))
game_title_rect = game_title_surface.get_rect(center = (400,80)) 

start_message_surface = test_font.render("Press space to run",False,(111,196,169))
start_message_rect = start_message_surface.get_rect(center = (400,330))

button_font = test_font

start_button = Button( # Start Butonu
    x=75, y=HEIGHT // 2 ,
    width=200,height=50,
    text="Start Game", font=button_font,
    color=(60,179,113),
    hover_color=(50,150,100)
) 
exit_button = Button( # Çıkış Butonu
    x=550, y=HEIGHT // 2 ,
    width=200,height=50,
    text="Finish Game", font=button_font,
    color=(220,20,60),
    hover_color=(180,15,50)
)

score = 0

player = pygame.sprite.GroupSingle()
player.add(Player())

enemy = pygame.sprite.Group()

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1500)
game_active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == enemy_timer:
                enemy.add(Enemy())

        else: 
            if start_button.is_clicked(event) :
                game_active = True 
                score = 0 
                enemy.empty() 
                
                current_enemy_spawn_interval = 1500 
                pygame.time.set_timer(enemy_timer, current_enemy_spawn_interval) 
                
                player.sprite.rect.midbottom = (80, 300) 
                player.sprite.gravity = 0

            if exit_button.is_clicked(event):
                pygame.quit()
                sys.exit()

    if game_active:
        collided_enemies = pygame.sprite.spritecollide(player.sprite,enemy,True)
        if collided_enemies:
            game_active = False

        for current_enemy in enemy:
            if current_enemy.rect.right < player.sprite.rect.left and not current_enemy.passed_player:
                score += 1
                current_enemy.passed_player = True
    
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))

        player.draw(screen)
        player.update()

        enemy.draw(screen)
        enemy.update()

        display_score()

    else:
        screen.fill((94,129,162)) 

        screen.blit(player_stand, player_stand_rect) 
        screen.blit(game_title_surface, game_title_rect) 

        start_button.draw(screen)
        exit_button.draw(screen)

        # if score == 0: 
        #     screen.blit(start_message_surface, start_message_rect) 
        # else: 
        #     final_score_message = test_font.render(f"Score: {int(score)}", False, (111, 196, 169))
        #     final_score_message_rect = final_score_message.get_rect(center=(400, 330))
        #     screen.blit(final_score_message,final_score_message_rect)

    pygame.display.update()
    clock.tick(60)



