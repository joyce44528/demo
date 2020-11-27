# -*- coding: utf-8 -*-
"""
Created on Fri May  8 20:27:05 2020

@author: 110612048
"""
from pygame import *
import random
import RPi.GPIO as GPIO
from time import sleep
import lcd



GPIO.setmode(GPIO.BCM)
btn = 16
btn2 = 21
GPIO.setup(btn, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)


windowX = 650
windowY = 350

init()
clock = time.Clock()
window = display.set_mode((windowX, windowY))

display.set_caption('Dino')


ground = windowY - 35  

gravity = 1



class PlayerClass:
    def __init__(self, scale, imageChangeSpeed, terminalVelocity):
        self.dragon1 = transform.scale(image.load('dragon-1.png'), (88 * scale, 94 * scale))
        self.dragon2 = transform.scale(image.load('dragon-2.png'), (88 * scale, 94 * scale))
        self.dragon3 = transform.scale(image.load('dragon-3.png'), (88 * scale, 94 * scale))
        self.dragon4 = transform.scale(image.load('dragon-4.png'), (88 * scale, 94 * scale))
        self.dragon5 = transform.scale(image.load('dragon-5.png'), (88 * scale, 94 * scale))
        self.dragon6 = transform.scale(image.load('dragon-6.png'), (88 * scale, 94 * scale))
        self.dragon7 = transform.scale(image.load('dragon-7.png'), (117 * scale, 60 * scale))
        
        self.scale = scale
        self.imageChangeSpeed = imageChangeSpeed
        self.terminalVelocity = terminalVelocity
        
        self.height = 94  * scale
        self.width = 88 * scale
        
    
    dead = False
    
        
    def update (self):
        self.physics()
        
        if self.touchCactus():
            self.dead = True
            
        if not self.dead:
            self.playInput()
            self.playInput2()
            
        self.y += self.velocityY 
        
        self.show()
        
        
    def touchCactus(self):
        for  hurdles in hurdleManager.hurdleList:
            if self.x / 2 + self.width > hurdles.x :
                if self.x < hurdles.x + hurdles.width:
                    if self.y + self.height / 1.1 > hurdles.y:
                        return True
                        

        for  hurdles2 in hurdleManager2.hurdleList2:
            if self.x / 2 + self.width > hurdles2.x :
                if self.x < hurdles2.x + hurdles2.width:
                    if self.y + self.height / 1.1 > hurdles2.y:
                        return True
                        

        
        
        for  clouds in cloudManager.cloudList:
            if self.x / 1.5 + self.height > clouds.x :
                if self.y < clouds.y + clouds.height:
                    if self.y / 4 + self.width / 4 > clouds.y:
                        return True
                        

    x = 50
    y = 30
        
    velocityY = 0

  
    def playInput(self):
        bs1 = False        

        if GPIO.input(btn)==0:
            if bs1 == False:
                if self.y + self.height == ground:
                    self.velocityY -= 14
                else:
                   self.velocityY -= gravity / 1.5
                bs1 = True
                
        
    def playInput2(self): 
        bs2 = False
        
        if GPIO.input(btn2)==0:
            if bs2 == False:
                if self.y + self.height == ground:
                    self.velocityY += 55
                else:
                    self.velocityY += gravity /0.3
                bs2 = True
                    
    def physics(self): 
        if self.dead:
            if self.y < windowY:
                self.velocityY += 1
                

        elif self.y + self.height < ground:
            if self.velocityY < self.terminalVelocity:
                self.velocityY += gravity *1.5
               
        
        elif self.velocityY > 0: 
            self.velocityY = 0
            self.y = ground - self.height 
            
            
            
    runTick = 0
    
    
    def show(self):
        #pressedKeys = key.get_pressed()
        if GPIO.input(btn)==0:
            img = self.dragon1
            
        elif GPIO.input(btn2)==0:
            img = self.dragon7
            
        elif self.runTick <= self.imageChangeSpeed:
            img = self.dragon3
            
        elif self.runTick <= self.imageChangeSpeed * 1.5:
            img = self.dragon3
            
        elif self.runTick <= self.imageChangeSpeed * 2:
            img = self.dragon4 
            
        elif self.runTick <= self.imageChangeSpeed * 2.5:
            img = self.dragon4
            
        else:
             img = self.dragon1 
            
        self.runTick += 1
        
        if self.runTick >= self.imageChangeSpeed * 3:
            self.runTick = 0
        
        window.blit(img, (self.x , self.y + 23))

player = PlayerClass(1, 4, 5)


