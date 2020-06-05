import os
import pygame


def import_sprite_car():
    path = "../"
    fichier = os.listdir(path)

    list_image = []

    for i in range(0,len(fichier)):


        if fichier[i][:3]=="car":

            list_image.append(fichier[i])


    return list_image

            
def creation_data_image(u):

    
    list_image = import_sprite_car()
    list_img_car = []
    for i in range(0,len(list_image)):

        k = pygame.image.load("../"+str(list_image[i]))
        k = pygame.transform.scale(k,(u,u))
        list_img_car.append(k)


    return list_img_car,list_image
    
