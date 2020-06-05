import pygame
from time import time, sleep
from random import randint
from jeu import main
from randomizer import randomizer

# Initialisation de Variable
inProgress = True
# Initialisation de pygame
pygame.init()
Fond_Ecran = pygame.display.set_mode((450, 350))  # Taille de la fenetre (en pixel)
pygame.display.set_caption("Mr.Driller")  # Nom de la fenetre
pygame.display.set_icon(pygame.image.load('textures/mrdrillerico.png'))

# Couleurs PYGAME
BLACK = (0, 0, 0)
Vert_Air = (46, 255, 0)
Rouge_Air = (255, 8, 0)
ORANGE = (255, 178, 0)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)

# Initialisation de l'ecran de chargement
Font_Menu = pygame.font.Font("font/marcoozie.ttf", 32)
Fond_Chargement = pygame.image.load("textures/menu/menu_background.png")

# Chargement des images
Fond_Ecran.blit(Font_Menu.render("Chargement des images...", 1, CYAN), (100, 350 / 2))
pygame.display.update()
#############################
## Chargement des Textures ##
#############################
Fond_Menu = pygame.image.load("textures/menu/menu_background2_2.png")
Fond_Settings = pygame.image.load("textures/menu/Settings_background.png")
Fond_Scoreboard = pygame.image.load("textures/menu/Scoreboard_background.png")
World_Menu = pygame.image.load("textures/menu/menu_chargement2.png")
leveldone = pygame.image.load("textures/menu/level_access.png")
Fond_Control = pygame.image.load("textures/menu/Control_background.png")
Rand_Menu = pygame.image.load("textures/menu/randomiser.png")
Victory = [pygame.image.load("textures/menu/Victory1.png"), pygame.image.load("textures/menu/Victory2.png")]
######################
## Fin des Textures ##
######################
Fond_Ecran.blit(Fond_Chargement, (0, 0))

# Chargement des sons
Fond_Ecran.blit(Font_Menu.render("Chargement des sons...", 1, CYAN), (100, 350 / 2))
pygame.display.update()
###########################
## Chargement des Musics ##
###########################
menu = pygame.mixer.Sound("sound/title.ogg")
tululu = pygame.mixer.Sound("sound/sound1.ogg")
back_sd = pygame.mixer.Sound("sound/back.ogg")
error_sd = pygame.mixer.Sound("sound/error.ogg")
newworld_sd = pygame.mixer.Sound("sound/newworld.ogg")
random_sd = pygame.mixer.Sound("sound/randomizer.ogg")
ending_music = pygame.mixer.Sound("sound/ending.ogg")
####################
## Fin des Musics ##
####################
Fond_Ecran.blit(Fond_Chargement, (0, 0))
Fond_Ecran.blit(Font_Menu.render("Chargement...", 1, CYAN), (100, 350 / 2))
pygame.display.update()
######################
## Chargement autre ##
######################
Font_HUD = pygame.font.Font("font/8-Bit.ttf", 32)


#############################
## Fin de Chargement autre ##
#############################
def load(niveau):
    file = open("Save/" + niveau + ".txt", "r")
    liste = []
    map = file.readline().split()
    tour = 0
    for y in range(0, len(map), 6):
        liste.append([])
        for i in range(6):
            liste[tour].append([int(map[y + i])])
        tour += 1
    file.close()
    return liste


def launch(niveau, inProgress, score=0, lives=3):
    while inProgress and niveau != 0 and niveau != "11":
        niveau, inProgress, score, lives = main(niv=load("lvl_" + niveau), level=niveau, score=int(score), lives=lives)
    if niveau == "11":
        Fond_Ecran.blit(Victory[0], (0, 0))
        pygame.display.update()
        ending_music.play(-1)
        sleep(1)
        tempV = True
        while inProgress:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if 328 < pos[0] < 328 + 106 and 286 < pos[1] < 286 + 49 and tempV:
                        Fond_Ecran.blit(Victory[1], (0, 0))
                        pygame.display.update()
                        tempV = False
                        sleep(1)
                    elif 328 < pos[0] < 328 + 106 and 286 < pos[1] < 286 + 49 and tempV == False:
                        menu.play(-1)
                        ending_music.stop()
                        return True
                if event.type == pygame.QUIT:
                    return False
    if inProgress:
        menu.play(-1)
    return inProgress


