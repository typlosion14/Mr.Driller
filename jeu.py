import pygame, sys
from pygame.locals import *
import random
from time import time, sleep
from random import randint
from map import sprite_import

# delai d'animation est du a l'animation du blcok lorsqu'il ce detruit   : il faut faire une exception dusur c'est bloques index_block_destru

niv = 1
data_sprite = sprite_import.creation_data_sprite()
# Couleurs PYGAME
BLACK = (0, 0, 0)
Vert_Air = (46, 255, 0)
Rouge_Air = (255, 8, 0)
ORANGE = (255, 178, 0)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)

sound_detect = False
debut = time()
pygame.init()
ma_surface = pygame.display.set_mode((450, 350))
pygame.display.set_caption('MR.driller')
fpsClock = pygame.time.Clock()
fps = 60
# Initialisation de l'ecran de chargement
Font_Menu = pygame.font.Font("font/marcoozie.ttf", 32)
Fond_Chargement = pygame.image.load("textures/menu/menu_background.png")

# Chargement des images
ma_surface.blit(Font_Menu.render("Chargement des images...", 1, CYAN), (100, 350 / 2))
pygame.display.update()
#############################
## Chargement des Textures ##
#############################
game_bg = pygame.image.load("textures/menu/game_background200.png")
img_live = pygame.image.load("textures/menu/live.png")
img_sign = pygame.image.load("textures/menu/sign.png")
Pause_Menu = pygame.image.load("textures/menu/pause.png")
######################
## Fin des Textures ##
######################
ma_surface.blit(Fond_Chargement, (0, 0))

# Chargement des sons
ma_surface.blit(Font_Menu.render("Chargement des sons...", 1, CYAN), (100, 350 / 2))
pygame.display.update()
###########################
## Chargement des Musics ##
###########################
tululu = pygame.mixer.Sound("sound/sound1.ogg")
back_sd = pygame.mixer.Sound("sound/back.ogg")
error_sd = pygame.mixer.Sound("sound/error.ogg")
Warning_Air = pygame.mixer.Sound("sound/sonic.ogg")
recovery = pygame.mixer.Sound("sound/recovery.ogg")
bg_music = pygame.mixer.Sound("sound/fond.ogg")
death = [pygame.mixer.Sound("sound/death1.ogg"), pygame.mixer.Sound("sound/death2.ogg")]
fall_sd = pygame.mixer.Sound("sound/fall.ogg")
box_sd = pygame.mixer.Sound("sound/box.ogg")
step_sd = pygame.mixer.Sound("sound/steps.ogg")
star_sd = pygame.mixer.Sound("sound/star.ogg")
bloc_sd = pygame.mixer.Sound("sound/blocks.ogg")
oxy_sd = pygame.mixer.Sound("sound/oxy.ogg")

####################
## Fin des Musics ##
####################
ma_surface.blit(Fond_Chargement, (0, 0))
ma_surface.blit(Font_Menu.render("Chargement...", 1, CYAN), (100, 350 / 2))
pygame.display.update()
######################
## Chargement autre ##
######################
Font_HUD = pygame.font.Font("font/8-Bit.ttf", 32)


#############################
## Fin de Chargement autre ##
#############################
def saveScore(score):
    File=open("Save/scoreboard.txt","r+") #6
    contenu=File.readlines()
    File.close()
    Final=[]
    taille=len(contenu)
    if len(contenu)>6:
        taille=6
    else:
        taille=len(contenu)
    if len(contenu)!=1: #Alors le fichier ne contient pas de scores
        Final.append(contenu[0]) # on ecrit la save
        for i in range(1,taille):
            if int(contenu[i][:-1])<score and Final.count(str(score)+"\n")==0:
                Final.append(str(score)+"\n")#on ecrit le score si il est pas deja dans le scoreboard
                Final.append(contenu[i])
            else:
                Final.append(contenu[i])#on ecrit les scores superieurs ou restant
    else: # on ecrit la save et le nouveau score
        Final.append(contenu[0])
        Final.append(str(score)+"\n")
    File=open("Save/scoreboard.txt","w")
    File.write("".join(Final))
    File.close()


