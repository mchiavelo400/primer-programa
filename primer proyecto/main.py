import pygame
import events

pygame.init()

width = 1000
heigth = 1000
image = pygame.image.load('Cubo 3D minimalista en escala de grises.png')
cubo = pygame.transform.scale(image, (100,100))
window = pygame.display.set_mode((width,heigth))
pygame.display.set_caption("prueba 1")
time = pygame.time.Clock()

x = 350
y = 350
speed = 10

run=True
while run:
    time.tick(60)
    a,w,s,d = events.teclas()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if a:
        x -= speed
    if w:
        y -= speed
    if s:
        y += speed
    if d:
        x += speed
    window.fill((0,0,0))
    window.blit(cubo, (x,y))
    pygame.display.flip()

pygame.quit()
