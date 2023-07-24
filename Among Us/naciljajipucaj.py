import sys, pygame, random
from pygame.locals import *
from pygame.mixer import set_num_channels

pygame.init()

SURFACEWIDTH = 600
SURFACEHEIGHT = 450
OFFSETX = 100
OFFSETY = 75
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
POINTSFORWIN = 15

WIN = pygame.mixer.Sound('win.wav')
FONT = pygame.font.Font('freesansbold.ttf', 32)

spaceImg = pygame.image.load('space.png')
spaceImg = pygame.transform.scale(spaceImg, (SURFACEWIDTH, SURFACEHEIGHT))

taskText = FONT.render('Postavi nisan i opali na SPACE', 1, WHITE)
taskRect = taskText.get_rect()
taskRect.topleft = (SURFACEWIDTH - 250, 10)

winText = FONT.render('TASK COMPLETED!', 1, GREEN)
winRect = winText.get_rect()
winRect.center = (SURFACEWIDTH/2, SURFACEHEIGHT/2)

sniperGameSurface = pygame.Surface((SURFACEWIDTH,SURFACEHEIGHT))

nisanRect1 = pygame.rect.Rect(0, 0, 200, 20)
nisanRect2 = pygame.rect.Rect(0, 0, 20, 200)

class SniperGame:
    
    def __init__(self) -> None:
        self.crossCenterX = random.randrange(0, 600)
        self.crossCenterY = random.randrange(0, 450)
        nisanRect1.center = (self.crossCenterX, self.crossCenterY)
        nisanRect2.center = (self.crossCenterX, self.crossCenterY)
        
    def igraj(self):
        self.checkClick()
        self.checkNisan()

    def doticeNisan(mousex, mousey, self):
        nisanRect1.collidepoint(mousex, mousey)



    def checkClick(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                self.doticeNisan(mousex, mousey)
                    
    def checkNisan(self):
        if (self.crossCenterX >= SURFACEWIDTH/2 - 10) and (self.crossCenterX <= SURFACEWIDTH/2 + 10) and self.crossCenterY >= SURFACEHEIGHT/2 - 10 and self.crossCenterY >= SURFACEHEIGHT/2 + 10:
            self.won = True

    
    def drawSniperGame(self, screen, fpsClock, FPS):
        pygame.draw.rect(sniperGameSurface, WHITE, nisanRect1)
        pygame.draw.rect(sniperGameSurface, WHITE, nisanRect2)

        if(self.won):
            WIN.play()
            sniperGameSurface.blit(winText, winRect)               # ispisujemo pobedu
            screen.blit(sniperGameSurface, (OFFSETX, OFFSETY))
            pygame.display.update()
            fpsClock.tick(FPS)
            pygame.time.wait(2000)
        screen.blit(sniperGameSurface, (OFFSETX, OFFSETY))