def Randomiser_Menu(inProgress):
    Fond_Ecran.blit(Rand_Menu, (0, 0))
    pygame.display.update()
    while inProgress:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if 132 < pos[0] < 164 and 78 < pos[1] < 78 + 35:
                    randomizer(1)
                    random_sd.play()
                elif 193 < pos[0] < 193 + 37 and 75 < pos[1] < 75 + 39:
                    randomizer(2)
                    random_sd.play()
                elif 279 < pos[0] < 279 + 38 and 77 < pos[1] < 77 + 35:
                    randomizer(3)
                    random_sd.play()
                elif 129 < pos[0] < 129 + 31 and 128 < pos[1] < 128 + 38:
                    randomizer(4)
                    random_sd.play()
                elif 200 < pos[0] < 233 and 133 < pos[1] < 164:
                    randomizer(5)
                    random_sd.play()
                elif 284 < pos[0] < 284 + 32 and 133 < pos[1] < 167:
                    randomizer(6)
                    random_sd.play()
                elif 129 < pos[0] < 129 + 32 and 193 < pos[1] < 193 + 33:
                    randomizer(7)
                    random_sd.play()
                elif 202 < pos[0] < 235 and 193 < pos[1] < 193 + 33:
                    randomizer(8)
                    random_sd.play()
                elif 285 < pos[0] < 285 + 30 and 191 < pos[1] < 191 + 30:
                    randomizer(9)
                    random_sd.play()
                elif 195 < pos[0] < 195 + 54 and 246 < pos[1] < 246 + 36:
                    randomizer(10)
                    random_sd.play()
                elif 0 < pos[0] < 93 and 207 < pos[1] < 350:
                    # print("Back")
                    back_sd.play()
                    Fond_Ecran.blit(Fond_Settings, (0, 0))
                    pygame.display.update()
                    return True
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Fond_Ecran.blit(Fond_Settings, (0, 0))
                pygame.display.update()
                back_sd.play()
                return True
    return False


def Scoreboard_Screen(inProgress):
    Fond_Ecran.blit(Fond_Scoreboard, (0, 0))
    try:
        saveFile = open("Save/scoreboard.txt", "r")
        save = saveFile.readlines()
    except:
        Fond_Ecran.blit(Fond_Settings, (0, 0))
        pygame.display.update()
        print("Erreur de lecture")
        error_sd.play()
        return True
    for i in range(1, len(save)):
        Fond_Ecran.blit(Font_Menu.render(str(save[i])[:-1], 1, ORANGE), (178, 37 + (30 * i)))
    pygame.display.update()
    while inProgress:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if 0 < pos[0] < 93 and 207 < pos[1] < 350:
                    # print("Back")
                    back_sd.play()
                    Fond_Ecran.blit(Fond_Settings, (0, 0))
                    pygame.display.update()
                    return True
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Fond_Ecran.blit(Fond_Settings, (0, 0))
                pygame.display.update()
                back_sd.play()
                return True
    return False


def Controles_Screen(inProgress):
    Fond_Ecran.blit(Fond_Control, (0, 0))
    pygame.display.update()
    while inProgress:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if 0 < pos[0] < 93 and 207 < pos[1] < 350:
                    # print("Back")
                    back_sd.play()
                    Fond_Ecran.blit(Fond_Settings, (0, 0))
                    pygame.display.update()
                    return True
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                back_sd.play()
                Fond_Ecran.blit(Fond_Settings, (0, 0))
                pygame.display.update()
                return True
    return False


