import sys, pygame, random
from pygame.locals import *

pygame.init()

SURFACEWIDTH = 600
SURFACEHEIGHT = 450
OFFSETX = 100
OFFSETY = 75
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
POINTSFORWIN = 15

BOOM = pygame.mixer.Sound('boom.wav')
WIN = pygame.mixer.Sound('win.wav')
FONT = pygame.font.Font('freesansbold.ttf', 32)

spaceImg = pygame.image.load('space.png')
spaceImg = pygame.transform.scale(spaceImg, (SURFACEWIDTH, SURFACEHEIGHT))
asteroidImg = pygame.image.load('asteroid.png')

scoreText = FONT.render('Score: 0', 1, WHITE)
scoreRect = scoreText.get_rect()
scoreRect.topleft = (SURFACEWIDTH - 150, 10)

winText = FONT.render('TASK COMPLETED!', 1, GREEN)
winRect = winText.get_rect()
winRect.center = (SURFACEWIDTH/2, SURFACEHEIGHT/2)

asteroidGameSurface = pygame.Surface((SURFACEWIDTH,SURFACEHEIGHT))

class Asteroid:
    
    def __init__(self) -> None:
        self.rect = asteroidImg.get_rect()
        self.rect.topleft = (random.randint(0, SURFACEWIDTH - self.rect.width), random.randint(0, SURFACEHEIGHT - self.rect.height))
        self.moveX = random.randint(-10,10)
        self.moveY = random.randint(-10,10)

    def move(self):
        if self.rect.top < 1:
            self.moveY = 5
        if self.rect.bottom > SURFACEHEIGHT-1:
            self.moveY = -5
        if self.rect.left < 1:
            self.moveX = 5
        if self.rect.right > SURFACEWIDTH-1:
            self.moveX = -5
        
        self.rect.x += self.moveX
        self.rect.y += self.moveY

    
    def drawAsteroid(self):
        asteroidGameSurface.blit(asteroidImg, self.rect)

a1 = Asteroid()
a2 = Asteroid()
a3 = Asteroid()

class AsteroidGame:

    def __init__(self) -> None:
        self.won = False
        self.score = 0
        self.asteroids = [a1, a2 , a3]

    def igraj(self):
        self.checkClick()
        for asteroid in self.asteroids:
            asteroid.move()
        if self.score == POINTSFORWIN:
            self.won = True
            return False
        return True

    def checkClick(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP: 
                mouseX, mouseY = event.pos
                for asteroid in self.asteroids:
                    if asteroid.rect.collidepoint((mouseX - OFFSETX, mouseY - OFFSETY)):
                        #BOOM.play()
                        self.score += 1
                        asteroid.rect.topleft = (random.randint(0, SURFACEWIDTH - asteroid.rect.width), random.randint(0, SURFACEHEIGHT - asteroid.rect.height))
                        asteroid.moveX, asteroid.moveY = (random.randint(-10,10), random.randint(-10,10))

    def draw(self, screen, fpsClock, FPS):
        asteroidGameSurface.blit(spaceImg, (0,0))
        scoreText = FONT.render('Score: ' + str(self.score), True, WHITE)
        asteroidGameSurface.blit(scoreText, scoreRect)
        for asteroid in self.asteroids:
            asteroid.drawAsteroid()

        if(self.won):
            WIN.play()
            asteroidGameSurface.blit(spaceImg, (0,0))
            asteroidGameSurface.blit(winText, winRect)
            screen.blit(asteroidGameSurface, (OFFSETX, OFFSETY))
            pygame.display.update()
            fpsClock.tick(FPS)
            pygame.time.wait(2000)
        screen.blit(asteroidGameSurface, (OFFSETX, OFFSETY))


