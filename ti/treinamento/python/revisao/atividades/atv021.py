import pygame

# Inicializar o mixer e o pygame
pygame.init()
pygame.mixer.init()

# Carregar a música
pygame.mixer.music.load('./reliable-safe-327618.mp3')

# Tocar a música
pygame.mixer.music.play()