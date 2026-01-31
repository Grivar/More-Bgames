import pygame
from random import randint
from os.path import join

pygame.init()
screen_width, screen_hight = 1280, 720 
screen = pygame.display.set_mode((screen_width, screen_hight))
Icon = pygame.image.load("5games-main/space shooter/images/laser.png")
pygame.display.set_caption('Space Shooter')
pygame.display.set_icon(Icon)
running = True
clock = pygame.time.Clock()

# import an image here
player_surface = pygame.image.load('5games-main/space shooter/images/player.png').convert_alpha()
player_rect = player_surface.get_frect(midbottom = (screen_width / 2, screen_hight -60))
player_direction = pygame.math.Vector2(20,-10)
player_speed = 100

meteor = pygame.image.load('5games-main/space shooter/images/meteor.png').convert_alpha()
meteor_rect = meteor.get_frect(center = (screen_width / 2, screen_hight / 2))

lasor = pygame.image.load('5games-main/space shooter/images/laser.png').convert_alpha()
lasor_rect = lasor.get_frect(bottomleft = (20, screen_hight -20))

star = pygame.image.load('5games-main/space shooter/images/star.png').convert_alpha()
star_position = [(randint(0, screen_width), randint(0, screen_hight)) for i in range(30)]

while running:
    dt = clock.tick() / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            print(event.key)

    
    screen.fill('cadetblue4')
    for pos in star_position:
        screen.blit(star, pos)

    screen.blit(meteor, meteor_rect)
    screen.blit(lasor, lasor_rect)

    if player_rect.right >= screen_width or player_rect.left < 0:
        player_direction.x *= -1
    if player_rect.bottom >= screen_hight or player_rect.top < 0:
        player_direction.y *= -1
    player_rect.center += player_direction * player_speed * dt
    screen.blit(player_surface, player_rect)
    pygame.display.update()



pygame.quit()