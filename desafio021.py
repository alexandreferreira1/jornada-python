# Abrir e executar um áudio MP3

import pygame
import time

pygame.mixer.init()
# r significa uma string bruta, assim a barra invertida não altera nada. Também pode usar barra dupla
pygame.mixer.music.load(r'D:\Documentos\Arquivos\Alexandre\Músicas\Storge 2 - Meu Mundo 2008\01 Viver pra Ti.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)