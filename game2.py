import pygame
import time
import random

pygame.init()
display_width=1080
display_height=720
gameDisplay=pygame.display.set_mode((display_width,display_height))

black=(0,0,0)
white=(255,255,255)
red=(100,0,0)
green=(0,100,0)
bright_green=(0,255,0)
bright_red=(255,0,0)
blue=(0,0,255)

    
Img=pygame.image.load('c4.png')
car_width=78
car_height=91


ltext=pygame.font.SysFont('comicsansms',100)
stext=pygame.font.SysFont('comicsansms',20)


def crash():
    message_display('Andhe')


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if(x+w>mouse[0]>x)and(y+h>mouse[1]>y):
         pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
         if(click[0]==1 and action!=None):
             action()
# =============================================================================
#          if(click[0]==1 and action!=None):
#              if(action=='play'):
#                  game_loop()
#              if(action=='quit'):
#                  pygame.quit()
#                  quit()
# =============================================================================
         
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
            
        #text on Button
    TextSurf,TextRect =text_objects(msg,stext)
    TextRect.center=((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(TextSurf,TextRect)
        
        
def score(count):
    font=pygame.font.SysFont('comicsansms',25)
    text=font.render("Score:"+str(count),True,green)
    gameDisplay.blit(text,(0,0))
    
def message_display(txt):
    TextSurf,TextRect =text_objects(txt,ltext)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()    
    
def car(x,y):
    gameDisplay.blit(Img,(x,y))

def things(thingx,thingy,thingw,thingh,color):
    for i in thingx:
        pygame.draw.rect(gameDisplay,color,[i,thingy,thingw,thingh])
    
pygame.display.set_caption('Gadi wala aaya')

clock=pygame.time.Clock()

def Exit():
    pygame.quit()
    quit()

def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.fill(white)
        TextSurf,TextRect =text_objects('GADI WALA AAYA',ltext)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        #Button1
       
# =============================================================================
#         button('Aarambh',150,600,100,50,green,bright_green,"play")
#         button('Aant',850,600,100,50,red,bright_red,"quit")
# =============================================================================
        button('Aarambh',150,600,100,50,green,bright_green,game_loop)
        button('Aant',850,600,100,50,red,bright_red,Exit)
        
        pygame.display.update()
        clock.tick(15)
    
def game_loop():
    x=display_width*0.45
    y=display_height*0.8
    x_change=0
    y_change=0
    dodged=0
    thing_width=100
    thing_height=100
    thing_num=1
    thing_startx=[random.randrange(0,display_width-thing_width) for i in range(thing_num)]
    thing_starty=-800
    thing_speed=5
    
    
    
    gameExit=False
    
    while not gameExit:
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                quit()
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                elif event.key==pygame.K_RIGHT:
                    x_change=5
                elif event.key==pygame.K_UP:
                    y_change=-5
                elif event.key==pygame.K_DOWN:
                    y_change=5
            
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key== pygame.K_RIGHT or event.key== pygame.K_UP or event.key== pygame.K_DOWN:
                    x_change=0
                    y_change=0
        
        x+=x_change
        y+=y_change   
        gameDisplay.fill(white)
        
        car(x,y)

        things(thing_startx,thing_starty,thing_width,thing_height,blue)
        
        score(dodged)
        
        thing_starty+=thing_speed
    
        if(x>(display_width-car_width) or x<0 or y<0 or y>(display_height-car_height)):
            crash()
        
        if(thing_starty>display_height):
            thing_starty=0-thing_height
            thing_startx=[random.randrange(0,display_width-thing_width,thing_width+1) for i in range(thing_num)]
            dodged+=1
            if((dodged%5)==0):
                thing_speed+=0.7
            
            if((dodged%10)==0):
                thing_num+=1
        
        if y<(thing_starty+thing_height) and y > thing_starty:
            for it in thing_startx :
                if(x>it  and x<it+thing_width) or(x+car_width>it and x+car_width<it+thing_width):
                    crash()
            
        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()