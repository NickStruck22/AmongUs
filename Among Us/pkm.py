import sys, pygame, random
from pygame.locals import *

pygame.init()

GRAY = (155, 155, 155)
RED = (255, 0, 0)
GREEN = (0,255,0)
WHITE = (255, 255, 255)
SURFACEWIDTH = 600
SURFACEHEIGHT = 450
MARGIN = 30
RECTGAP = 25
SMALLRECTW = 100
SMALLRECTH = 100
OFFSETX = 100
OFFSETY = 75

WIN = pygame.mixer.Sound('win.wav')
FONT = pygame.font.Font('freesansbold.ttf', 32)

pkmSurface = pygame.Surface((SURFACEWIDTH, SURFACEHEIGHT))
PKMBACKGROUND = pygame.Rect(0, 0, SURFACEWIDTH, SURFACEHEIGHT)
COMPUTERRECT = pygame.Rect(MARGIN, MARGIN, SURFACEWIDTH/2, SURFACEHEIGHT/2)
PAPIRRECT = pygame.Rect( 400, MARGIN, SMALLRECTW, SMALLRECTH)
KAMENRECT = pygame.Rect( 400, MARGIN + RECTGAP + SMALLRECTH, SMALLRECTW, SMALLRECTH)
MAKAZERECT = pygame.Rect( 400, MARGIN + RECTGAP*2 + SMALLRECTH*2, SMALLRECTW, SMALLRECTH)

papirImg = pygame.image.load("papir.png")
papirRect = papirImg.get_rect()
papirRect.center = PAPIRRECT.center

kamenImg = pygame.image.load("kamen.png")
kamenRect = kamenImg.get_rect()
kamenRect.center = KAMENRECT.center

makazeImg = pygame.image.load("makaze.png")
makazeRect = makazeImg.get_rect()
makazeRect.center = MAKAZERECT.center

victoryText = FONT.render('TASK COMPLETED !', True, GREEN)
victoryRect = victoryText.get_rect()
victoryRect.center = (SURFACEWIDTH/2, SURFACEHEIGHT/2)

class Pkm:

    def __init__(self) -> None:
        self.points = 0
        self.pointsForWin = 3
        self.scoreText = FONT.render(str(self.points) + '/3', True, RED)
        self.scoreRect = self.scoreText.get_rect()
        self.scoreRect.topleft = (MARGIN, SURFACEHEIGHT - 100)
        self.pritisnutoDugme = None
        self.computerPKM = None
        self.computerImg = None
        self.computerImgRect = makazeImg.get_rect()
        self.computerImgRect.center = COMPUTERRECT.center
        self.cekanjeNaIgraca = False
        self.won = False

    
    def igraj(self):
        self.checkClick()
        if not self.cekanjeNaIgraca:
            self.computerPKM = random.choice(("papir", "kamen", "makaze"))      # kompjuter bira svoj znak i prikazuje ga i posle toga ceka na igraca
            if(self.computerPKM == "papir"):
                self.computerImg = pygame.image.load("papir.png")
            elif(self.computerPKM == "kamen"):
                self.computerImg = pygame.image.load("kamen.png")
            else:
                self.computerImg = pygame.image.load("makaze.png")
            # ovde moze da se doda neka animacija da se zna da je promenio, jer je bezveze kada dva puta za redom lupi isti
            self.cekanjeNaIgraca = True
        else:
            if self.pritisnutoDugme and self.dobarZnak():       # moramo da napravimo posebno pitanje ako smo tacni znak odabrali
                self.points += 1                                # tacno smo klknuli pa povecavamo poene, ako smo sva 3 pobedili onda cuvamo pobedu i vracamo False,
                if self.points == self.pointsForWin:            #  da bi main znao da ne treba vise da proverava pkmTerminal
                    self.won = True
                    return False
                self.pritisnutoDugme = None                     # vracamo dugme na None i kompjuter vise ne ceka na nas
                self.cekanjeNaIgraca = False
            elif self.pritisnutoDugme and self.pogresanZnak():      #moramo da napravimo posebno pitanje ako smo pogresni znak odabrali
                self.cekanjeNaIgraca = False                    # pogresili smo, vraca nas na 0 poena i ne ceka nas vise
                self.pritisnutoDugme = None
                self.points = 0
                pygame.time.wait(200)
        return True                                 # vracamo True, da bi main znao da nastavi da prikazuje pkm
    
    def checkClick(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                self.pritisnutoDugme = self.proslediPritisnutoDugme(mousex - OFFSETX, mousey - OFFSETY) # prosledjujemo smanjeno za offset zato sto je surface blitovan na screen na toj tacki
                print(self.pritisnutoDugme)

    def proslediPritisnutoDugme(self, x, y):        # vraca pritisnuto dugme ili None
        if papirRect.collidepoint((x, y)):
            return "papir"
        elif kamenRect.collidepoint((x, y)):
            return "kamen"
        elif makazeRect.collidepoint((x, y)):
            return "makaze"
        return None

    def dobarZnak(self):
        if(self.computerPKM == "papir" and self.pritisnutoDugme == "makaze"):
            return True
        elif(self.computerPKM == "makaze" and self.pritisnutoDugme == "kamen"):
            return True
        elif(self.computerPKM == "kamen" and self.pritisnutoDugme == "papir"):
            return True
        return False
    
    def pogresanZnak(self):
        if(self.computerPKM == "papir" and self.pritisnutoDugme == "kamen"):
            return True
        elif(self.computerPKM == "makaze" and self.pritisnutoDugme == "papir"):
            return True
        elif(self.computerPKM == "kamen" and self.pritisnutoDugme == "makaze"):
            return True
        return False

    def drawPkm(self, screen, fpsClock, FPS):
        pygame.draw.rect(pkmSurface, GRAY, PKMBACKGROUND)                       #
        pygame.draw.rect(pkmSurface, WHITE, COMPUTERRECT)                       #
        pygame.draw.rect(pkmSurface, WHITE, PAPIRRECT)                          #
        pygame.draw.rect(pkmSurface, WHITE, KAMENRECT)                          #
        pygame.draw.rect(pkmSurface, WHITE, MAKAZERECT)                         #
        pkmSurface.blit(self.computerImg, self.computerImgRect)                 #
        pkmSurface.blit(papirImg, papirRect)                                    # sve ove crtamo na pkmSurface koji je novi prozor igre koji se otvara kad pritisnemo E na terminalu
        pkmSurface.blit(kamenImg, kamenRect)                                    #
        pkmSurface.blit(makazeImg, makazeRect)                                  #
        self.scoreText = FONT.render(str(self.points) + '/3', True, RED)        #
        pkmSurface.blit(self.scoreText, self.scoreRect)                         #

        if(self.won):
            WIN.play()
            pkmSurface.blit(victoryText, victoryRect)               # ispisujemo pobedu
            screen.blit(pkmSurface, (OFFSETX, OFFSETY))
            pygame.display.update()
            fpsClock.tick(FPS)
            pygame.time.wait(2000)
        screen.blit(pkmSurface, (OFFSETX, OFFSETY))     #kad blitujemo na screen pkmSurface, stavljamo ga na offset, da bi bio na centru ekrana



