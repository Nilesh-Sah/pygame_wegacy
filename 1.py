import pygame  #imports the feature of pygame 

from sys import exit #imported a specific part from the module 

pygame.init()  #starts pygame, initiates subpart of pygame that you need to make a game; starting part of engine 

screen=pygame.display.set_mode((800,400))  #creates the display 
pygame.display.set_caption('Legacy') #title name of the game  
#these above three lines of code (1,3,7) gets executed and the window does not gets closed so we have to do something to keep the game's window
#this is why we will create a while loop 

while True:   #This loop won't stop because it's condition won't be false so we have to break the loop from inside 
#draw all our element 
#update everything
    for event in pygame.event.get(): # pygame.event.get()= this will get the event, for event in= this loops through all of them 
        if event.type==pygame.QUIT:  # pygame.quit is synonyms to the cross button of the window
            pygame.quit()  #makes the cross button clickable; works after the click, pygame.quit is the opposite to pygame.init 
            # pygame.quit() is the exact opposite of pygame.init() so the game gets closed as the latest code is pygame.quit()   
            # this is why we need to import a specific part from a module(from sys import exit)
            exit() #closes the loop of while true which is very useful as there would be shown error messages without this
    pygame.display.update()  #this updates the 5th line of code as we have to update variuos element inside this game

#pygame.quit() is the exact opposite of pygame.init() so the game gets closed as the latest code is pygame.quit()
#this is why we need to import a module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            