class CactusManager:
    def __init__(self, scale, spawnRange):
        self.img = transform.scale(image.load('cactus-1.png'), (10 * scale, 20  * scale))
        
        self.spawnRange = spawnRange
        self.hurdleList = []
        self.scale = scale
        
    
    
    def update(self, doSpawn, moveSpeed):
        if doSpawn:
            self.spawn()
        self.manage(moveSpeed)
        
     
    def manage(self, moveSpeed):
        hurdles2 = []
        
        for hurdle in self.hurdleList:
            hurdle.update(moveSpeed)
        
            if hurdle.onScreen:
                hurdles2.append(hurdle)
                
                
        
        self.hurdleList = hurdles2
        
    spawnTick = 0
    
    def spawn(self):
        if self.spawnTick >= self.spawnRange[1]:
            newCactus = Hurdle(windowX, self.img, 10 * self.scale, 20 * self.scale)
            self.hurdleList.append(newCactus)
            self.spawnTick = 0
            
        elif self.spawnTick > self.spawnRange[0]:
            if random.randint(0,self.spawnRange[1] - self.spawnRange[0]) == 0:
                newCactus = Hurdle(windowX, self.img, 10 * self.scale, 20 * self.scale)
                self.hurdleList.append(newCactus)
                self.spawnTick = 0
                
        self.spawnTick += 1
        

hurdleManager = CactusManager(3, (100, 128))




class CactusManager2:
    def __init__(self, scale, spawnRange):
        self.img = transform.scale(image.load('csctus-2.png'), (20 * scale, 20  * scale))
        
        self.spawnRange = spawnRange
        self.hurdleList2 = []
        self.scale = scale
        
    
    
    def update(self, doSpawn, moveSpeed):
        if doSpawn:
            self.spawn()
        self.manage(moveSpeed)
        
     
    def manage(self, moveSpeed):
        hurdles3 = []
        
        for hurdle in self.hurdleList2:
            hurdle.update(moveSpeed)
        
            if hurdle.onScreen:
                hurdles3.append(hurdle)
                
                
        
        self.hurdleList2 = hurdles3
        
    spawnTick = 0
    
    def spawn(self):
        if self.spawnTick >= self.spawnRange[1]:
            newCactus2 = Hurdle(windowX, self.img, 20 * self.scale, 20 * self.scale)
            self.hurdleList2.append(newCactus2)
            self.spawnTick = 0
            
        elif self.spawnTick > self.spawnRange[0]:
            if random.randint(0,self.spawnRange[1] - self.spawnRange[0]) == 0:
                newCactus2 = Hurdle(windowX, self.img, 20 * self.scale, 20 * self.scale)
                self.hurdleList2.append(newCactus2)
                self.spawnTick = 0
                
        self.spawnTick += 1
        

hurdleManager2 = CactusManager2(3, (240, 400))
                

class Hurdle:
    def __init__(self, x, img, width, height):
        self.x = x
        self.img = img
        self.width = width
        self.height = height
        self.y = ground - 30
        
        
        
    
    def update(self, moveSpeed):
        self.move(moveSpeed)
        self.show()
        
        
    def move(self, moveSpeed):
        self.x -= moveSpeed * 2
        
    def show(self):
        window.blit(self.img, (self.x, self.y))
        
    def onScreen(self):
        if self.x + self.width > 0:
            return True
        else:
            return False
            



class CloudManager:
    def __init__(self, scale, spawnRange):
        self.img = transform.scale(image.load('bird.png'), (92 * scale, 27 * scale))
        
        self.spawnRange = spawnRange
        self.cloudList = []
        self.scale = scale
        
    
    
    def update(self, doSpawn, moveSpeed):
        if doSpawn:
            self.spawn()
        self.manage(moveSpeed)
        
     
    def manage(self, moveSpeed):
        cloud2 = []
        
        for cloud in self.cloudList:
            cloud.update(moveSpeed)
        
            if cloud.onScreen:
                cloud2.append(cloud)
                
                
        
        self.cloudList = cloud2
        
    spawnTick = 0
    
    def spawn(self):
        if self.spawnTick >= self.spawnRange[1]:
            newCloud = Cloud(windowX, self.img, 10 * self.scale, 6 * self.scale)
            self.cloudList.append(newCloud)
            self.spawnTick = 0
            
        elif self.spawnTick > self.spawnRange[0]:
            if random.randint(0,self.spawnRange[1] - self.spawnRange[0]) == 0:
                newCloud = Cloud(windowX, self.img, 10 * self.scale, 6 * self.scale)
                self.cloudList.append(newCloud)
                self.spawnTick = 0
                
        self.spawnTick += 1
        

cloudManager = CloudManager(1, (330, 570))
                

class Cloud:
    def __init__(self, x, img, width, height):
        self.x = x
        self.img = img
        self.width = width
        self.height = height
        self.y = ground - random.randint(70, 90)
        
        
        
    
    def update(self, moveSpeed):
        self.move(moveSpeed)
        self.show()
        
        
    def move(self, moveSpeed):
        self.x -= moveSpeed * 2.4
        
    def show(self):
        window.blit(self.img, (self.x, self.y))
        
    def onScreen(self):
        if self.x + self.width > 0:
            return True
        else:
            return False
            



