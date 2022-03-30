import os
from xmlrpc.client import boolean
import pygame as pg
import time


cpt = 0        


def plateau_simple(n):
    p = []
    for i in range (n-1):
        for j in range (n-1):
            p.append((i,j))
    return p

def plateau_pond(n):
   p = dict()
   # création de l'echequier qu'on initialise à 8
   for i in range (n+1):
       for j in range (n+1):
           p[i,j] = 8
 
   # on initialise les 6
   for i in range (n+1):
       for j in range (n+1):
           if  i==1 or j==1 or i==n-1 or j==n-1:
              p[i,j] = 6

   # on initialise les 4
   for i in range (n+1):
       for j in range (n+1):
           if  i==0 or j==0 or i==n or j==n:
              p[i,j] = 4
   p[1,1] = 4
   p[n-1,1] = 4
   p[1,n-1] = 4
   p[n-1,n-1] = 4

   # on initialise les coins 2
   p[0,0] = 2
   p[0,n] = 2
   p[n,0] = 2
   p[n,n] = 2

   # on initialise les 3
   p[0,1] = 3
   p[1,0] = 3
   p[0,n-1] = 3
   p[1,n] = 3
   p[n-1,0] = 3
   p[n,1] = 3
   p[n,n-1] = 3
   p[n-1,n] = 3

   return p    

def deplacement(x,y):

    return  tuple(map(lambda i, j: i + j, x, y)) #additione les x et y de deux tuples

def compare(a, n):
    min = 0
    max = n-2
    if(a[0]>=min and a[0]<=max):
        if(a[1]>=min and a[1]<=max):
            return True
    return False
   

def Cavalier(pion, n):
    Sauts = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
    echequier = plateau_pond(n)
    AVisiter = plateau_simple(n)    
    parcours = []
    while (AVisiter != []):
        pond_base = 10 # on met la pondération max a 10
        parcours.append(pion)
        AVisiter.remove(pion)
        for i in range (8): #len Sauts
            if compare(deplacement(pion, Sauts[i]), n) == True: # regarde si le pion ne sort pas du tableau
                x = deplacement(pion, Sauts[i]) # recupere la nouvelle valeur du pion + saut
                if echequier.get(x) != 0: #on ne soustrait pas si il n'y a déjà plus de possibilité
                    echequier[x] = echequier.get(x)-1 # on soustrait la pondération des  valeurs ou peux aller le pion
                if x in AVisiter: # si le nouveau deplacement est dans la liste des sommets a visiter
                    if (echequier[x] < pond_base): # si la pondération de la nouvelle case est infèrieur aux autres ( de base on l'initialise a 10)
                        pond_base = echequier.get(x) # on change la pond pour comparer la pondération de la nouvelle case à la plus petite à l'instant t
                        next_case = x # la prochaine case sera celle avec la pondération la plus faible

        pion = next_case
        presence = False # va servir a voir si on a besoin de refaire un saut en arrière

        while ((pion == parcours[-1] ) or ( presence == True)): 
            pion = parcours[-1] # le pion prend la valeur de la derniere case parcourus
            parcours.pop() # on reprned le dernier element parcourus
            #il a bien été supprimé
            AVisiter.append(pion) # on remet l'ancienne case dans la liste des cases a parcourir
            # il a bien été ajouré

            # On reparcoure les cases possibles du cavalier depuis la case parcours[-1] et on incrémente de 1 chaque pondérations
            for i in range (8): # on parcours toute les posibilite de deplacement
                if compare(deplacement(pion, Sauts[i]), n) == True: # si le deplcaement est dans le tableau
                    z = deplacement(pion, Sauts[i])
                    echequier[z] = echequier.get(z)+1 # on augmente sa ponderation de 1
            for i in range (8):
                if compare(deplacement(pion, Sauts[i]), n) == True:
                    y = deplacement(pion, Sauts[i])                    
                    if echequier.get(y) != 0: 
                        echequier[y] = echequier.get(y)-1 
                    if y in AVisiter: 
                        presence = True #on peux aller visiter ce sommmet donc on change la variable boooléenne
                        if (y != x):
                            if (echequier[y] < pond_base): 
                                pond_base = echequier.get(y) 
                                next_case = y
            pion = next_case


        print("pion :", pion)
        print("Avisiter : ",AVisiter)
    print(pion)
    return parcours


    
def jeu_6(pos, tab):
    pg.init()

    SIZE = 635
    square = 106


    clock = pg.time.Clock()
    screen = pg.display.set_mode((SIZE,SIZE))
    knight = pg.transform.scale(pg.image.load(os.path.join("img", "cavalier.png")), (square, square))
    white_square = pg.transform.scale(pg.image.load(os.path.join("img", "blanc.png")), (square, square))
    blue_square  = pg.transform.scale(pg.image.load(os.path.join("img", "bleu.png")), (square,square))
    red_square  = pg.transform.scale(pg.image.load(os.path.join("img", "rouge.png")), (square,square))

    run = True
    screen.blit(white_square, (0,0))
    screen.blit(white_square, (0,212))
    screen.blit(white_square, (0,424))
    screen.blit(white_square, (212,0))
    screen.blit(white_square, (424,0))
    screen.blit(white_square, (106,106))
    screen.blit(white_square, (318,106))
    screen.blit(white_square, (530,106))
    screen.blit(white_square, (212,212))
    screen.blit(white_square, (424,212))
    screen.blit(white_square, (106,318))
    screen.blit(white_square, (318,318))
    screen.blit(white_square, (530,318))
    screen.blit(white_square, (212,424))
    screen.blit(white_square, (424,424))
    screen.blit(white_square, (106,530))
    screen.blit(white_square, (318,530))
    screen.blit(white_square, (530,530))

    screen.blit(blue_square, (106,0))        
    screen.blit(blue_square, (318,0))
    screen.blit(blue_square, (530,0))
    screen.blit(blue_square, (0,106)) 
    screen.blit(blue_square, (0,318))      
    screen.blit(blue_square, (0,530))  
    screen.blit(blue_square, (212,106))
    screen.blit(blue_square, (424,106))
    screen.blit(blue_square, (106,212))
    screen.blit(blue_square, (318,212))
    screen.blit(blue_square, (530,212))
    screen.blit(blue_square, (212,318))
    screen.blit(blue_square, (424,318))
    screen.blit(blue_square, (106,424))
    screen.blit(blue_square, (318,424))
    screen.blit(blue_square, (530,424))
    screen.blit(blue_square, (212,530))
    screen.blit(blue_square, (424,530))



    screen.blit(knight, pos)
    pg.display.update()

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                quit()
            elif(pg.key.get_pressed()[pg.K_SPACE]):
                    chemin = True
                    for i in range(0, len(tab)):
                        lst_tmp = list(tab[i])
                        for j in range (0, len(lst_tmp)):
                            lst_tmp[j] = lst_tmp[j] * 106
                            pos = lst_tmp
                        pg.display.update()
                        screen.blit(red_square, pos)
                        screen.blit(knight, pos)
                        print("moved")
                        time.sleep(0.2)
                




parcours = [(1,2), (5,4), (2,3)]
# jeu_6((0,0), parcours)
Cavalier((0,0), 9)
