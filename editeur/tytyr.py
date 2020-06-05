
import pygame,sys
from pygame.locals import *

class Text :

    def __init__(self,text):

        self.text = text


    def text_affich(self):
        
        fontobj = pygame.font.Font('freesansbold.ttf',48)
        textesurface = fontobj.render(self.text,True,couleur.red,couleur.fond)
        textrect = textesurface.get_rect()
        textrect.topleft = (100,100)

        return textesurface,textrect



        
