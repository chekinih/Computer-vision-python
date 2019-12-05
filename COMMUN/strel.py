__author__ = 'chaussard'

import numpy as np
from operator import itemgetter
import math


# Fonction permettant de construire un element structurant
# Il faut choisir le type (disque, carre, diamant, ligne)
# Puis le parametre de taille et, dans le cas de la ligne, le parametre d'angle
# L'element structurant est donne sous forme de liste de coordonnees
def build_as_list(type, size, angle):
    if (type == 'disque'):
        Strel = []  # Le resultat sera une liste de coordonnees
        # On parcourt tous les pixels entre -size et size pour tester si le disque passerait par le pixel : si oui, on l'allume
        for x in range(-((np.int)(size)) - 1, ((np.int)(size)) + 2):
            for y in range(-((np.int)(size)) - 1, ((np.int)(size)) + 2):
                if ((abs(x) - 0.5) * (abs(x) - 0.5) + (abs(y) - 0.5) * (abs(y) - 0.5) <= size * size):
                    Strel.append((y, x))

    elif (type == 'carre'):
        # On place dans le resultat toutes les coordonnees entre -size et size inclus
        Strel = [(y, x) for x in range(-size, size + 1) for y in range(-size, size + 1)]

    elif (type == 'diamant'):
        # On parcourt ligne par ligne pour ajouter les segments qu'il faut
        Strel = [(i, j) for i in range(-size, size + 1) for j in range(-size + abs(i), size - abs(i) + 1)]


    elif (type == 'ligne'):
        Strel = []
        # Une ligne
        d = size
        a = angle

        # On place l'angle dans un intervalle entre 90 et -90
        while (a > 90):
            a = a - 180
        while (a < -90):
            a = a + 180
        # Si l'angle est superieur a 45deg, on retire 90def et on tournera le resultat obtenu...
        rot = 0
        if (a > 45):
            a = a - 90
            rot = 1
        elif (a < -45):
            a = a + 90
            rot = 3;
        # Conversion de l'angle en radian
        a = a * math.pi / 180
        # Petite conversion pour ramener l'angle par rapport au coin inferieur gauche de l'ecran
        a = -a

        # Calcul de la taille de l'element structurant en fonction de d
        lx = int(math.ceil(d / math.sqrt(1 + math.tan(a) * math.tan(a))))
        if (lx == 0):
            lx = 1
        ly = int(math.ceil(d * math.tan(abs(a)) / math.sqrt(1 + math.tan(a) * math.tan(a))))
        if (ly == 0):
            ly = 1

        # Allocation du resultat
        Strel = []

        # Algo de Bresenham
        for x in range(-lx, lx + 1):
            y = math.tan(a) * x;
            Strel.append((int(round(y)), x))

        # Si nous devons tourner le resultat...
        if (rot > 0):
            # La rotation s'effectue avec une transposee puis un flip horizontal
            for i in range(0, len(Strel)):
                Strel[i] = (-Strel[i][1], Strel[i][0])

    else:
        assert (False), type + " n'est pas un nom d'element structurant valide pour cette fonction."

    return Strel


# Fonction permettant de construire un element structurant
# Il faut choisir le type (disque, carre, diamant, ligne)
# Puis le parametre de taille et, dans le cas de la ligne, le parametre d'angle
# L'element structurant est donne sous forme d'une image
def build(type, size, angle=0):
    return toImage(build_as_list(type, size, angle))


# Fonction permettant de construire une image a partir d'une liste de points d'un element structurant
def toImage(Strel):
    if len(Strel) == 0:
        assert (False), "L element structurant donne en parametre est vide (trop petit)."

    # On recupere les plus grandes et petites coordonnees de l'element structurant
    max_i = max(Strel, key=itemgetter(0))[0]
    min_i = min(Strel, key=itemgetter(0))[0]
    max_j = max(Strel, key=itemgetter(1))[1]
    min_j = min(Strel, key=itemgetter(1))[1]

    # On alloue l'image de sortie
    Im = np.zeros([max_i - min_i + 1, max_j - min_j + 1, 1], np.uint8)

    for (i, j) in Strel:
        Im[i + abs(min_i), j + abs(min_j)] = 255

    return Im

