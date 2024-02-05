import pygame
from pygame.locals import *

def get_player_name(screen, clock):
    player_name = ""
    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(430, 560, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    text_surface = font.render(text, True, color)

    width = max(200, text_surface.get_width()+10)
    input_box.w = width

    while True:
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.draw.rect(screen, (255, 255, 255), input_box)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    return text
                elif event.key == K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
                text_surface = font.render(text, True, color)

        width = max(200, text_surface.get_width()+10)
        input_box.w = width

        screen.blit(text_surface, (input_box.x+5, input_box.y+5))
        pygame.display.flip()
        clock.tick(30)
