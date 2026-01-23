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

# import an image here
player_surface = pygame.image.load('5games-main/space shooter/images/player.png').convert_alpha()
player_rect = player_surface.get_frect(center = (screen_width / 2,screen_hight / 2))

star = pygame.image.load('5games-main/space shooter/images/star.png').convert_alpha()
star_position = [(randint(0, screen_width), randint(0, screen_hight)) for i in range(30)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill('cadetblue4')
    for pos in star_position:
        screen.blit(star, pos)
    screen.blit(player_surface, player_rect)
    pygame.display.update()



pygame.quit()