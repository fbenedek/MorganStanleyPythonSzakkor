# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 08:17:24 2020

@author: Benedek
"""

import pygame #grafikus felülethez
import random #az izgalomhoz

#pygame grafikus felület indítása
pygame.init()

#milyen nagy legyen az ablak, amire rajzolgatunk?
windowHeigth = 500
windowWidth = 500


#ablak init: innen már megnézhetjük
win = pygame.display.set_mode((windowHeigth,windowWidth))

#kis feliratunk is legyen
pygame.display.set_caption("AgarIO")

#honnan indulok?
startX = windowWidth // 2 #egész eredmény kell - különben megharagszik
startY = windowHeigth // 2 

#töltsük be a helyünket jelző változóba!
x = startX
y = startY

#milyen sugárral indulok?
radius = 20

#és mekkora a cél?
goalRadius = 50

#milyen gyorsan mehetek?
vel = 5

#eledelek tulajdonságai
numOfEledels = 8
eledelSize = 5
cycleToErase = 100

#színek, "RGB" színtérben
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0) 
blue = (0, 0, 128) 

#textInit
font = pygame.font.Font('freesansbold.ttf', 32)

textNyertel = font.render('Nyertel!', True, green, blue) 
textRectNyertel = textNyertel.get_rect() 
textRectNyertel.center = (windowWidth // 2, windowHeigth // 2) 
        
textVesztettel = font.render(':c', True, green, blue)
textRectVesztettel = textVesztettel.get_rect() 
textRectVesztettel.center = (windowWidth // 2, windowHeigth // 2)

display_surface = pygame.display.set_mode((windowWidth, windowHeigth)) 
        
#legyen egy listában tárolva az, hogy hány eledem van hol!
eledelXList = []
eledelYList = []

#töltsük föl ezt a listát - véletlenszerűen!
for i in range(numOfEledels):
    eledelX = random.randint(1, windowWidth)
    eledelXList.append(eledelX)
    eledelY = random.randint(1, windowHeigth)
    eledelYList.append(eledelY)
    
#indulhat a játék!
run = True
numCycle = 0
while run:
    pygame.time.delay(50) #FPS?
    
    #valamikor vége is legyen...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #mit nyomkodunk?
    keys = pygame.key.get_pressed()     
    
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    
    #megvan minden infó ami kell.
    #jöhet a megjelenítés!

    #fekete ablak - stílus az első
    win.fill((0,0,0))
    
    #kell eltüntetni bigyót?
    remove = False
    
    #megtaláltam-e egy bigyót?
    scored = False
    
        
    #először rajzoljuk le az eledeleket - így tűnnek el, ha átmegyünk rajtuk!
    for i in range(len(eledelXList)):
        #végigmegyünk a listájukon, és kirajzolgatjuk őket a circle-el
        pygame.draw.circle(win, white, (eledelXList[i],eledelYList[i]),eledelSize)
        
        #ha bármelyiknek is a közelében vagyok, legyen eltüntetve, és nőjön a pontom
        if abs(eledelXList[i]-x)<radius/2 and abs(eledelYList[i]-y)<radius/2:
            removeX = eledelXList[i]
            removeY = eledelYList[i]
            remove = True
            scored = True
            
    if numCycle%cycleToErase == 99:
        if len(eledelXList) > 0:
            indexToRemove = random.randint(0,len(eledelXList)-1)
            removeX = eledelXList[indexToRemove]
            removeY = eledelYList[indexToRemove]
            remove = True
    
    if remove:
        eledelXList.remove(removeX)
        eledelYList.remove(removeY)
        
        if scored:
            radius += 5
            
    if radius >= goalRadius:
        display_surface.blit(textNyertel, textRectNyertel)
        
    elif len(eledelXList) == 0:
        display_surface.blit(textVesztettel, textRectVesztettel)
        
    
            
    pygame.draw.circle(win, red, (x,y),radius)
    pygame.draw.circle(win, white, (x,y),goalRadius, 2)
    pygame.display.update()
    numCycle +=1
    
pygame.quit()