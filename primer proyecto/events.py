import pygame

def teclas():
    key = pygame.key.get_pressed()
    a = key[pygame.K_a]
    w = key[pygame.K_w]
    s = key[pygame.K_s]
    d = key[pygame.K_d]
    return a,w,s,d
