import pygame
import time
import os

pygame.init()
pygame.mixer.init()

window=pygame.display.set_mode((0,0),pygame.FULLSCREEN)

music=pygame.mixer.Sound(os.path.join("Assets","music.mp3"))
music.play()

for i in range(10,-1,-1):
    filename="count"+str(i)+".png"
    image=pygame.image.load(os.path.join("Assets",filename))
    window.blit(image,(0,0))
    pygame.display.update()
    time.sleep(1)
time.sleep(10)