def Hud_Update(debut, ma_surface, AirT, AirM, lives, score, pos, level, sound_detect, char):
    # Affichage Profondeur
    ma_surface.blit(game_bg, (0, 0))
    affichage = str(pos)
    for i in range(0, 5 - len(affichage)):
        affichage = "0", str("".join(affichage))
    ma_surface.blit(Font_HUD.render(str("".join(affichage)), 1, (255, 178, 0)), (323, 39))
    # Affichage Score
    affichage = str(score)
    for i in range(0, 6 - len(affichage)):
        affichage = "0", str("".join(affichage))  # 323 263
    ma_surface.blit(Font_HUD.render(str("".join(affichage)), 1, Rouge_Air), (290, 105))
    # Affichage Niveau
    ma_surface.blit(Font_HUD.render(str(level), 1, WHITE), (340, 260))
    # Affichage Air
    if time() - debut >= 1:
        AirT += AirM - 1
        debut = time()
    if AirT > 100:
        AirT = 100
    elif AirT <= 0:

        ma_surface.blit(Font_HUD.render("00", 1, Rouge_Air), (402, 169))
        sound_detect = False
        char.lives=revive(ma_surface, lives)
        char.angel = True
        char.angel_x = char.x
        AirT = 100
    elif 0 < AirT <= 12:
        if not sound_detect:
            Warning_Air.play()
            sound_detect = True
        Drawing_Air(ma_surface, AirT, Rouge_Air)
    else:
        sound_detect = False
        Warning_Air.stop()
        Drawing_Air(ma_surface, AirT, Vert_Air)
    # Affichage Vie
    for i in range(0, lives):
        ma_surface.blit(img_live, (378 - (i * 40), 326))
    return debut, sound_detect, AirT, lives


def Drawing_Air(ma_surface, AirT, COLOR):
    for i in range(0, AirT * 2):
        # 2*14 = 1% #445 195
        pygame.draw.line(ma_surface, COLOR, (445 - (i - 1), 195), (445 - (i - 1), 208))
        pygame.draw.line(ma_surface, COLOR, (445 - i, 195), (445 - i, 208))
    if len(str(AirT)) >= 2:
        ma_surface.blit(Font_HUD.render(str(AirT), 1, COLOR), (399, 169))
    else:
        affichage = "0", str(AirT)
        ma_surface.blit(Font_HUD.render(str("".join(affichage)), 1, COLOR), (399, 169))


def revive(ma_surface, lives):
    # Affichage Vie
    lives -= 1
    for i in range(0, lives):
        ma_surface.blit(img_live, (378 - (i * 40), 326))
    # sound de mort
    Warning_Air.fadeout(100)
    death[randint(0, 1)].play()
    if lives <= 0:  # GAME OVER
        temp = True
        ma_surface.blit(img_sign, (8, 160))
        ma_surface.blit(Font_Menu.render("  GAME OVER", 1, Rouge_Air), (100, 165 + 16))
        pygame.display.update()
        sleep(.500)
        while temp:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    temp = False

        return lives
    else:
        text = "    Il te reste ", str(lives), " vies."  # affichage vie restante
        temp = True
        ma_surface.blit(img_sign, (8, 160))
        ma_surface.blit(Font_Menu.render(str("".join(text)), 1, CYAN), (10, 165))
        ma_surface.blit(Font_Menu.render("  Appuyez pour continuer...", 1, CYAN), (10, 165 + 32))
        pygame.display.update()
        sleep(.500)
        while temp:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    temp = False
        recovery.play()
        return lives


rerun = False


