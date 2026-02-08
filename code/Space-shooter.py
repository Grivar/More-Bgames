import pygame
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('5games-main/space shooter/images/player.png').convert_alpha()
        self.rect = self.image.get_frect(center = (screen_width / 2, screen_hight -60))
        self.direction = pygame.Vector2()
        self.speed = 300

        #cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            print(current_time)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            print("GGGGGGGGGGGGGGGGGG")
            self.can_shoot = False
        self.laser_timer()
        

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, screen_width), randint(0, screen_hight)))

# General
pygame.init()
screen_width, screen_hight = 1280, 720 
screen = pygame.display.set_mode((screen_width, screen_hight))
Icon = pygame.image.load("5games-main/space shooter/images/laser.png")
pygame.display.set_caption('Space Shooter')
pygame.display.set_icon(Icon)
running = True
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
star_surf = pygame.image.load('5games-main/space shooter/images/star.png').convert_alpha()
for i in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites)

meteor = pygame.image.load('5games-main/space shooter/images/meteor.png').convert_alpha()
meteor_rect = meteor.get_frect(center = (screen_width / 2, screen_hight / 2))

lasor = pygame.image.load('5games-main/space shooter/images/laser.png').convert_alpha()
lasor_rect = lasor.get_frect(bottomleft = (20, screen_hight -20))

# costom events
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

while running:
    dt = clock.tick() / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            print('YOU GAY!')
    
    all_sprites.update(dt)

    # draw the game
    screen.fill('cadetblue4') 
    all_sprites.draw(screen)

    pygame.display.update()



pygame.quit()