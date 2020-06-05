import pygame, sys
from pygame.locals import *
import import_img
import Save_import



class Couleur:


    def __init__ (self):

        self.fond = (46, 49, 49, 1)
        self.red = (255,0,0,1)


couleur = Couleur()


class User:

    def __init__(self):

        self.selected_block_sprite = 0
        self.position_liste = 5
        self.save_file_name = None


class Map:

    def __init__(self):

        self.current_map = []


class Rectangle:

    def __init__ (self,x_depart,y_depart,largeur,hauteur,name):

        self.x_depart = x_depart
        self.y_depart = y_depart
        self.largeur = largeur
        self.hauteur = hauteur
        self.name = name
        
    def rect_data(self):

        return self.x_depart,self.y_depart,self.largeur,self.hauteur


class Text:

    def __init__(self,text,x,y,texte_size):

        self.text = text
        self.x = x
        self.y = y
        self.texte_size = texte_size
        
        fontobj = pygame.font.Font('freesansbold.ttf',self.texte_size)
        textesurface = fontobj.render(self.text,True,couleur.red,couleur.fond)
        self.textesurface = textesurface
        
        textrect = textesurface.get_rect()
        textrect.topleft = (self.x,self.y)
        self.textrect = textrect

    def changement_de_text(self,text):
        self.text = text

class Tile_img:

    def __init__(self, x, y, u, sprite, name):

        self.x = x
        self.y = y
        self.u = u
        self.sprite = sprite
        self.name = name