def main(u=40, niv=niv, level=1, score=0, lives=3):
    class Couleur:

        def __init__(self):
            self.white = (255, 255, 255, 1)
            self.fond = (46, 49, 49, 1)
            self.red = (255, 0, 0, 1)

    class Board:

        def __init__(self, niv):
            self.map = niv
            self.index_block_destru = [24, 25, 26, 27]
            self.index_block_destru_rouge = [28, 29, 30, 31]
            self.index_block_destru_vert = [32, 33, 34, 35]
            self.index_block_destru_jaune = [36, 37, 38, 39]
            self.block_with_hitbox = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 40]
            self.diamand_index = [6, 7, 8, 9]
            self.oxygene_index = [20, 21, 22, 23]
            self.pierre_index = [11, 12, 13, 14]
            self.rocher_index = [16, 17, 18, 19]
            self.list_moving_block = []
            self.list_oxygene_block = []
            self.block_fin_jeu = [40]
            self.position_char = 0
            # format [x,y]
            self.giggle = []

        #  ["vide",
        #  1 - 4 "car_bleu", "car_rouge", "car_vert", "car_jaune",
        #   5 - 9 "car_diamant", "car_diamant1", "car_diamant2", "car_diamant3", "car_diamant4",
        #   10 - 15 "car_pierre_dur", "car_pierre_dur1", "car_pierre_dur2", "car_pierre_dur3", "car_pierre_dur4",
        #   16 - 20"car_rocher", "car_rocher1", "car_rocher2", "car_rocher3", "car_rocher4"
        #  21 - 24, "car_oxy", "car_oxy1", "car_oxy2", "car_oxy3",
        #   25 - 28 "carre_destru_bleu0", "carre_destru_bleu1", "carre_destru_bleu2" "carre_destru_bleu3"]

        def giggle_creation(self):
            self.giggle = [-1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, - 1, -1, -1, 1, 1, 1,
                           -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1,
                           -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1,
                           1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1,
                           -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1,
                           -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1,
                           1, 1, 1]

        def cordonne_block_board(self, board):

            for i in range(len(board)):
                for x in range(len(board[i])):
                    k = board[i][x][0]
                    if k==  10:
                        board[i][x] = [k, (x * 40), (i * 40), 0, 0, 0, 5]
                    else:
                        board[i][x] = [k, (x * 40), (i * 40), 0, 0, 0, 0]

            self.map = board

        def ajout_destru_block(self, y, x):
            self.map[y][x][3] = "destru"

        def delete_block(self, y, x):
            self.map[y][x][0] = 0

        def transform_block(self, y, x, index_sprite):
            self.map[y][x][0] = self.index_block_destru[index_sprite]

        def animation_destruction_block_et_oxygene(self):

            for y in range(self.position_char - 3, self.position_char + 5):
                for x in range(len(self.map[y])):

                    if self.map[y][x][3] == "destru":
                        if self.map[y][x][4] >= 8:
                            self.map[y][x][5] += 1
                            self.map[y][x][4] = 0
                            if self.map[y][x][5] >= 4:
                                self.map[y][x][0] = 0
                                self.map[y][x][3] = 0
                            else:
                                if 5 <= self.map[y][x][0] <= 9:
                                    self.map[y][x][0] = self.diamand_index[self.map[y][x][5]]
                                elif 10 <= self.map[y][x][0] <= 14:
                                    self.map[y][x][0] = self.pierre_index[self.map[y][x][5]]
                                elif 15 <= self.map[y][x][0] <= 19:
                                    self.map[y][x][0] = self.rocher_index[self.map[y][x][5]]
                                elif self.map[y][x][0] == 2 or self.map[y][x][0] in self.index_block_destru_rouge:
                                    self.map[y][x][0] = self.index_block_destru_rouge[self.map[y][x][5]]
                                elif self.map[y][x][0] == 3 or self.map[y][x][0] in self.index_block_destru_vert:
                                    self.map[y][x][0] = self.index_block_destru_vert[self.map[y][x][5]]
                                elif self.map[y][x][0] == 4 or self.map[y][x][0] in self.index_block_destru_jaune:
                                    self.map[y][x][0] = self.index_block_destru_jaune[self.map[y][x][5]]
                                else:
                                    self.map[y][x][0] = self.index_block_destru[self.map[y][x][5]]
                        else:
                            self.map[y][x][4] += 1

                    if 20 <= self.map[y][x][0] <= 23:
                        if self.map[y][x][4] >= 20:
                            self.map[y][x][5] += 1
                            self.map[y][x][4] = 0
                            if self.map[y][x][5] >= 4:
                                self.map[y][x][5] = 0
                            else:
                                self.map[y][x][0] = self.oxygene_index[self.map[y][x][5]]
                        else:
                            self.map[y][x][4] += 1

        def update(self):

            self.animation_destruction_block_et_oxygene()
            self.changement_position_block()
            self.mouv_block_list_moving_block()

        def check_block_with_hotbox(self, y, x):
            k = self.map[y][x][0]
            for i in self.block_with_hitbox:
                if k == i:
                    return True

            return False

        def check_block(self, y, x):
            if self.map[y][x][0] != 0 and self.check_block_with_hotbox(y, x) and self.map[y][x][
                0] not in self.list_oxygene_block:
                return True

        def check_block_in_list_moving_block(self, y, x):
            for i in self.list_moving_block:
                if i[0] == y and i[1] == x:
                    return True
            return False

        def add_and_check_moving_block(self, y, x):

            if not self.check_block_in_list_moving_block(y, x):
                self.list_moving_block.append([y, x, 0, 0])

        def check_for_void(self, y, x):

            if self.map[y + 1][x][0] == 0 or self.map[y + 1][x][0] not in self.block_with_hitbox and self.map[y + 1][x][
                0] not in self.oxygene_index:
                #  if (x - 1 >= 0 and self.map[y][x - 1][0] != self.map[y][x][0]) and (
                # x + 1 < len(self.map[y]) and self.map[y][x + 1][0] != self.map[y][x][0]):
                self.add_and_check_moving_block(y, x)

            # if x - 1 == -1 and self.map[y][x + 1][0] != self.map[y][x][0]:
            #   self.add_and_check_moving_block(y, x)

            #   if x + 1 == len(self.map[y]) and self.map[y][x - 1][0] != self.map[y][x][0]:
            #    self.add_and_check_moving_block(y, x)

        def changement_position_block(self):
            if self.position_char - 5 > 2:
                for y in range(self.position_char - 5, self.position_char + 5):
                    for x in range(len(self.map[y])):

                        if self.map[y][x][0] != 0 and self.map[y][x][
                            0] in self.oxygene_index or self.check_block_with_hotbox(y, x):
                            self.check_for_void(y, x)

        def mouv_block_list_moving_block(self):
            list_index = 0
            for i in self.list_moving_block:
                if i[3] >= 120:
                    if i[2] >= 40:
                        self.map[i[0] + 1][i[1]][0] = self.map[i[0]][i[1]][0]
                        self.map[i[0] + 1][i[1]][1] = self.map[i[0]][i[1]][1]
                        self.map[i[0] + 1][i[1]][2] = self.map[i[0]][i[1]][2]
                        self.map[i[0] + 1][i[1]][3] = self.map[i[0]][i[1]][3]
                        self.map[i[0] + 1][i[1]][4] = self.map[i[0]][i[1]][4]
                        self.map[i[0] + 1][i[1]][5] = self.map[i[0]][i[1]][5]
                        self.map[i[0] + 1][i[1]][6] = self.map[i[0]][i[1]][6]

                        self.map[i[0]][i[1]] = [0, i[2] * 40, i[1] * 40, 0, 0, 0, 0]

                        if self.map[i[0] + 2][i[1]][0] == 0:
                            self.list_moving_block[list_index] = [i[0] + 1, i[1], 0, 120]
                        else:
                            del self.list_moving_block[list_index]

                    else:

                        i[2] += 4
                        self.map[i[0]][i[1]][2] += 4
                    list_index += 1
                else:

                    i[3] += 1
                    self.map[i[0]][i[1]][1] += self.giggle[i[3]]

    copie_map = niv
    map = Board(niv)
    # mise en place des cordonée de la map
    map.cordonne_block_board(map.map)
    map.giggle_creation()

    class Char:

        def __init__(self, u):

            # cordonnée
            self.x = 125
            self.y = 160
            self.score = score
            self.size_of_steps = 3
            self.lives = lives
            self.air = 100

            # hitbox char
            self.hitbox_bottom = ((self.x, 160 + 32), (30, 10)),
            self.hit_left = ((self.x - 5, 160 + 5), (5, 30)),
            self.hit_right = ((self.x + 30, 160 + 5), (5, 30))
            self.hit_top = ((self.x + 2, 160 + 8), (28, 5))
            self.emplacement_y = int(self.y / 40)
            self.emplacement_x = int(self.x / 40)

            self.sprite = data_sprite["idle"][0]
            self.map = map.map
            self.close_box = []

            self.direction = "down"

            # animation
            # nombre de pas par animation
            self.step = 0
            self.step_for_sprite = 0
            self.index_of_sprite = 0
            self.name_of_sprite = "idle"

            # angel for data
            self.angel = False
            self.angel_frame = 0
            self.angel_index = 0
            self.angel_sprite = data_sprite["angel"][0]
            self.angel_x = 0
            self.angel_y = self.y

            self.game_state = True

            # animation creuse

            self.drilling = False
            self.drilling_frame = 0
            self.drilling_index = 0


            # animation tombe

            self.falling = False
            self.falling_frame = 0
            self.falling_index = 0
            self.falling_size = 0

            self.waiting_time = 0


        def changement_sprite(self, sprite, index):
            self.sprite = data_sprite[sprite][index]

        def actualisation_emplacement_y(self):
            self.emplacement_y = int(self.y / 40)

        def actualisation_emplacement_x(self):
            self.emplacement_x = int((self.x + 10) / 40)

        def check_for_collide(self, rect):

            rect = pygame.Rect(rect)
            for i in range(len(self.close_box)):
                i = (self.close_box[i][0][0], self.close_box[i][0][1], self.close_box[i][1][0], self.close_box[i][1][1])
                i = pygame.Rect(i)
                if pygame.Rect.colliderect(i, rect):
                    return True

        def step_animation(self):

            def step_and_check(step, step_for_sprite, index_of_sprite):
                step += 1
                if step == step_for_sprite:
                    index_of_sprite += 1
                    step = 0

                return step, step_for_sprite, index_of_sprite

            if self.direction == "left":
                step_sd.play()
                self.step_for_sprite = 5
                self.step, self.step_for_sprite, self.index_of_sprite = step_and_check(step=self.step,
                                                                                       step_for_sprite=self.step_for_sprite,
                                                                                       index_of_sprite=self.index_of_sprite)
                if self.index_of_sprite < len(data_sprite["walking_left"]):
                    self.changement_sprite("walking_left", self.index_of_sprite)
                else:
                    self.index_of_sprite = 0

            if self.direction == "right":
                step_sd.play()
                self.step_for_sprite = 5
                self.step, self.step_for_sprite, self.index_of_sprite = step_and_check(step=self.step,
                                                                                       step_for_sprite=self.step_for_sprite,
                                                                                       index_of_sprite=self.index_of_sprite)
                if self.index_of_sprite < len(data_sprite["walking_right"]):
                    self.changement_sprite("walking_right", self.index_of_sprite)
                else:
                    self.index_of_sprite = 0

            if self.direction == "down":
                self.changement_sprite("idle", 0)

            if self.direction == "up":
                self.changement_sprite("drilling_up", 0)

        def check_for_oxygene(self):
            if map.oxygene_index[0] <= map.map[self.emplacement_y][self.emplacement_x][0] <= map.oxygene_index[-1]:
                map.delete_block(self.emplacement_y, self.emplacement_x)
                self.air += 20
                oxy_sd.play()

        def check_oxygene_block(self):

            def check_if_in_list_oxygene(y, x, list):

                for i in list:
                    if i[0] == y and i[1] == x:
                        return True
                return False

            for y in range(self.emplacement_y - 5, self.emplacement_y + 5):
                for x in range(len(map.map[y])):
                    if map.oxygene_index[0] <= map.map[y][x][0] <= map.oxygene_index[-1]:

                        if not check_if_in_list_oxygene(y, x, map.list_oxygene_block):
                            map.list_oxygene_block.append([y, x, self.map[y][x][0], 0, 0, ])

        def key_left(self):

            self.direction = "left"

            self.step_animation()
            if self.x > 0 and not self.check_for_collide(self.hit_left):
                self.x -= self.size_of_steps
                self.actualisation_emplacement_x()
                self.check_for_oxygene()

        def key_right(self):

            self.direction = "right"
            self.step_animation()

            if self.x < 210 and not self.check_for_collide(self.hit_right):
                self.x += self.size_of_steps
                self.actualisation_emplacement_x()
                self.check_for_oxygene()

        def look_down(self):
            self.direction = "down"
            self.step_animation()

        def look_up(self):
            self.direction = "up"
            self.step_animation()

        def check_if_rocher(self, y, x, liste=map.map):
            if liste[y][x][0] == 10:  # Check si c'est une caisse
                self.air -= 20
                box_sd.play()
            elif liste[y][x][0] == 5:  # Check si c'est un crystal
                star_sd.play()
            elif liste[y][x][0] in (1, 2, 3, 4, 15): #check si c'est un bloc classique
                bloc_sd.play()

        def x_press(self):

            def nav_mouv(mouv):
                for i in mouv:
                    map.ajout_destru_block(i[0], i[1])

            if self.direction == "left":

                y = self.emplacement_y
                x = self.emplacement_x - 1

                if x >= 0 and map.check_block(y, x) and not map.map[y][x][3] == "destru":

                    if self.waiting_time<= 0:
                        self.drilling = True
                        if char.waiting_time == 0:
                            char.waiting_time = 20
                            if map.map[y][x][6]<= 0:


                                mouv = self.check_for_merged_block(y, x)
                                self.check_if_rocher(y, x, liste=map.map)
                                nav_mouv(mouv)
                                self.score += 10
                            else:
                                map.map[y][x][6] -=1




                    self.score += 10
            if self.direction == "right":

                y = self.emplacement_y
                x = self.emplacement_x + 1
                if x < len(map.map[y]) and map.check_block(y, x) and not map.map[y][x][3] == "destru":

                    if self.waiting_time <= 0:
                        self.drilling = True
                        if char.waiting_time == 0:
                            char.waiting_time = 20
                            if map.map[y][x][6] <= 0:

                                mouv = self.check_for_merged_block(y, x)
                                self.check_if_rocher(y, x, liste=map.map)
                                nav_mouv(mouv)
                                self.score += 10
                            else:
                                map.map[y][x][6] -= 1

            if self.direction == "down":

                y = self.emplacement_y + 1
                x = self.emplacement_x

                if map.map[y][x][0] in map.block_fin_jeu:
                    self.game_state = False
                else:
                    if map.check_block(y, x) and not map.map[y][x][3] == "destru":
                        if self.waiting_time <= 0:
                            self.drilling = True
                            if char.waiting_time == 0:
                                char.waiting_time = 20
                                if map.map[y][x][6] <= 0:

                                    mouv = self.check_for_merged_block(y, x)
                                    self.check_if_rocher(y, x, liste=map.map)
                                    nav_mouv(mouv)
                                    self.score += 10
                                else:
                                    map.map[y][x][6] -= 1
            if self.direction == "up":
                y = self.emplacement_y - 1
                x = self.emplacement_x

                if map.check_block(y, x) and not map.map[y][x][3] == "destru":
                    if self.waiting_time <= 0:
                        self.drilling = True
                        if char.waiting_time == 0:
                            char.waiting_time = 20
                            if map.map[y][x][6] <= 0:

                                mouv = self.check_for_merged_block(y, x)
                                self.check_if_rocher(y, x, liste=map.map)
                                nav_mouv(mouv)
                                self.score += 10
                            else:
                                map.map[y][x][6] -= 1

        def falling_animation(self):
            if self.falling == True:
                self.falling_size += 1
                if self.falling_size >= 13:
                    if self.falling_frame >= 7:
                        fall_sd.play()
                        self.falling_index += 1
                        self.falling_frame = 0
                    if self.falling_index >= len(data_sprite["falling"]):
                        self.falling_index = 0
                    else:
                        self.sprite = data_sprite["falling"][self.falling_index]
                        self.falling_frame += 1

        def gravity(self):

            if not self.check_for_collide(self.hitbox_bottom):
                self.falling = True
                self.falling_animation()
                for y in range(len(map.map)):
                    for x in range(len(map.map[y])):
                        map.map[y][x][2] -= 4

                self.y += 4
                if self.angel == True:
                    self.angel_y -= 4

                self.score += 1
                self.actualisation_emplacement_y()
                self.check_for_oxygene()

            elif self.falling == True:
                self.falling = False
                fall_sd.stop()
                self.falling_size = 0
                self.sprite = data_sprite["idle"][0]

        def close_box_creation(self):

            self.close_box = []
            for y in range(int(self.y / 40 - 2), int(self.y / 40 + 2)):
                for x in range(int(self.x / 40) - 2, int(self.x / 40 + 2)):
                    if x < len(self.map[y]) and x >= 0 and self.map[y][x][0] != 0 and map.check_block_with_hotbox(y, x):
                        self.close_box.append([(self.map[y][x][1], self.map[y][x][2]), (40, 40)])

        def envoie_position_char(self):
            map.position_char = self.emplacement_y

        def top_colision(self):
            if self.check_for_collide(self.hit_top):
                for y in range(0, self.emplacement_y + 1):
                    for x in range(self.emplacement_x - 1, self.emplacement_x + 2):
                        if x >= 0 and x < len(map.map[y]):
                            map.map[y][x][0] = 0
                self.lives = revive(ma_surface, self.lives)
                self.air = 100
                self.angel = True
                self.angel_x = self.x

        def angel_animation(self):
            if self.angel == True:
                self.angel_frame += 1
                if self.angel_frame >= 10:
                    self.angel_index += 1
                    self.angel_frame = 0
                if self.angel_index >= 3:
                    self.angel_index = 0
                self.angel_y -= 1
                self.angel_sprite = data_sprite["angel"][self.angel_index]

                if self.angel_y <= -60:
                    self.angel = False
                    self.angel_y = 160

        def check_for_merged_block(self, y_block, x_block):

            def check_if_in_mouv(mouv, y, x):
                for i in mouv:
                    if i == [y, x]:
                        return True
                return False

            mouv = [[y_block, x_block]]

            for i in mouv:
                ind = [[i[0] - 1, i[1]], [i[0], i[1] - 1], [i[0], i[1] + 1], [i[0] + 1, i[1]]]

                for j in ind:
                    if 0 <= j[1] < len(map.map[j[0]]) and map.map[j[0]][j[1]][0] == map.map[y_block][x_block][
                        0] and not check_if_in_mouv(mouv, j[0], j[1]):
                        mouv.append([j[0], j[1]])
            return mouv




        def update(self):
            self.envoie_position_char()
            self.hitbox_bottom = ((self.x, 160 + 32), (30, 10)),
            self.hit_left = ((self.x - 5, 160 + 5), (5, 30)),
            self.hit_right = ((self.x + 30, 160 + 5), (5, 30))
            self.hit_top = ((self.x + 2, 160 + 8), (27, 5))
            if self.waiting_time>0:
                self.waiting_time -= 1
            # check collision carre top personnage if true die
            self.top_colision()

            if self.drilling:
                if self.drilling_frame >= 5:
                    self.drilling_frame = 0
                    self.drilling_index += 1

                if self.drilling_index >= len(data_sprite["drilling" + "_" + self.direction]):
                    self.drilling_index = 0
                    self.drilling_frame = 0
                    self.drilling = False
                    self.sprite = data_sprite["idle"][0]
                else:
                    self.drilling_frame += 1
                    self.sprite = data_sprite["drilling" + "_" + self.direction][self.drilling_index]




            self.angel_animation()

            self.gravity()
            self.close_box_creation()
            self.check_oxygene_block()

    sound_detect = False
    debut = time()
    # relier a la fenetre

    fpsClock = pygame.time.Clock()
    fps = 60

    # data map ///from sprite_import
    liste_data_image = sprite_import.creation_data_image(u)
    char = Char(u)

    # sprite init
    couleur = Couleur()

    pygame.key.set_repeat(1, 0)

    # boucle jeu
    boucle_jeu = True
    bg_music.play(-1)
    while boucle_jeu == True:

        for event in pygame.event.get():
            if event.type == QUIT:
                boucle_jeu = False
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    char.key_left()
                elif event.key == K_RIGHT:
                    char.key_right()
                elif event.key == K_DOWN:
                    char.look_down()
                elif event.key == K_UP:
                    char.look_up()
                elif event.key == K_x:

                    char.x_press()


                elif event.key == (K_ESCAPE or K_p):
                    ma_surface.blit(Pause_Menu, (0, 0))
                    pygame.display.update()
                    temp = True
                    pygame.mixer.pause()
                    sleep(.500)
                    while temp:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                boucle_jeu = False
                                temp = False
                            elif event.type == pygame.MOUSEBUTTONUP:
                                pos = pygame.mouse.get_pos()
                                if (63 < pos[0] < 63 + 113 and 146 < pos[1] < 146 + 27):  # Continue
                                    temp = False
                                    tululu.play()
                                    sleep(.500)
                                    pygame.mixer.unpause()
                                elif (63 < pos[0] < 63 + 113 and 179 < pos[1] < 179 + 24):  # Reset
                                    bg_music.stop()
                                    tululu.play()
                                    return level, True, 0, 3
                                elif (63 < pos[0] < 63 + 113 and 211 < pos[1] < 211 + 24):  # Quit (Retour au Menu)
                                    bg_music.stop()
                                    tululu.play()
                                    Warning_Air.stop()
                                    return 0, True, char.score, char.lives
                            elif event.type == KEYDOWN and event.key == K_ESCAPE:  # Continue
                                sleep(.500)
                                pygame.mixer.unpause()
                                temp = False

        # Passage de niveau
        if not char.game_state:
            bg_music.stop()
            level = str(level)
            try: #creation de la save
                SaveFile = open("Save/scoreboard.txt", "r+")
                save = int(SaveFile.read(1))
                if save < int(level) and save!=9:
                    SaveFile.seek(0)
                    SaveFile.write(str(level)+"\n")
            except:
                SaveFile = open("Save/scoreboard.txt", "w")
                SaveFile.write(str(level)+"\n")
            SaveFile.close()
            return str(int(level)+1), True, char.score, char.lives

        if char.lives <= 0:# Mort du personnage
            sound_detect = False
            saveScore(char.score)
            bg_music.stop()
            Warning_Air.stop()
            return 0, True, char.score, 0

        debut, sound_detect, char.air, lives = Hud_Update(debut, ma_surface, char.air, 0, char.lives, char.score,
                                                          char.emplacement_y,
                                                          level,
                                                          sound_detect, char)

        for y in range(char.emplacement_y - 6, char.emplacement_y + 6):
            for x in range(len(map.map[y])):
                for i in range(1, len(liste_data_image)):
                    if map.map[y][x][0] == i:
                        ma_surface.blit(liste_data_image[i], (map.map[y][x][1], map.map[y][x][2]))
        ma_surface.blit(char.sprite, (char.x, 160))

       # for y in range(len(char.close_box)):
         #   pygame.draw.rect(ma_surface, couleur.red, char.close_box[y], 1)

        # affihage rectangle hitbox
      #  pygame.draw.rect(ma_surface, couleur.red, char.hitbox_bottom, 1)
      #  pygame.draw.rect(ma_surface, couleur.red, char.hit_left, 1)
      #  pygame.draw.rect(ma_surface, couleur.red, char.hit_right, 1)
      #  pygame.draw.rect(ma_surface, couleur.red, char.hit_top, 1)
        if char.angel == True:
            ma_surface.blit(char.angel_sprite, (char.angel_x - 10, char.angel_y))

        map.update()
        char.update()
        pygame.display.update()
        fpsClock.tick(fps)
    return 0, False, char.score, char.lives