class CloudManager2:
    def __init__(self, scale, spawnRange):
        self.img = transform.scale(image.load('cloth.png'), (92 * scale, 27 * scale))
        
        self.spawnRange = spawnRange
        self.cloud2List = []
        self.scale = scale
        
    
    
    def update(self, doSpawn, moveSpeed):
        if doSpawn:
            self.spawn()
        self.manage(moveSpeed)
        
     
    def manage(self, moveSpeed):
        cloud3 = []
        
        for clouds in self.cloud2List:
            clouds.update(moveSpeed)
        
            if clouds.onScreen:
                cloud3.append(clouds)
                
                
        
        self.cloud2List = cloud3
        
    spawnTick = 0
    
    def spawn(self):
        if self.spawnTick >= self.spawnRange[1]:
            newClouds = Cloud2(windowX, self.img, 10 * self.scale, 3 * self.scale)
            self.cloud2List.append(newClouds)
            self.spawnTick = 0
            
        elif self.spawnTick > self.spawnRange[0]:
            if random.randint(0,self.spawnRange[1] - self.spawnRange[0]) == 0:
                newClouds = Cloud2(windowX, self.img, 10 * self.scale, 3 * self.scale)
                self.cloud2List.append(newClouds)
                self.spawnTick = 0
                
        self.spawnTick += 1
        

cloudManager2 = CloudManager2(1, (30, 80))
                

class Cloud2:
    def __init__(self, x, img, width, height):
        self.x = x
        self.img = img
        self.width = width
        self.height = height
        self.y = ground - random.randint(190, 270)
        
        
        
    
    def update(self, moveSpeed):
        self.move(moveSpeed)
        self.show()
        
        
    def move(self, moveSpeed):
        self.x -= moveSpeed * 2
        
    def show(self):
        window.blit(self.img, (self.x, self.y))
        
    def onScreen(self):
        if self.x + self.width > 0:
            return True
        else:
            return False









def mainEventLoop():
    for events in event.get():
        if events.type == KEYDOWN:
            if events.key == K_ESCAPE:
                quit()


groundImg = transform.scale(image.load('ground.png'), (windowX, int(windowY - ground)))


font = font.SysFont("", 40)
deadword = image.load('gameover.png')
deadword2 = image.load('again.png')

message1Rect = deadword.get_rect()
message1x = windowX / 2 - message1Rect.width / 2        

message2Rect = deadword.get_rect()
message2x = windowX  - message2Rect.width / 1.1

def showMessage(y):
    window.blit(deadword, (message1x, y))
    window.blit(deadword2, (message2x, y + message1Rect.height + 20))

                           
score = {'gameScore': 0}
lcd.data(True)



def game():
    player.update()
    #Cloth(True)
    lcd.data(True)
    
    while True:
        if player.dead:
            fall()
        
        mainEventLoop()
        window.fill((250, 252, 255))
        
        player.update()
        
        hurdleManager.update(True, score['gameScore'] / 50 + 3)
        hurdleManager2.update(True, score['gameScore'] / 50 + 3)
        cloudManager.update(True, score['gameScore'] / 50 + 3)
        cloudManager2.update(True, score['gameScore'] / 50 + 3)
       
        window.blit(groundImg, (0, ground))
        
        clock.tick(60)
        
        scoreStr = font.render(str(round(score['gameScore'])), True, (173, 169, 168))
        window.blit(scoreStr, (50, 50))

        
    
        display.update()
        score['gameScore']  += 0.1
        
                
        
def fall():
    space = 0
    lcd.again(True)
        
    while True:
        #pressedKeys = key.get_pressed()
        
        oldSpace = space
        space = GPIO.input(btn)==0
        
        mainEventLoop()
        window.fill((250, 252, 255))
        
        player.update()
        
        
        hurdleManager.update(False, score['gameScore'] / 50 + 3)
        
        hurdleManager2.update(False, score['gameScore'] / 50 + 3)
        
        cloudManager.update(False, score['gameScore'] / 50 + 3)
        
        cloudManager2.update(False, score['gameScore'] / 50 + 6)
       
        
        window.blit(groundImg, (0, ground))
        
        
        clock.tick(60)
        
        showMessage(50)
        
        scoreStr = font.render(str(round(score['gameScore'])), True, (173, 169, 168))
        window.blit(scoreStr, (50, 50))
        
        if GPIO.input(btn2)==0:
            lcd.ex(True)
            quit()
        
        display.update()
        
        spaceEvent = space - oldSpace
        
        if spaceEvent == 1:
            #reset everything
            
            hurdleManager.hurdleList = []
            cloudManager.cloudList = []
            cloudManager2.cloud2List = []
            player.velocityY = 0
            player.dead = False
            player.y = ground - player.height
            score['gameScore'] = 0
            lcd.data(True)
            
            break
                    
   

game()