def main(u=40):

    hauteur_fenetre = 500
    largeur_fenetre = 720

    pygame.init()

    # relier a la fenetre
    ma_surface = pygame.display.set_mode((largeur_fenetre,hauteur_fenetre))
    pygame.display.set_caption('MR.driller Editeur')
    fpsClock = pygame.time.Clock()
    fps = 60

    # random var
    map = Map()
    user = User()

    # initialisation des different rectangle
    rectangle_centre = Rectangle(x_depart=240,
                                 y_depart=70,
                                 largeur=240,
                                 hauteur=360,
                                 name="centre")

    rectangle_select = Rectangle(x_depart=10,
                                 y_depart=70,
                                 largeur=160,
                                 hauteur=360,
                                 name="select")

    rectangle_plus = Rectangle(x_depart=500,
                               y_depart=175,
                               largeur=50,
                               hauteur=50,
                               name="plus")

    rectangle_moins = Rectangle(x_depart=500,
                                y_depart=275,
                                largeur=50,
                                hauteur=50,
                                name="moins")

    rectangle_position = Rectangle(x_depart=500,
                                   y_depart=225,
                                   largeur=50,
                                   hauteur=50,
                                   name="position")

    rectangle_load = Rectangle(x_depart=580,
                               y_depart=350,
                               largeur=100,
                               hauteur=50,
                               name="load")
    
    rectangle_save = Rectangle(x_depart=580,
                               y_depart=400,
                               largeur=100,
                               hauteur=50,
                               name="save")

    # initialisation des different texte
    load_text = Text(text='Load',
                     x=602,
                     y=363,
                     texte_size=25)

    save_text = Text(text='Save',
                     x=602,
                     y=412,
                     texte_size=25)

    plus_text = Text(text="+",
                     x=512,
                     y=176,
                     texte_size=45)

    moin_text = Text(text = "-",
                     x = 516,
                     y = 278,
                     texte_size = 45)

    letter_text = Text(text="Selected block",
                       x=580,
                       y=220,
                       texte_size=15)


    # liste objet

    liste_rectangle = [rectangle_centre,
                       rectangle_select,
                       rectangle_plus,
                       rectangle_moins,
                       rectangle_position,
                       rectangle_load,
                       rectangle_save]

    liste_text = [save_text,load_text,plus_text,moin_text,letter_text]

    # importation des images dossier ../

    list_img_car,list_img = import_img.creation_data_image(u)
    print(list_img_car,list_img)
    
    # generation des objet a partir des image(tuile) pour la partie selection
    list_tile = []
    largeur_rangee = 0
    y_rangee = 0

    for i in range(0,len(list_img)):

        k = list_img[i].replace(".png","")
        
        k = Tile_img(x=rectangle_select.x_depart+(i%4)*u,
                     y=rectangle_select.y_depart+y_rangee*u,
                     u=u,
                     sprite=list_img_car[i],
                     name=list_img[i])

        list_tile.append(k)
        
        largeur_rangee += 1
        if largeur_rangee == 4:

            y_rangee += 1
            largeur_rangee = 0

    # generation des block pour le tableau centre

    list_car_centre = []
    list_name_car_centre = []
    for x in range(0, int(rectangle_centre.hauteur / u)):
        for i in range(0, int(rectangle_centre.largeur/u)):

            k = Rectangle(x_depart=(i*u)+rectangle_centre.x_depart,
                          y_depart=(x*u)+rectangle_centre.y_depart,
                          largeur=u,
                          hauteur=u,
                          name=("car_centre_"+str(x)+str(i)))

            list_car_centre.append(k)
            list_name_car_centre.append(k.name)

    print(list_car_centre)
    print(list_name_car_centre)
    # objet selected block

    selected_block = Tile_img(x=610,
                              y=250,
                              u=u,
                              sprite=user.selected_block_sprite,
                              name='selected block')

    # generation de la liste
    for i in range(0,9):
        map.current_map.append([])
        for x in range(0,6):
            map.current_map[i].append(0)

    print(map.current_map)

    def ajout_ligne_liste(liste):

        liste.append([])
        for x in range(0, 6):
            liste[len(liste)-1].append(0)
        return liste


    # hit box gestion 
    def hitbox(mouse_pos,liste_rectangle):


        def hitbox_general(mouse_pos):

            if ((mouse_pos[0] >= liste_rectangle[i].x_depart and
                 mouse_pos[0] <= liste_rectangle[i].x_depart + liste_rectangle[i].largeur) and
                    (mouse_pos[1] >= liste_rectangle[i].y_depart and
                     mouse_pos[1] <= liste_rectangle[i].y_depart + liste_rectangle[i].hauteur)):

                return True

        def hitbox_select(mouse_pos):

            if ((mouse_pos[0] >= list_tile[x].x and
                 mouse_pos[0] <= list_tile[x].x + list_tile[i].u) and
                    (mouse_pos[1] >= list_tile[x].y and
                     mouse_pos[1] <= list_tile[x].y + list_tile[i].u)):

                return True

        def hitbox_centre(mouse_pos):

            if ((mouse_pos[0] >= list_car_centre[x].x_depart and
                 mouse_pos[0] <= list_car_centre[x].x_depart + list_car_centre[i].largeur) and
                    (mouse_pos[1] >= list_car_centre[x].y_depart and
                     mouse_pos[1] <= list_car_centre[x].y_depart + list_car_centre[i].hauteur)):
                return True


        for i in range(0,len(liste_rectangle)):

            if hitbox_general(mouse_pos):
                
                print(liste_rectangle[i].name)

                if liste_rectangle[i].name == "select":

                    for x in range(0,len(list_tile)):
                        
                        if hitbox_select(mouse_pos):
                            
                            print("i :x ",list_tile[x].x)
                            print(list_tile[x].name)
                            user.selected_block_sprite = x



                if liste_rectangle[i].name == "centre":

                    for x in range(0,len(list_car_centre)):

                        if hitbox_centre(mouse_pos):

                            k = list_car_centre[x].name
                            ligne = user.position_liste - 5 + int(k[11])
                            colonne = int(k[12])
                            map.current_map[ligne][colonne] = user.selected_block_sprite

                if liste_rectangle[i].name == "plus":

                    if len(map.current_map)>=user.position_liste+4:
                        map_edit = ajout_ligne_liste(liste = map.current_map)
                        user.position_liste+=1

                if liste_rectangle[i].name == "moins":

                    if user.position_liste>5:
                        user.position_liste -=1

                if liste_rectangle[i].name == "load":

                    map.current_map,user.save_file_name = Save_import.save_select()

                if liste_rectangle[i].name == "save":
                    user.save_file_name = Save_import.create_save_file(map=map.current_map, previous_file=user.save_file_name )



        print(user.position_liste,"pos liste")



    def letter_pos(text):
        letter_position_list = Text(text=str(text),
                                    x=510,
                                    y=240,
                                    texte_size=20)
        return letter_position_list

    letter_position_list = letter_pos(str(user.position_liste))

    ###############################################################
    # boucle jeu
    boucle_jeu = True
    while boucle_jeu:

        for event in pygame.event.get():
            if event.type == QUIT:
                boucle_jeu = False

            if event.type ==MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()

                print("mouse position",mouse_pos)
                hitbox(mouse_pos,liste_rectangle)
                letter_position_list = letter_pos(str(user.position_liste))

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    print("key left")
                if event.key == K_RIGHT:
                    print("key right")
                if event.key == K_DOWN:
                    print("key down")

        ########################################################
        # zone affichage


        #layer fond
        ma_surface.fill(couleur.fond)

        for i in range(0,len(liste_rectangle)):
            pygame.draw.rect(ma_surface,couleur.red,(liste_rectangle[i].rect_data()),1)


        for i in range(0,len(list_tile)):
            ma_surface.blit(list_tile[i].sprite,(list_tile[i].x,list_tile[i].y))

        ma_surface.blit(list_tile[user.selected_block_sprite].sprite, (selected_block.x,selected_block.y))

        
        p=0
        for i in range(user.position_liste-5,user.position_liste+4):

            for x in range(0,6):
                ma_surface.blit(list_tile[map.current_map[i][x]].sprite, (rectangle_centre.x_depart+u*x, rectangle_centre.y_depart+u*p))
            p+=1


        ### affichage carrer centre
        for i in range(0,len(list_car_centre)):
            pygame.draw.rect(ma_surface, couleur.red, (list_car_centre[i].rect_data()), 1)


        #### affichage des different text non modifiable
        for i in range(0, len(liste_text)):
            ma_surface.blit(liste_text[i].textesurface, liste_text[i].textrect)


        ### affichage text modiable
        ma_surface.blit(letter_position_list.textesurface, letter_position_list.textrect)

        #### affichage block selectionner
        ma_surface.blit(list_tile[user.selected_block_sprite].sprite, (selected_block.x, selected_block.y))


        pygame.display.update()
        fpsClock.tick(fps)

    pygame.quit()


main()


