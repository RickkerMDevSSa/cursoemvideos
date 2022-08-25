# Programa que reproduz mp3

import pygame

pygame.init()
pygame.mixer.music.load('hino-nacional-brasileiro-mp3')
pygame.mixer.music.play()
pygame.event.wait()


#by Rickker Marques