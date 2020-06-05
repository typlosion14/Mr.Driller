from random import *
# 1 2 3 4 = blocs de couleurs
# 5 = Crystal
# 10 = caisse
# 15 = blance
# 21 = oxy
def randomizer(lvl=2):
    aleatoire=[1,2,3,4,5,10,15,21,1,2,3,4,21,1,2,3,4]
    board=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    for i in range(lvl-1):
        aleatoire.extend([1,2,3,4,5,10,15,1,2,3,4])
        if i<=5:
            aleatoire.append(21)
    taille=lvl*100*6
    board.extend([choice(aleatoire) for i in range(taille)])
    while len(board)%6!=0:
        board.append(choice(aleatoire))
    board.extend([40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40])
    board=[str(i) for i in board]
    board=str(" ".join(board))
    file = open("Save/lvl_"+str(lvl)+".txt","w")
    file.write(board)
    file.close()
randomizer()
