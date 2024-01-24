import pygame
import pickle
from math import *
import math
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)

pygame.init()
 
# Set the width and height of the screen [width, height]
WIDTH = 1900
HEIGHT = 1000
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Physics : Chapter 7")
running = True
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
file = open('data', 'rb')
data = pickle.load(file)

f = int(data[0])
AB = int(data[1])
OA = int(data[2])
scale = int(data[3])
OA2 = (f*-OA)//(f-OA)
gamma = OA2 / OA
AB2 = AB * gamma
Af = OA - f
x = (math.tan((90 - math.acos(Af/math.sqrt(AB**(2) + Af**(2))) * 180/math.pi)/180*math.pi))* AB2
Af2 = OA2 - f
x2 = (math.tan((90 - math.acos(Af2/math.sqrt(AB2**(2) + Af2**(2))) * 180/math.pi)/180*math.pi))* AB


print("values down below are already scaled : ")
print("f' : ", f*scale)
print("AB' : ", AB*scale)
print("A'B' : ", AB2*scale)
print("OA : ", OA*scale)
print("OA' : ", OA2*scale)
print("gamma : ", gamma*scale)
print("vergence : ", (1/f*scale))


def regle2et3():
    
    pygame.draw.line(screen, YELLOW, (WIDTH//2 - OA,HEIGHT//2 - AB), (WIDTH//2 - f ,HEIGHT//2), 4) 
    pygame.draw.line(screen, YELLOW, (WIDTH//2 - f ,HEIGHT//2), (WIDTH//2 - f + x,HEIGHT//2 + AB2), 4) 
    pygame.draw.line(screen, YELLOW, (WIDTH//2 - f + x,HEIGHT//2 + AB2), (WIDTH//2 +OA ,HEIGHT//2 + AB2), 4) 
    
    pygame.draw.line(screen, YELLOW, (WIDTH//2 + OA2,HEIGHT//2 + AB2), (WIDTH//2 + f ,HEIGHT//2), 4) 
    pygame.draw.line(screen, YELLOW, (WIDTH//2 + f ,HEIGHT//2), (WIDTH//2 + f - x2,HEIGHT//2 - AB), 4) 
    pygame.draw.line(screen, YELLOW, (WIDTH//2 + f - x2,HEIGHT//2 - AB), (WIDTH//2 -OA2 ,HEIGHT//2 - AB), 4) 
    


while running:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            click = True
            pos = pygame.mouse.get_pos()
    
    
    screen.fill(BLACK)
    
    
    pygame.draw.line(screen, WHITE, (0, HEIGHT//2), (WIDTH, HEIGHT//2),3) #axe optique
    pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT),5)  #lentille convergente
    pygame.draw.line(screen, GREEN, (WIDTH//2 - OA,HEIGHT//2), (WIDTH//2 - OA,HEIGHT//2 - AB), 2) #foyer objet AB
    pygame.draw.line(screen, WHITE, (WIDTH//2 - f,HEIGHT//2 - 20), (WIDTH//2 - f,HEIGHT//2 + 20), 4) #OF = f' 
    pygame.draw.line(screen, WHITE, (WIDTH//2 + f,HEIGHT//2 - 20), (WIDTH//2 + f,HEIGHT//2 + 20), 4) #OF' = f'
    pygame.draw.line(screen, RED, (WIDTH//2 + OA2,HEIGHT//2), (WIDTH//2 + OA2,HEIGHT//2 + AB2), 4) #foyer image A'B'
    
    pygame.draw.line(screen, YELLOW, (WIDTH//2 - OA,HEIGHT//2 - AB), (WIDTH//2 + OA2,HEIGHT//2 + AB2), 4) #1ere regle
    regle2et3()
    
    
    pygame.display.flip()
    click = False
    clock.tick(60)
    

pygame.quit()