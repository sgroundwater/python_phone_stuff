import time, sys, pygame
from pygame import mixer

import pygame
import time

pygame.init()
pygame.mixer.init()
sounda= pygame.mixer.Sound("../FUN_sounds/dial_tone.wav")

sounda.play()
time.sleep (20)
