import pygame
from random import randint, uniform

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
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            quit()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(lasor, self.rect.midtop, (all_sprites, laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()

        self.laser_timer()
        
class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, screen_width), randint(0, screen_hight)))

class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)
    
    def update(self, dt):
        self.rect.centery -= 600 * dt
        if self.rect.bottom < 0:
            self.kill()

class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 4000
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(300,400)
    
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

def collitions():
    global running
    collition_sprites = pygame.sprite.spritecollide(player, meteor_sprites, True)
    if collition_sprites:
        running = False

    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()

# General
pygame.init()
screen_width, screen_hight = 1280, 720 
screen = pygame.display.set_mode((screen_width, screen_hight))
Icon = pygame.image.load("5games-main/space shooter/images/laser.png")
pygame.display.set_caption('Space Shooter')
pygame.display.set_icon(Icon)
running = True
clock = pygame.time.Clock()

# import
star_surf = pygame.image.load('5games-main/space shooter/images/star.png').convert_alpha()
meteor = pygame.image.load('5games-main/space shooter/images/meteor.png').convert_alpha()
lasor = pygame.image.load('5games-main/space shooter/images/laser.png').convert_alpha()

# sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
for i in range(30):
    Star(all_sprites, star_surf)
player = Player(all_sprites)


# costom events
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 200)

while running:
    dt = clock.tick() / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            x, y = randint(0, screen_width), randint(-200, -100)
            Meteor(meteor, (x, y), (all_sprites, meteor_sprites))
    
    # updates
    all_sprites.update(dt)

    collitions()

    # draw the game
    screen.fill('cadetblue4') 
    all_sprites.draw(screen)

    pygame.display.update()



pygame.quit()