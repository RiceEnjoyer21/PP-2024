import pygame 
import sys
import os

pygame.init()

screen_width = 1400
screen_height = 1050

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mikeyclock')
fps = pygame.time.Clock()

angle_1 = 0
angle_2 = 0

_image_library = dict()
def load_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(pygame.transform.scale(load_image("mainclock.png"), (1400, 1050)), (0, 0))

    current_time = pygame.time.get_ticks()

    seconds = current_time // 1000 % 60
    minutes = current_time // 60000 % 60

    seconds_angle = 360 - seconds * 6 
    minutes_angle = 360 - minutes * 6 

    left_arm = pygame.transform.rotate(load_image("leftarm.png"), seconds_angle)
    left_arm_rect = left_arm.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(left_arm, left_arm_rect)

    right_arm = pygame.transform.rotate(load_image("rightarm.png"), minutes_angle)
    right_arm_rect = right_arm.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(right_arm, right_arm_rect)

    pygame.display.flip()

    pygame.display.update()
    fps.tick(60)