def Settings_Screen(inProgress):
    while inProgress:
        Fond_Ecran.blit(Fond_Settings, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                # print(pygame.mouse.get_pos())
                pos = pygame.mouse.get_pos()
                if 158 < pos[0] < 158 + 134 and 90 < pos[1] < 90 + 38:
                    # print("Scoreboard")
                    tululu.play()
                    inProgress = Scoreboard_Screen(inProgress)
                elif 155 < pos[0] < 155 + 134 and 204 < pos[1] < 246:
                    # print("Controles")
                    tululu.play()
                    inProgress = Controles_Screen(inProgress)
                elif 157 < pos[0] < 157 + 135 and 150 < pos[1] < 185:
                    # print("Randomiser")
                    tululu.play()
                    inProgress = Randomiser_Menu(inProgress)
                elif 0 < pos[0] < 93 and 207 < pos[1] < 350:
                    # print("Back")
                    Fond_Ecran.blit(Fond_Menu, (0, 0))
                    pygame.display.update()
                    back_sd.play()
                    return True
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                back_sd.play()
                Fond_Ecran.blit(Fond_Menu, (0, 0))
                pygame.display.update()
                return True
    return False


def World_Screen(inProgress):
    Fond_Ecran.blit(World_Menu, (0, 0))
    try:
        saveFile = open("Save/scoreboard.txt", "r")
        save = int(saveFile.read(1))
    except:
        Fond_Ecran.blit(Fond_Menu, (0, 0))
        pygame.display.update()
        print("Erreur de lecture")
        error_sd.play()
        return True
    level = 0
    for i in range(0, save + 1):
        if i == 9:
            Fond_Ecran.blit(leveldone, (204, 256))
            Fond_Ecran.blit(Font_Menu.render(str(i + 1), 1, Rouge_Air), (214, 268))
        else:
            Fond_Ecran.blit(leveldone, (135 + ((i - (level * 3)) * 70), 69 + (level * 62)))
            Fond_Ecran.blit(Font_Menu.render(str(i + 1), 1, Rouge_Air),
                            (150 + ((i - (level * 3)) * 70), 81 + (level * 62)))
        if i + 1 in range(3, 9, 3):
            level = (i + 1) / 3
    pygame.display.update()
    while inProgress:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                # print(pygame.mouse.get_pos())
                pos = pygame.mouse.get_pos()
                if 0 < pos[0] < 93 and 207 < pos[1] < 350:
                    Fond_Ecran.blit(Fond_Menu, (0, 0))
                    pygame.display.update()
                    back_sd.play()
                    return True
                else:
                    level = 0
                    for i in range(0, save + 1):
                        if i == 9 and 204 < pos[0] < 246 and 256 < pos[1] < 296:  # 42 40
                            # chargement niveau 10
                            # print("Chargement du niveau 10")
                            tululu.play()
                            menu.fadeout(1000)
                            inProgress = launch("10", inProgress)
                            return inProgress
                        else:
                            if save >= (i) and (135 + ((i - (level * 3)) * 70)) < pos[0] < (
                                    135 + ((i - (level * 3)) * 70)) + 42 and 69 + (level * 62) < pos[1] < 69 + (
                                    level * 62) + 40:
                                # chargement du niveau i+1
                                # print("Chargement du niveau: "+str(i+1))
                                level = i + 1
                                tululu.play()
                                menu.fadeout(1000)
                                inProgress = launch(str(i + 1), inProgress)
                                return inProgress
                        if i + 1 in range(3, 9, 3):
                            level = (i + 1) / 3
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Fond_Ecran.blit(Fond_Menu, (0, 0))
                pygame.display.update()
                return True
    return False


def Menu(inProgress):
    menu.play(-1)
    while inProgress:
        Fond_Ecran.blit(Fond_Menu, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                # print(pygame.mouse.get_pos())
                pos = pygame.mouse.get_pos()
                if 67 < pos[0] < 202 and 176 < pos[1] < 242:
                    newworld_sd.play()
                    menu.fadeout(1000)
                    inProgress = launch("1", inProgress)
                    # chargement du niveau 1
                elif 247 < pos[0] < 383 and 203 < pos[1] < 246:
                    # print("Charger")
                    tululu.play()
                    inProgress = World_Screen(inProgress)
                elif 152 < pos[0] < 295 and 271 < pos[1] < 314:
                    # print("Quitter")
                    menu.fadeout(1000)
                    inProgress = False
                elif 403 < pos[0] < 450 and 0 < pos[1] < 47:
                    # print("Settings")
                    tululu.play()
                    inProgress = Settings_Screen(inProgress)
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return False
    return False


# Boucle de jeu principale
while inProgress:
    inProgress = Menu(inProgress)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inProgress = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            inProgress = False

pygame.quit()
