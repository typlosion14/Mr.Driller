import pygame
import sys

sys.path.append("../")


def creation_data_image(u):
    path = "textures/blocs/"
    liste_image = ["vide", "car_bleu", "car_rouge", "car_vert", "car_jaune","car_diamant",
                   "car_diamant1","car_diamant2","car_diamant3","car_diamant4","car_pierre_dur",
                   "car_pierre_dur1","car_pierre_dur2","car_pierre_dur3","car_pierre_dur4",
                   "car_rocher","car_rocher1","car_rocher2","car_rocher3","car_rocher4"
                  , "car_oxy","car_oxy1","car_oxy2","car_oxy3",
                   "carre_destru_bleu0","carre_destru_bleu1", "carre_destru_bleu2",
                   "carre_destru_bleu3",

                # 28
                    "carre_destru_rouge0","carre_destru_rouge1", "carre_destru_rouge2",
                   "carre_destru_rouge3",
               #32
                   "carre_destru_vert0","carre_destru_vert1", "carre_destru_vert2",
                   "carre_destru_vert3",
                #36
                   "carre_destru_jaune0","carre_destru_jaune1", "carre_destru_jaune2",
                   "carre_destru_jaune3","carre_fin_niv" ]
    liste_data_image = ["vide", ]

    for i in range(1,len(liste_image)):
        k = pygame.image.load((path + liste_image[i] + ".png"))
        k = pygame.transform.scale(k, (u, u))
        liste_data_image.append(k)

    return liste_data_image


##  liste char [idle 0, left 1, up 2, right 3, down 4]
##                               |
##                               ^
##                      [up 1, up 2,up 3, up4]



def creation_data_sprite():
    path = "textures/personnage/"
    mouvement = [["idle", "char_idle"],
                 ["climbing_left", "climbing_left_0", "climbing_left_1", "climbing_left_2"],
                 ["climbing_right", "climbing_right_0", "climbing_right_1", "climbing_right_2"],
                 ["drilling_down", "drilling_down_0", "drilling_down_1", "drilling_down_2", "drilling_down_3"],
                 ["drilling_left", "drilling_left_0", "drilling_left_1"],
                 ["drilling_right", "drilling_right_0", "drilling_right_1"],
                 ["drilling_up", "drilling_up_0", "drilling_up_1", "drilling_up_2", "drilling_up_3"],
                 ["walking_left", "walking_left_0", "walking_left_1", "walking_left_2", "walking_left_3"],
                 ["walking_right", "walking_right_0", "walking_right_1", "walking_right_2", "walking_right_3"],
                 ["angel","angel0","angel1","angel2"],
                 ["falling","falling_0","falling_1"]]

    data_sprite = {}

    for i in range(0, len(mouvement)):
        liste_provisoire = []
        for x in range(1, len(mouvement[i])):
            k = pygame.image.load((path + mouvement[i][x] + ".png"))
            k = pygame.transform.scale2x(k)
            liste_provisoire.append(k)

        data_sprite[mouvement[i][0]] = liste_provisoire


    return data_sprite
