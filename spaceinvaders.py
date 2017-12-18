# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 19:09:17 2016

@author: lenovo
"""

import sys
sys.path.append("modules") 
import time
import random
import threading
from queue import Queue
import _thread
_start_new_thread = _thread.start_new_thread



import pygame
from pygame.locals import *

pygame.init()
gameDisplay = pygame.display.set_mode((800 ,600)) 
display_width = 800
display_height = 600

myfont = pygame.font.SysFont("monospace", 64)
myfont5 = pygame.font.SysFont("monospace", 16)
myfont1 = pygame.font.SysFont("outrun future", 26)
pygame.display.set_caption('Space Invaders')

black = (0,0,0)
white = (255,255,255)
ob1=pygame.image.load("bbb1.png").convert_alpha()
player_s=pygame.image.load("aaa1.png").convert_alpha()
fire_s=pygame.image.load("fire.bmp").convert_alpha()



        
class starship:
    SPRITE = None
    x = None
    y = None
    speed = None
    score=None
    life = None
    firex= None
    firey= None
    fire_speed= None
    fireSPRITE = None
    fireBOOL = None
    def __init__(self):
        self.SPRITE = player_s
        self.size = (40, 38)
        self.x =  (display_width * 0.45)
        self.y = (display_height * 0.8)
        self.x_change = 0
        self.speed = 4
        self.life = 5
        self.score=0
        
        self.fireSPRITE = fire_s
        self.firex = self.x + 20
        self.firey = self.y
        self.fire_speed = 6
        self.fireBOOL = False
    
    def Fire_t(self):
        while(self.fireBOOL == True) and (-1*self.firey<0):
            self.firey-=self.fire_speed
            
            time.sleep(0.01)
            
        self.fireBOOL = False
        self.firex = self.x + 20
        self.firey = self.y 
        
    def Fire(self):
        if self.fireBOOL != True:
            self.firex = self.x + 20
            self.firey = self.y - 5
            self.fireBOOL = True
            _thread.start_new_thread(self.Fire_t, ())
            
        
        
    def Render(self):
        pygame.display.get_surface().blit(self.SPRITE, (self.x, self.y))  
        if self.fireBOOL == True:
            pygame.display.get_surface().blit(self.fireSPRITE, (self.firex, self.firey))

    def right (self):
        self.x += self.x_change
        
         
    def left (self):
        self.x -= self.x_change
       
    def coord (self):
        if self.x <=0:
            self.x=0
        if self.x>=762:
            self.x=762
class Callable:
    def __init__(self, anycallable):
        self.__call__ = anycallable            
class AlienType:

    def Type0(self):
        return -1

    def Type1(self):
        return 0     
    Type0 = Callable(Type0)
    Type1 = Callable(Type1)


class Alien_Tools:
    ACROSS=11
    ROWS = 5
    Alien_list = []
    AlienSurface = pygame.Surface(((ACROSS*58),(ROWS*50)))
    AlienSurface.set_colorkey((0,0,0))
    AlienSurface.fill(AlienSurface.get_colorkey())   
    MOVEMENT = "INCREASE"
    MoveX = 0
    MoveY = 0 
    
    class Alien:
        SPRITE = None
        TYPE = None
        x = None
        y = None
        Frame = None
        STOP_THREADS = None
        fireSPRITE = None
        firey = None
        firex = None
        fireBOOL = None
        fire_speed = None
        is_alive = None
        
        
        def __init__(self, Type):
            self.SPRITE = []
            self.TYPE = Type
            self.FRAME = 0
            self.STOP_THREADS = False
            self.is_alive= True
            if self.TYPE == AlienType.Type0:
                AlienSurface = pygame.Surface((40,38))
                AlienSurface.fill((0,0,0))
                self.SPRITE.append(AlienSurface)
                self.SPRITE.append(AlienSurface)
                
            elif self.TYPE == AlienType.Type1:
                self.SPRITE.append(ob1)
                self.SPRITE.append(pygame.image.load("bbb1.png"))
            
            self.x = 0
            self.y = 0
            
            self.fireSPRITE = pygame.image.load("fire1.bmp")
            self.firex = self.x+20
            self.firey = self.y+15
            self.fire_speed = 6
            self.fireBOOL = False
            
        def Fire (self):
            if self.TYPE != AlienType.Type0:
                if self.fireBOOL == False:
                    self.firex = self.x+20
                    self.firey = self.y + 15
                    
                    self.fireBOOL=True

                
        def Render(self):
            Alien_Tools.AlienSurface.blit(self.SPRITE[self.FRAME], (self.x, self.y))
            
        def setX(self, x):
                #Set XPos
            self.x = x
    
        def setY(self, y):
                #Set YPos
            self.y = y
            
        def getX(self):
            return self.x
            
        def getY(self):
            return self.y
            
        def getType(self):
            #Return Alien type
            return self.TYPE
            
            
    def __init__(self):
        self.Alien_list = []
        
    def Generate (self):
        for i in range (0, self.ROWS):
            for j in range (0, self.ACROSS):
                sEnemy=self.Alien(AlienType.Type1)
                self.Alien_list.append(sEnemy)
                sEnemy = None

    def Render (self):
        nRow = 0
        nAcross = 0
        
        for i in range (0, len(self.Alien_list)):
            self.Alien_list[i].setX((nAcross*(40+13)))
            self.Alien_list[i].setY((nRow*(38+13)))
            
            self.Alien_list[i].Render()
            
            
            self.Alien_list[i].setX(self.Alien_list[i].getX() + self.MoveX)
            self.Alien_list[i].setY(self.Alien_list[i].getY() + self.MoveY)
            
            if nAcross < self.ACROSS:
                nAcross += 1
            
                if nAcross == self.ACROSS:
                    nAcross=0
                    nRow+=1
            
            if self.Alien_list[i].fireBOOL == True:
                pygame.display.get_surface().blit(self.Alien_list[i].fireSPRITE, (self.Alien_list[i].firex, self.Alien_list[i].firey))
                
                if self.Alien_list[i].firey < 560:
                    self.Alien_list[i].firey += self.Alien_list[i].fire_speed
                else:
                    self.Alien_list[i].fireBOOL = False
                    
                    
        pygame.display.get_surface().blit(self.AlienSurface, (self.MoveX, self.MoveY))
        
        if self.MOVEMENT == "INCREASE":
            if self.MoveX < 220:
                self.MoveX += 0.5
            else:
                self.MoveY += (20+13)
                self.MOVEMENT = "DECREASE"
                
        if self.MOVEMENT == "DECREASE":
            if self.MoveX > 0:
                self.MoveX -=  0.5
            else:
                self.MoveY += (20+13)
                self.MOVEMENT = "INCREASE"
                
    def Kill (self, i):
        
        self.Alien_list[i]=self.Alien(AlienType.Type0)
        self.Alien_list[i].is_alive = False

        
    
class obstacle:
    SPRITE = None
    SPRITE2 = None
    SPRITE3 = None
    SPRITE4 = None
    SPRITE5 = None
    TYPE = None
    x = None
    y = None
    hit = None
    hit1=None
    hit2=None
    hit3=None
    def __init__(self):
        self.SPRITE = pygame.image.load("obstacle.png")
        self.SPRITE2 = pygame.image.load("obstacle1.png")
        self.SPRITE3 = pygame.image.load("obstacle2.png")
        self.SPRITE4 = pygame.image.load("obstacle3.png")
        self.SPRITE5 = pygame.image.load("obstacle4.png")
        self.size = (80, 20)
        self.x = 80
        self.y = 400
        self.hit = 0
        self.hit1=0
        self.hit2=0
        self.hit3=0
       
    def Render(self):
        if self.hit==0 or self.hit==1:
            pygame.display.get_surface().blit(self.SPRITE, (self.x, self.y))
        elif self.hit == 2 or self.hit==3:
            pygame.display.get_surface().blit(self.SPRITE2, (self.x, self.y))
        elif self.hit == 4 or self.hit==5:
            pygame.display.get_surface().blit(self.SPRITE3, (self.x, self.y))
        elif self.hit == 6 or self.hit==7:
            pygame.display.get_surface().blit(self.SPRITE4, (self.x, self.y))
        else:
            pygame.display.get_surface().blit(self.SPRITE5, (self.x, self.y))
        
        if self.hit1==0 or self.hit1==1:
            pygame.display.get_surface().blit(self.SPRITE, (self.x+200, self.y))
        elif self.hit1 == 2 or self.hit1==3:
            pygame.display.get_surface().blit(self.SPRITE2, (self.x+200, self.y))
        elif self.hit1 == 4 or self.hit1==5:
            pygame.display.get_surface().blit(self.SPRITE3, (self.x+200, self.y))
        elif self.hit1 == 6 or self.hit1==7:
            pygame.display.get_surface().blit(self.SPRITE4, (self.x+200, self.y))
        else:
            pygame.display.get_surface().blit(self.SPRITE5, (self.x+200, self.y))
            
        if self.hit2==0 or self.hit2==1:
            pygame.display.get_surface().blit(self.SPRITE, (self.x+400, self.y))
        elif self.hit2 == 2 or self.hit2==3:
            pygame.display.get_surface().blit(self.SPRITE2, (self.x+400, self.y))
        elif self.hit2 == 4 or self.hit2==5:
            pygame.display.get_surface().blit(self.SPRITE3, (self.x+400, self.y))
        elif self.hit2 == 6 or self.hit2==7:
            pygame.display.get_surface().blit(self.SPRITE4, (self.x+400, self.y))
        else:
            pygame.display.get_surface().blit(self.SPRITE5, (self.x+400, self.y))
       
        if self.hit3==0 or self.hit3==1:
            pygame.display.get_surface().blit(self.SPRITE, (self.x+600, self.y))
        elif self.hit3 == 2 or self.hit3==3:
            pygame.display.get_surface().blit(self.SPRITE2, (self.x+600, self.y))
        elif self.hit3 == 4 or self.hit3==5:
            pygame.display.get_surface().blit(self.SPRITE3, (self.x+600, self.y))
        elif self.hit3 == 6 or self.hit3==7:
            pygame.display.get_surface().blit(self.SPRITE4, (self.x+600, self.y))
        else:
            pygame.display.get_surface().blit(self.SPRITE5, (self.x+600, self.y))
def DrawBackground(background, xpos, ypos):
    gameDisplay.blit(background, [xpos, ypos])   
    
score=[0, 0, 0, 0, 0]          
dwa=False           
bg1 = pygame.image.load("game.png").convert()  
main=True
while main==True:        
    pygame.init()      
    start=False  
    win = False      
    while start==False: 
        bg = pygame.image.load("tlodogry.png")             
        DrawBackground(bg, 0, 0)
        start_text = myfont1.render("Wcisnij Enter zeby zaczac", False, (255,255,255))
        end_text = myfont1.render("Wcisnij Escape zeby wyjsc", False, (255,255,255))
        gameDisplay.blit(start_text, (200, 200))
        gameDisplay.blit(end_text, (200, 300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    dwa=True
                    start=True 
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                
                
    while dwa==True:
        DrawBackground(bg, 0, 0)
        start_text2 = myfont1.render("Wybierz poziom trudnosci (1-5)", False, (255,255,255))
        gameDisplay.blit(start_text2, (200, 200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type==KEYDOWN:
                if event.key==K_1:
                    a=2
                    b=1
                    dwa=False
                    done=False
                        
                if event.key==K_2:
                    a=1
                    b=2
                    dwa=False
                    done=False
                if event.key==K_3:
                    a=0.5
                    b=3
                    dwa=False
                    done=False
                if event.key==K_4:
                    a=0.2
                    b=4
                    dwa=False
                    done=False
                if event.key==K_5:
                    a=0.1 
                    b=5
                    dwa=False
                    done=False
    Alien = Alien_Tools()
    obstacle1=obstacle()
    Alien.Generate()
    display1=Alien_Tools.AlienSurface
    
    clock = pygame.time.Clock()
    player1=starship()                 
    nothing=False
        
    def ifAlien():
         canfire=[44, 45, 46, 47, 48,49, 50, 51, 52, 53, 54]
         while True:
             if len(Alien.Alien_list)>0:
                 for i in range (0, len(Alien.Alien_list)):
                    if i<44 and Alien.Alien_list[i+ 11].is_alive == False and Alien.Alien_list[i].is_alive==True:
                         canfire.append(int(i))
                    elif i>=44 and Alien.Alien_list[i].is_alive==True:
                        canfire.append(int(i))
                 Rnd = random.choice(canfire)
            
                 Alien.Alien_list[Rnd].Fire()
                 canfire = None
                 canfire = []
                        
                 time.sleep(a)
                
    _thread.start_new_thread(ifAlien, ())
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                nothing=True
                    
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player1.x_change = -5
                    player1.left()
                      
                elif event.key == pygame.K_RIGHT:
                    player1.x_change = 5
                    player1.right()
                        
                if event.key == K_SPACE:
                    player1.Fire()
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player1.x_change = 0
        for i in range (0, len(Alien.Alien_list)):
            if Alien.Alien_list[i].is_alive==True:
                if (player1.fireSPRITE.get_rect( center=(player1.firex, player1.firey) ).colliderect\
                    (Alien.Alien_list[i].SPRITE[Alien.Alien_list[i].FRAME].get_rect\
                     ( center=(Alien.Alien_list[i].getX()+20, Alien.Alien_list[i].getY()) ))) == True:
                    player1.fireBOOL = False
                    player1.score+=10
                        
                    Alien.Kill(i)
                    break

        for i in range(0, len(Alien.Alien_list)):
            if(Alien.Alien_list[i].fireSPRITE.get_rect(center=(Alien.Alien_list[i].firex, Alien.Alien_list[i].firey) ).colliderect\
               (player1.SPRITE.get_rect(center=(player1.x+20, player1.y)))) == True:
        
                if Alien.Alien_list[i].fireBOOL == True:
                                
                    player1.life -= 1
                       
                            
                Alien.Alien_list[i].fireBOOL = False
                Alien.Alien_list[i].firex = 0
                Alien.Alien_list[i].firey = 0
                if player1.life==0:
                    done=True
                            
                break
        
        for i in range(0, len(Alien.Alien_list)):
            if(Alien.Alien_list[i].fireSPRITE.get_rect(center=(Alien.Alien_list[i].firex, Alien.Alien_list[i].firey) ).colliderect\
                   (obstacle1.SPRITE.get_rect(center=(obstacle1.x+30, obstacle1.y)))) == True:
                if Alien.Alien_list[i].fireBOOL == True:
                    obstacle1.hit+=1
                    if obstacle1.hit<=8:
                        Alien.Alien_list[i].fireBOOL = False
                    
                        Alien.Alien_list[i].firex = 0
                        Alien.Alien_list[i].firey = 0
                    
            if(Alien.Alien_list[i].fireSPRITE.get_rect(center=(Alien.Alien_list[i].firex, Alien.Alien_list[i].firey) ).colliderect\
                   (obstacle1.SPRITE.get_rect(center=(obstacle1.x+235, obstacle1.y)))) == True:
                if Alien.Alien_list[i].fireBOOL == True:
                    obstacle1.hit1+=1
                    if obstacle1.hit1<=8:
                        Alien.Alien_list[i].fireBOOL = False
                    
                        Alien.Alien_list[i].firex = 0
                        Alien.Alien_list[i].firey = 0
                    
            if(Alien.Alien_list[i].fireSPRITE.get_rect(center=(Alien.Alien_list[i].firex, Alien.Alien_list[i].firey) ).colliderect\
                   (obstacle1.SPRITE.get_rect(center=(obstacle1.x+440, obstacle1.y)))) == True:
                if Alien.Alien_list[i].fireBOOL == True:
                    obstacle1.hit2+=1
                    if obstacle1.hit2<=8:
                        Alien.Alien_list[i].fireBOOL = False
                    
                        Alien.Alien_list[i].firex = 0
                        Alien.Alien_list[i].firey = 0
                        
            if(Alien.Alien_list[i].fireSPRITE.get_rect(center=(Alien.Alien_list[i].firex, Alien.Alien_list[i].firey) ).colliderect\
                   (obstacle1.SPRITE.get_rect(center=(obstacle1.x+640, obstacle1.y)))) == True:
                if Alien.Alien_list[i].fireBOOL == True:
                    obstacle1.hit3+=1
                    if obstacle1.hit3<=8:
                        Alien.Alien_list[i].fireBOOL = False
                    
                        Alien.Alien_list[i].firex = 0
                        Alien.Alien_list[i].firey = 0
                
        if (player1.fireSPRITE.get_rect( center=(player1.firex, player1.firey) ).colliderect\
            (obstacle1.SPRITE.get_rect(center=(obstacle1.x+30, obstacle1.y)))) == True:
                obstacle1.hit+=1
                if obstacle1.hit<=7:
                    player1.fireBOOL = False
                    
        if (player1.fireSPRITE.get_rect( center=(player1.firex, player1.firey) ).colliderect\
            (obstacle1.SPRITE.get_rect(center=(obstacle1.x+235, obstacle1.y)))) == True:
                obstacle1.hit1+=1
                if obstacle1.hit1<=7:
                    player1.fireBOOL = False
                    
        if (player1.fireSPRITE.get_rect( center=(player1.firex, player1.firey) ).colliderect\
            (obstacle1.SPRITE.get_rect(center=(obstacle1.x+440, obstacle1.y)))) == True:
                obstacle1.hit2+=1
                if obstacle1.hit2<=7:
                    player1.fireBOOL = False
                   
        if (player1.fireSPRITE.get_rect( center=(player1.firex, player1.firey) ).colliderect\
            (obstacle1.SPRITE.get_rect(center=(obstacle1.x+640, obstacle1.y)))) == True:
                obstacle1.hit3+=1
                if obstacle1.hit3<=7:
                    player1.fireBOOL = False
                    
        for i in range (0, len(Alien.Alien_list)):
            if Alien.Alien_list[i].is_alive and Alien.Alien_list[i].y+20>400:
                done = True
                win = False
                break
        player1.x += player1.x_change
        player1.coord()
        DrawBackground(bg1, 0, 0)
        player1.Render()
        Alien.Render()
        obstacle1.Render()
        count=0
        for i in range (0, len(Alien.Alien_list)):
            if Alien.Alien_list[i].is_alive==True:
                count+=1
        if count==0:
            win=True
            done=True
        lifetext = myfont5.render("Ilosc zyc: " + str(player1.life), 1, (255, 255, 255))
        scoretext = myfont5.render("Wynik: " + str(player1.score), 1, (255, 255, 255))
        gameDisplay.blit(lifetext, (5, 550))
        gameDisplay.blit(scoretext, (5, 565))
        pygame.display.update()
        clock.tick(70)
           
    if done==True and nothing==False:   
        if win==False:
            endtext=myfont.render("Gra skonczona!" , 1, white)
            pygame.display.get_surface().blit(endtext, (150, 300))
            if player1.score>score[b-1]:
                score[b-1]=player1.score
                highscore=myfont5.render("Gratulacje, najwyzszy wynik na poziomie "+str(b)+" - "+str(score[b-1]), 1, white)
                pygame.display.get_surface().blit(highscore, (200, 400))
            pygame.display.update()
            time.sleep(3)
        else:
            endtext=myfont.render("Wygrales!" , 1, white)
            pygame.display.get_surface().blit(endtext, (150, 300))
            if player1.score>score[b-1]:
                score[b-1]=player1.score
                highscore=myfont5.render("Gratulacje, najwyzszy wynik na poziomie "+str(b)+" - "+str(score[b-1]), 1, white)
                pygame.display.get_surface().blit(highscore, (200, 400))
            pygame.display.update()
            time.sleep(3)
                    
    
pygame.display.quit()
pygame.quit()