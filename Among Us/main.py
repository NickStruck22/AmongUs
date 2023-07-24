import pygame, sys
import amogus as a
import pkm
import asteroid
from pygame.locals import *

pygame.init()
FPS = 30 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
SIRINAEKRANA = 800
VISINAEKRANA = 600

FONT = pygame.font.Font('freesansbold.ttf', 32)
terminalPopup = FONT.render('Press E to access terminal', True, RED)
terminalRect = terminalPopup.get_rect()

pkmSePrikazuje = False
asteroidSePrikazuje = False

pkmGame = pkm.Pkm()
asteroidGame = asteroid.AsteroidGame()

def main():
    global pkmSePrikazuje, asteroidSePrikazuje
    screen = pygame.display.set_mode((SIRINAEKRANA, VISINAEKRANA))
    
    pygame.display.set_caption('Amogus')
    fpsClock = pygame.time.Clock() 
    
    mapImg = pygame.image.load('map.png')

    amogus = a.Amogus()

    while True:
        screen.fill(WHITE)        
        
        checkQuit()
        #lokacijaKlika(amogus)                       #ovo je koristeno za trazenje tacaka poligona zidova
        if(pkmSePrikazuje):     # ovde igramo papir kamen makaze
            if(not pkmGame.igraj()):       # kada igraj vrati True main zna da je igra gotova i da ne treba vise da je prikazuje
                pkmSePrikazuje = False
            screen.blit(mapImg, (SIRINAEKRANA/2 - amogus.image.get_width()/2 - mapImg.get_width()/2 - amogus.x, VISINAEKRANA/2 - amogus.image.get_height()/2 - mapImg.get_height()/2 - amogus.y))
            pkmGame.drawPkm(screen, fpsClock, FPS);
        elif(asteroidSePrikazuje):  # ovde igramo asteroid igru
            if(not asteroidGame.igraj()):   # kada igraj vrati True main zna da je igra gotova i da ne treba vise da je prikazuje
                asteroidSePrikazuje = False
            screen.blit(mapImg, (SIRINAEKRANA/2 - amogus.image.get_width()/2 - mapImg.get_width()/2 - amogus.x, VISINAEKRANA/2 - amogus.image.get_height()/2 - mapImg.get_height()/2 - amogus.y))
            asteroidGame.draw(screen, fpsClock, FPS)
        else:       # ovde kontrolisemo amogusa, pomeramo mapu i proveravamo da li smo dosli do terminala
            amogus.checkInput()
            screen.blit(mapImg, (SIRINAEKRANA/2 - amogus.image.get_width()/2 - mapImg.get_width()/2 - amogus.x, VISINAEKRANA/2 - amogus.image.get_height()/2 - mapImg.get_height()/2 - amogus.y))
            if(pkmGame.won == False):
                pkmTerminalDetection(amogus, screen)
            if(asteroidGame.won == False):
                asteroidTerminalDetection(amogus, screen)
            amogus.draw(screen)
            

        pygame.display.update()
        fpsClock.tick(FPS)


def pkmTerminalDetection(amogus, screen):
    global pkmSePrikazuje
    rectWidth, rectHeight = (145.0 - 45.0, -425.0 + 540)
    rect = pygame.Rect(45.0, -540.0, rectWidth, rectHeight)
    
    pkmTermRect = pygame.Rect(SIRINAEKRANA/2-amogus.x + 45, VISINAEKRANA/2-amogus.y - 540, rectWidth, rectHeight) # crtanje terminal recta, mora da bude pomeren za pola ekrana-amogus pozicija
    pygame.draw.rect(screen, RED, pkmTermRect)
    
    if(rect.collidepoint(amogus.x, amogus.y)):
        terminalRect.topleft = (50, VISINAEKRANA - 35)  # ispisujemo popup text koji nas podseca da pritisnemo E
        screen.blit(terminalPopup, terminalRect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            pkmSePrikazuje = True

def asteroidTerminalDetection(amogus, screen):
    global asteroidSePrikazuje
    rectWidth, rectHeight = (75.0 + 70.0, 975 - 815)
    rect = pygame.Rect(-70.0, -975.0, rectWidth, rectHeight)

    asteroidTermRect = pygame.Rect(SIRINAEKRANA/2-amogus.x - 70, VISINAEKRANA/2-amogus.y - 975, rectWidth, rectHeight)
    pygame.draw.rect(screen, RED, asteroidTermRect)

    if(rect.collidepoint(amogus.x, amogus.y)):
        terminalRect.topleft = (50, VISINAEKRANA - 35)
        screen.blit(terminalPopup, terminalRect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            asteroidSePrikazuje = True

def lokacijaKlika(amogus):
    for event in pygame.event.get(MOUSEBUTTONDOWN):
            x, y = event.pos
            x = amogus.x + x - SIRINAEKRANA/2
            y = amogus.y + y - VISINAEKRANA/2
            if x%5 >=3:
                x += 5 - x%5
            else:
                x -= x%5
            if x%5 >=3:
                y += 5 - y%5
            else:
                y -= y%5
            if(x >= 0 and  y >= 0):
                print('(x+' + str(x) + ', y+' + str(y) + '), ')    
            elif(x < 0 and  y >= 0):
                print('(x' + str(x) + ', y+' + str(y) + '), ')
            elif(x >= 0 and y < 0):
                print('(x+' + str(x) + ', y' + str(y) + '), ')
            elif(x < 0 and y <  0):
                print('(x' + str(x) + ', y' + str(y) + '), ')

def terminate():
    pygame.quit()
    sys.exit()

def checkQuit():
    for event in pygame.event.get(QUIT): 
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)

if __name__ == '__main__':
    main()