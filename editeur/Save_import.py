import os



def save_select():


    def selected_value(value,list):

        if value>=0 and value<len(list):
            return True

    path = "../Save_map"
    fichier = os.listdir(path)

    if len(fichier) == 0:
        print("Aucune sauvegarde de map")
    else:
        for i in range(len(fichier)):
            print(i, fichier[i])

        while True:
            try:
                select = int(input("selectionner votre sauvegarde"))
                break
            except ValueError:
                print("la valeur n'est pas un int")

        if selected_value(value=select, list=fichier):

            file = open(path+"/"+fichier[select],"r")
            liste = []


            map = file.readline()
            print(len(map))
            tour = 0
            for y in range(0, len(map), 6):
                liste.append([])
                for i in range(6):
                    liste[tour].append(int(map[y+i]))
                tour+=1



            print(liste)


            file.close()

            return liste,fichier[select]





def creation_of_save(filename,map):
    path = "../Save_map"
    print(filename[len(filename)-4:len(filename)])
    if filename[len(filename)-4:len(filename)]!=".txt":
        file = open(path+"/"+filename+".txt","w+")
    else:
        file = open(path + "/" + filename, "w+")

    for i in map:

        for x in i:

            file.write(str(x))

    file.close()

def create_save_file(map, previous_file):

    print("\in dev/")

    # random value

    save_state = False
    check = True
    while check:
        save_name = input("name save file or default is gonna be applied")

        if save_name == "!q":
            print("quitting save mode")
            check = False


        elif save_name != "":


            if save_name == "s":

                if previous_file == None:
                    previous_file = save_name
                    print("no previous file")
                    save_state = False
                    check = False

                else:
                    print("saving in previous file")
                    save_name = previous_file
                    check = False
                    save_state = True

            else:
                check = False
                save_state = True



    if save_state:
        print("save state ", save_state)
        creation_of_save(filename=save_name, map=map)

    else:
        print("save cancel")


    return previous_file




