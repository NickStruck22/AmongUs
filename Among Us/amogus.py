import sys, pygame
import collision as coll
from pygame.locals import *

SIRINAEKRANA = 800
VISINAEKRANA = 600

pygame.init()

class Amogus:

    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.prewX = 0
        self.prewY = 0
        self.speed = 5
        self.direction = 'right'
        self.index = 0
        self.images = []
        self.images.append(pygame.image.load('amogus1.png'))
        self.images.append(pygame.image.load('walk1.png'))
        self.images.append(pygame.image.load('walk2.png'))
        self.images.append(pygame.image.load('walk3.png'))
        self.images.append(pygame.image.load('walk4.png'))
        self.image = self.images[0]

    def checkInput(self):
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_a]:
            self.updatePos(-self.speed, 0)
            self.direction = 'left'
        elif keys[pygame.K_d]:
            self.updatePos(self.speed, 0)
            self.direction = 'right'
        if keys[pygame.K_w]:
            self.updatePos(0, -self.speed)
        elif keys[pygame.K_s]:
            self.updatePos(0, self.speed)
        
        if not (keys[pygame.K_a] or keys[pygame.K_d]):
            self.prewX = self.x
        if not (keys[pygame.K_w] or keys[pygame.K_s]):
            self.prewY = self.y
            
    def updatePos(self, x, y):
        self.polygon1 = self.createPolygon1(-self.x , -self.y)
        self.polygon2 = self.createPolygon2(-self.x, -self.y)
        self.polygon3 = self.createPolygon3(-self.x, -self.y)
        newRect = self.image.get_rect()
        newRect.x += x
        newRect.y += y
        if not (coll.collideRectPolygon(newRect, self.polygon1) 
        or coll.collideRectPolygon(newRect, self.polygon2) 
        or coll.collideRectPolygon(newRect, self.polygon3)):
            self.x += x
            self.y += y
            
    def draw(self, screen):
        if self.prewX != self.x or self.prewY != self.y:
            self.index += 1
            if(self.index >= len(self.images)):
                self.index = 1
        else:
            self.index = 0    

        if self.direction == 'left':
            self.image = pygame.transform.flip(self.images[self.index], True, False)
        else:
            self.image = self.images[self.index]
        
        screen.blit(self.image, (SIRINAEKRANA/2, VISINAEKRANA/2))
        # iscrtavanje poligona za zidove
        # poly = self.createPolygon1(SIRINAEKRANA/2-self.x, VISINAEKRANA/2 - self.y)
        # pygame.draw.polygon(screen, (255, 0, 0), poly, 10)
        # poly = self.createPolygon2(SIRINAEKRANA/2-self.x, VISINAEKRANA/2 - self.y)
        # pygame.draw.polygon(screen, (255, 0, 0), poly, 10)
        # poly = self.createPolygon3(SIRINAEKRANA/2-self.x, VISINAEKRANA/2 - self.y)
        # pygame.draw.polygon(screen, (255, 0, 0), poly, 10)
        

    def createPolygon1(self, x, y):
        return [
            (x-275.0, y+10.0), (x-240.0, y-89.0), (x-150.0, y-170.0), (x-150.0, y-240.0),
            (x-150.0, y-625.0), (x-40.0, y-720.0), (x-40.0, y-730.0), (x-60.0, y-730.0), 
            (x-65.0, y-775.0), (x-105.0, y-835.0), (x-105.0, y-995.0), (x+120.0, y-995.0), 
            (x+120.0, y-835.0), (x+75.0, y-775.0), (x+75.0, y-730.0), (x+60.0, y-730.0), 
            (x+60.0, y-670.0), (x-50.0, y-580.0), (x-50.0, y-490.0), (x-45.0, y-490.0), 
            (x-45.0, y-530.0), (x+65.0, y-615.0), (x+160.0, y-615.0), (x+160.0, y-355.0), 
            (x-45.0, y-355.0), (x-45.0, y-395.0), (x-50.0, y-395.0), (x-50.0, y-240.0),  
            (x+30.0, y-240.0), (x+30.0, y-190.0), (x+50.0, y-180.0), (x+60.0, y-195.0), 
            (x+40.0, y-230.0), (x+40.0, y-280.0), (x+195.0, y-280.0), (x+195.0, y-145.0),
            (x+140.0, y-145.0), (x+130.0, y-130.0), (x+170.0, y-65.0), (x+195.0, y+15.0), 
            (x+310.0, y+15.0), (x+310.0, y-315.0), (x+335.0, y-335.0), (x+425.0, y-335.0), 
            (x+450.0, y-315.0), (x+450.0, y+15.0), (x+635.0, y+15.0), (x+645.0, y+5.0), 
            (x+645.0, y-15.0), (x+605.0, y-15.0), (x+605.0, y-320.0), (x+750.0, y-375.0), 
            (x+785.0, y-375.0), (x+785.0, y-15.0), (x+740.0, y-15.0), (x+740.0, y+50.0),
            (x+700.0, y+100.0), (x+665.0, y+115.0), (x+450.0, y+115.0), (x+450.0, y+160.0), 
            (x+610.0, y+160.0), (x+610.0, y+265.0), (x+575.0, y+380.0), (x+505.0, y+505.0), 
            (x+405.0, y+600.0), (x+340.0, y+640.0), (x+320.0, y+610.0), (x+330.0, y+570.0), 
            (x+310.0, y+535.0), (x+280.0, y+535.0), (x+200.0, y+400.0), (x+135.0, y+430.0), 
            (x+45.0, y+445.0), (x+20.0, y+470.0), (x+30.0, y+480.0), (x+30.0, y+555.0), 
            (x+45.0, y+560.0), (x+80.0, y+675.0), (x+65.0, y+890.0), (x-110.0, y+890.0),
            (x-130.0, y+675.0), (x-90.0, y+560.0), (x-65.0, y+560.0), (x-70.0, y+475.0), 
            (x-65.0, y+470.0), (x-85.0, y+450.0), (x-180.0, y+435.0), (x-230.0, y+415.0),
            (x-270.0, y+380.0), (x-285.0, y+390.0), (x-255.0, y+415.0), (x-380.0, y+625.0), 
            (x-490.0, y+545.0), (x-555.0, y+460.0), (x-590.0, y+395.0), (x-620.0, y+320.0), 
            (x-635.0, y+235.0), (x-635.0, y+120.0), (x-395.0, y+120.0), (x-395.0, y+180.0), 
            (x-380.0, y+250.0), (x-340.0, y+330.0), (x-330.0, y+320.0), (x-370.0, y+230.0), 
            (x-380.0, y+185.0), (x-380.0, y+145.0), (x-380.0, y+110.0), (x-705.0, y+105.0), 
            (x-765.0, y+65.0), (x-780.0, y+35.0), (x-780.0, y-20.0), (x-825.0, y-20.0), 
            (x-825.0, y-385.0), (x-800.0, y-385.0), (x-640.0, y-320.0), (x-640.0, y-25.0), 
            (x-680.0, y-25.0), (x-680.0, y+10.0), (x-675.0, y+10.0), (x-275.0, y+10.0),
            ]
    
    def createPolygon2(self, x, y):
        return [
            (x-70.0, y+110.0), (x-70.0, y+180.0), (x-75.0, y+180.0), (x-75.0, y+120.0), 
            (x-265.0, y+120.0), (x-255.0, y+180.0), (x-235.0, y+230.0), (x-195.0, y+275.0), 
            (x-155.0, y+300.0), (x-105.0, y+320.0), (x-75.0, y+320.0), (x-75.0, y+280.0), 
            (x-70.0, y+280.0), (x-70.0, y+350.0), (x-90.0, y+375.0), (x-155.0, y+360.0), 
            (x-215.0, y+330.0), (x-260.0, y+280.0), (x-285.0, y+240.0), (x-305.0, y+185.0), 
            (x-305.0, y+150.0), (x-305.0, y+110.0), (x-70.0, y+110.0),
        ]
    
    def createPolygon3(self, x, y):
        return [
            (x+30.0, y+110.0), (x+310.0, y+110.0), (x+310.0, y+155.0), (x+210.0, y+155.0),
            (x+185.0, y+180.0), (x+140.0, y+180.0), (x+140.0, y+300.0), (x+160.0, y+335.0), 
            (x+105.0, y+360.0), (x+45.0, y+370.0), (x+30.0, y+350.0), (x+30.0, y+320.0), 
            (x+65.0, y+300.0), (x+70.0, y+265.0), (x+65.0, y+240.0), (x+45.0, y+225.0), 
            (x+30.0, y+220.0), (x+30.0, y+110.0) 
        ]
            

        