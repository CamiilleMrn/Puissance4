#!/usr/bin/env python
# -*- coding: utf-8 -*-

grille = {  # initialisation du dictionnaire grille
    'pions': {'rouge': [],
              'jaune': []},
    'joueur': 'rouge',
    'mode_jeu': '2joueurs',
    'partie_terminee': False}

lettre = 'F'  # initialisation des variables utilisée plus tard
pion = grille.get('pions')  # raccourcis permettant d'aller chercher directement la liste des pions posée
dernier_pion = 'A1'  # dernier pions joué dans la grille
liste_pion_actualiser = []  #liste des pions a actualiser quand on lance un jokerligneX

def pion_rouge(colone):  # création de la fonction pion rouge
    for k in range(0, len(pion.get(
            'rouge'))):  # on récupère dans le dictionnaire la liste correspondant aux pions joués par le joueur rouge
        a = pion.get('rouge')[k]  # on leur associe une lettre et un chiffre puis on les ajoute dans la liste
        b = int(a[1])
        if b == n_pion:
            colone.append(a)


def pion_jaune(colone):  # Idem mais pour les pions jaunes
    for i in range(0, len(pion.get('jaune'))):
        a = pion.get('jaune')[i]
        b = int(a[1])
        if b == n_pion:
            colone.append(a)


def chars(lettre,
          ligne_afficher):  # création de la fonction chars qui aura pour but de dessiner les X et les O dans la console
    for k in range(1, 8):
        if (str(lettre) + str(k)) in pion.get('rouge'):
            ligne_afficher = ligne_afficher + ' X'
        elif (str(lettre) + str(k)) in pion.get('jaune'):
            ligne_afficher = ligne_afficher + ' O'
        else:
            ligne_afficher = ligne_afficher + ' .'
    ligne_afficher = ligne_afficher + ' |'
    return ligne_afficher


def d_grille(ligne_afficher):  # création de d_grille qui corespond ni plus ni moins qu'à la grille de jeu
    print('| 1 2 3 4 5 6 7 |')
    ligne_afficher = chars('F', ligne_afficher)
    print(ligne_afficher)
    ligne_afficher = '|'
    ligne_afficher = chars('E', ligne_afficher)
    print(ligne_afficher)
    ligne_afficher = '|'
    ligne_afficher = chars('D', ligne_afficher)
    print(ligne_afficher)
    ligne_afficher = '|'
    ligne_afficher = chars('C', ligne_afficher)
    print(ligne_afficher)
    ligne_afficher = '|'
    ligne_afficher = chars('B', ligne_afficher)
    print(ligne_afficher)
    ligne_afficher = '|'
    ligne_afficher = chars('A', ligne_afficher)
    print(ligne_afficher)
    print('| 1 2 3 4 5 6 7 |')


nbr_pion_meme_couleur = 0  # Variable dans laquelle sera stocké le nombre de pion de la même couleur successifs


def verif_point(lettre, num_pion, nbr_pion_meme_couleur,joueur):  # Vérification du nombre de pion d'une même couleur successif
    if (str(lettre) + str(num_pion)) in joueur:
        nbr_pion_meme_couleur += 1
    return nbr_pion_meme_couleur


liste_lettre = ['A', 'B', 'C', 'D', 'E', 'F']  # Variable permettant de changer de lettre avec la fonction changer_lettre


def changer_lettre(lettredebase, liste_lettre,indentation):  # Initialisation d'une fonction permettant de changer la lettre d'entré avec un indice (A + 4 = E, F-2 = D)
    if liste_lettre.index(lettredebase) + indentation >= 0 and (liste_lettre.index(lettredebase) + indentation) <= len(liste_lettre) - 1:
        return liste_lettre[liste_lettre.index(lettredebase) + indentation]
    else:
        return 'Z' #lettre pour empecher de faire la liason entre F et A (F-1 != A)


def joker_ligne(ligne_x, pion, pion2):  # Création de la fonction qui permettra d'utiliser le jokerligneX
    pion2 = pion
    pion = {'rouge': [], 'jaune': []}
    suprimmer_ligne = changer_lettre('A', liste_lettre, ligne_x - 1)

    for f in range(0, 6):
        for k in range(1, 8):
            if changer_lettre('A', liste_lettre, f) + str(k) in pion2.get('rouge') and changer_lettre('A', liste_lettre,f) != suprimmer_ligne:
                if f >= ligne_x:
                    pion.get('rouge').append(changer_lettre('A', liste_lettre, f - 1) + str(k))
                    liste_pion_actualiser.append(changer_lettre('A', liste_lettre, f - 1) + str(k))
                else:
                    pion.get('rouge').append(changer_lettre('A', liste_lettre, f) + str(k))

    for f in range(0, 6):
        for k in range(1, 8):
            if changer_lettre('A', liste_lettre, f) + str(k) in pion2.get('jaune') and changer_lettre('A', liste_lettre,
                                                                                                      f) != suprimmer_ligne:
                if f >= ligne_x:
                    pion.get('jaune').append(changer_lettre('A', liste_lettre, f - 1) + str(k))
                    liste_pion_actualiser.append(changer_lettre('A', liste_lettre, f - 1) + str(k))
                else:
                    pion.get('jaune').append(changer_lettre('A', liste_lettre, f) + str(k))

    return pion


def joker_colonne(colone_y, pion, pion2):  # creation de la fonction qui permet d'utiliser jokercoloneY
    pion2 = pion
    pion = {'rouge': [], 'jaune': []}
    for f in range(0, 6):
        for k in range(0, 8):
            if changer_lettre('A', liste_lettre, f) + str(k) in pion2.get('rouge') and k != colone_y:
                pion.get('rouge').append(changer_lettre('A', liste_lettre, f) + str(k))

    for f in range(0, 6):
        for k in range(0, 8):
            if changer_lettre('A', liste_lettre, f) + str(k) in pion2.get('jaune') and k != colone_y:
                pion.get('jaune').append(changer_lettre('A', liste_lettre, f) + str(k))

    return pion


pion2 = {'rouge': [], 'jaune': []} #permet de modifier pion plus facilement
nb_joker_jrouge = 2  # Nombre de joker par joueur
nb_joker_jjaune = 2
# -----------------------PGM PRCPL------------------------------------

while grille.get('partie_terminee') == False:  # Tant que la partie n'est pas terminée on continue de jouer
    colone = []
    ligne_afficher = '|'

    d_grille(ligne_afficher)
    n_pion = input('Où souhaitez vous jouer ? (ou utiliser un joker avec: "jokerligneX" ou "jokercoloneY") ')

    # Si je joueur rouge entre JokerligneX, alors cette suite lui permet d'exécuter l'action souhaitée
    if grille.get('joueur') == 'rouge':
        if str(n_pion) == "jokerligneX" and nb_joker_jrouge > 0:  # On vérifié que le joueur ait encore un joker dispo
            ligne_erase = int(input('Quelle ligne souhaitez vous effacer ? '))
            pion = joker_ligne(ligne_erase, pion, pion2)  # On appelle la fonction joker_ligne
            nb_joker_jrouge = nb_joker_jrouge - 1  # On retire un joker au joueur
            n_pion = 409734034  #utilisé par le programme nombre a ne pas utiliser
        elif str(n_pion) == "jokerligneX":  # Si je joueur n'a plus de joker disponibles on le lui fait savoir
            print("Vous n'avez plus de joker disponibles")
            if grille.get(
                    'joueur') == 'rouge':  # permet au joueur qui n'a plus de joker de ne pas se faire sauter son tour
                grille['joueur'] = 'jaune'
            else:
                grille['joueur'] = 'rouge'
            n_pion = 409734034
    # Si le joueur rouge entre JokercoloneY
    if grille.get('joueur') == 'rouge':  # Meme procédé mais avec jokercolone
        if str(n_pion) == "jokercoloneY" and nb_joker_jrouge > 0:
            colone_erase = int(input('Quelle colone souhaitez vous effacer ? '))
            pion = joker_colonne(colone_erase, pion, pion2)
            nb_joker_jrouge = nb_joker_jrouge - 1
            n_pion = 409734034
        elif str(n_pion) == "jokercoloneY":
            print("Vous n'avez plus de joker disponibles")
            if grille.get('joueur') == 'rouge':
                grille['joueur'] = 'jaune'
            else:
                grille['joueur'] = 'rouge'
            n_pion = 409734034
    # Si le joueur jaune entre jokerligneX
    if grille.get('joueur') == 'jaune':  # Meme procédé avec le joueur jaune
        if str(n_pion) == "jokerligneX" and nb_joker_jjaune > 0:
            ligne1_erase = int(input('Quelle ligne souhaitez vous effacer ? '))
            pion = joker_ligne(ligne1_erase, pion, pion2)
            nb_joker_jjaune = nb_joker_jjaune - 1
            n_pion = 409734034
        elif str(n_pion) == "jokerligneX":
            print("Vous n'avez plus de joker disponibles")
            if grille.get('joueur') == 'rouge':
                grille['joueur'] = 'jaune'
            else:
                grille['joueur'] = 'rouge'
            n_pion = 409734034
    # si le joueur jaune entre jokercoloneY
    if grille.get('joueur') == 'jaune':  # meme procédé que pour le joueur rouge
        if str(n_pion) == "jokercoloneY" and nb_joker_jjaune > 0:
            colone1_erase = int(input('Quelle colone souhaitez vous effacer ? '))
            pion = joker_colonne(colone1_erase, pion, pion2)
            nb_joker_jjaune = nb_joker_jjaune - 1
            n_pion = 409734034
        elif str(n_pion) == "jokercoloneY":
            print("Vous n'avez plus de joker disponibles")
            if grille.get('joueur') == 'rouge':
                grille['joueur'] = 'jaune'
            else:
                grille['joueur'] = 'rouge'
            n_pion = 409734034
    n_pion = int(n_pion)#transforme n_pion en int sinon n_pion = '409734034' au lieu de n_pion = 409734034

    # Si le joueur n'utilise pas son joker alors, il entre la colone dans laquelle il souhaite jouer, on contrôle à l'entré qu'il ne soit pas en dehors de la grille
    if n_pion > 7 or n_pion < 1:
        # 409 734 034 est le chiffre a ne SURTOUT pas jouer, utilisé par le programme
        if n_pion == 409734034:
            if grille.get('joueur') == 'rouge':  # Permet de changer de joueur à la fin du tour
                grille['joueur'] = 'jaune'
            else:
                grille['joueur'] = 'rouge'
        else:
            print("/!/ Vous ne pouvez pas jouer hors de la grille /!/")  # Patch si le joueur entre un nombre trop grand
            n_pion = 0
        if grille.get('joueur') == 'rouge':  # Mais ne se fait pas sauter son tour
            grille['joueur'] = 'jaune'
        else:
            grille['joueur'] = 'rouge'

    pion_jaune(colone)
    pion_rouge(colone)
    #enregistrer les pions dans rouge ou jaune a partir de n_pion
    if grille.get('joueur') == 'rouge':
        if len(colone) == 0:
            pion.get('rouge').append('A' + str(n_pion)) #On enregistre avec A car la colone numero n_pion est vide, le pion va donc tout en bas
            dernier_pion = ('A' + str(n_pion))  # On utilise alors cette variable pour stocker le dernier pion joué
        if len(colone) == 1:
            pion.get('rouge').append('B' + str(n_pion))
            dernier_pion = ('B' + str(n_pion))
        if len(colone) == 2:
            pion.get('rouge').append('C' + str(n_pion))
            dernier_pion = ('C' + str(n_pion))
        if len(colone) == 3:
            pion.get('rouge').append('D' + str(n_pion))
            dernier_pion = ('D' + str(n_pion))
        if len(colone) == 4:
            pion.get('rouge').append('E' + str(n_pion))
            dernier_pion = ('E' + str(n_pion))
        if len(colone) == 5:
            pion.get('rouge').append('F' + str(n_pion))
            dernier_pion = ('F' + str(n_pion))
        if len(colone) == 6:
            print('Impossible de jouer ici') #la colone est pleine

    else:
        if len(colone) == 0:
            pion.get('jaune').append('A' + str(n_pion))
            dernier_pion = ('A' + str(n_pion))
        if len(colone) == 1:
            pion.get('jaune').append('B' + str(n_pion))
            dernier_pion = ('B' + str(n_pion))
        if len(colone) == 2:
            pion.get('jaune').append('C' + str(n_pion))
            dernier_pion = ('C' + str(n_pion))
        if len(colone) == 3:
            pion.get('jaune').append('D' + str(n_pion))
            dernier_pion = ('D' + str(n_pion))
        if len(colone) == 4:
            pion.get('jaune').append('E' + str(n_pion))
            dernier_pion = ('E' + str(n_pion))
        if len(colone) == 5:
            pion.get('jaune').append('F' + str(n_pion))
            dernier_pion = ('F' + str(n_pion))
        if len(colone) == 6:
            print('Impossible de jouer ici')

    pion = joker_colonne(0, pion, pion2) #efface la colone 0 qui se remplit si un joueur entre un chiffre trop grand
    repeter1fois_au_moins = 1
    # Ici on cherche à derterminer les cas de victoire (incluant lorsqu'un joker a été joué et qu'il permet la victoire) d'ou liste_pion actualiser
    while liste_pion_actualiser != [] or repeter1fois_au_moins == 1: #il faut faire tourner la boucle 1 fois meme si le joker n'a pas ete utilisé et que liste pion actualisé est vide
        if liste_pion_actualiser != []:  #si il y a des pions a actualiser (liste pion actualiser != [])
            dernier_pion = liste_pion_actualiser[0]#on prend le premier
            n_pion = dernier_pion[1]
            liste_pion_actualiser.remove(liste_pion_actualiser[0])#on le suprimme de la liste

        if len(colone) >= 3:  # verification verticale
            nbr_pion_meme_couleur = 0
            if len(colone) >= 5:
                nbr_pion_meme_couleur = verif_point('E', n_pion, nbr_pion_meme_couleur, pion.get(grille.get('joueur')))
            if len(colone) >= 4:
                nbr_pion_meme_couleur = verif_point('D', n_pion, nbr_pion_meme_couleur, pion.get(grille.get('joueur')))
            if len(colone) >= 3:
                nbr_pion_meme_couleur = verif_point('C', n_pion, nbr_pion_meme_couleur, pion.get(grille.get('joueur')))
            if len(colone) <= 4:
                nbr_pion_meme_couleur = verif_point('B', n_pion, nbr_pion_meme_couleur, pion.get(grille.get('joueur')))
            if len(colone) <= 3:
                nbr_pion_meme_couleur = verif_point('A', n_pion, nbr_pion_meme_couleur, pion.get(grille.get('joueur')))

        if nbr_pion_meme_couleur == 3:  # Si le programme detecte 3 pions identiques verticalement alors fin de la partie
            grille['partie_terminee'] = True

        nbr_pion_meme_couleur = 0
        pion_autre_couleur = False
        f = 1
        while pion_autre_couleur == False and f < 4:  # verification gauche
            if (str(dernier_pion[0]) + str(int(n_pion) - int(f))) in pion.get(grille.get('joueur')):
                nbr_pion_meme_couleur += 1
                f += 1
                if nbr_pion_meme_couleur == 3:
                    grille['partie_terminee'] = True
            else:
                pion_autre_couleur = True
        f = 1
        pion_autre_couleur = False
        while pion_autre_couleur == False and f < 4: #verification droite ( s'additione a la gauche)
            if (dernier_pion[0] + str(int(n_pion) + f)) in pion.get(grille.get('joueur')):
                nbr_pion_meme_couleur += 1
                f += 1
                if nbr_pion_meme_couleur == 3:
                    grille['partie_terminee'] = True
            else:
                pion_autre_couleur = True

        # verif diagonale d'une victoire

        nbr_pion_meme_couleur = 0
        pion_autre_couleur = False
        f = 1
        while pion_autre_couleur == False and f < 4:  #verif la diagonale bas gauche
            if (changer_lettre(dernier_pion[0], liste_lettre, -f) + str(int(n_pion) - f)) in pion.get(grille.get('joueur')):
                nbr_pion_meme_couleur += 1
                f += 1

                if nbr_pion_meme_couleur == 3:
                    grille['partie_terminee'] = True
            else:
                pion_autre_couleur = True

        f = 1
        pion_autre_couleur = False
        while pion_autre_couleur == False and f < 4:#verifi la diagonale haut droite
            if (changer_lettre(dernier_pion[0], liste_lettre, f) + str(int(n_pion) + f)) in pion.get(
                    grille.get('joueur')):
                nbr_pion_meme_couleur += 1
                f += 1
                if nbr_pion_meme_couleur == 3:
                    grille['partie_terminee'] = True
            else:
                pion_autre_couleur = True
        # --------------------------------Fin verif diag 1

        # verification diagonale 2
        nbr_pion_meme_couleur = 0
        pion_autre_couleur = False
        f = 1
        while pion_autre_couleur == False and f < 4:  #verifi la diagonale bas droite
            if (changer_lettre(dernier_pion[0], liste_lettre, -f) + str(int(n_pion) + f)) in pion.get(
                    grille.get('joueur')):
                nbr_pion_meme_couleur += 1
                f += 1
                if nbr_pion_meme_couleur == 3:
                    grille['partie_terminee'] = True
            else:
                pion_autre_couleur = True
                if nbr_pion_meme_couleur == 3:
                    grille['partie_terminee'] = True
        if nbr_pion_meme_couleur == 3:
            grille['partie_terminee'] = True
        f = 1
        pion_autre_couleur = False
        while pion_autre_couleur == False and f < 4: #verifie la diagnoale haut gauche
            if (changer_lettre(dernier_pion[0], liste_lettre, f) + str(int(n_pion) - f)) in pion.get(
                    grille.get('joueur')):
                nbr_pion_meme_couleur += 1
                f += 1
                if nbr_pion_meme_couleur == 3:
                    grille['partie_terminee'] = True
            else:
                pion_autre_couleur = True
                if nbr_pion_meme_couleur == 3:
                    grille['partie_terminee'] = True
        repeter1fois_au_moins = 0 #la verification ne se refait pas si il n'y a pas eu de joker joué avant
        if nbr_pion_meme_couleur == 3:
            grille['partie_terminee'] = True
    # ------------------------Fin verif diag 2

    if grille.get('joueur') == 'rouge':  # Changement de joueur
        grille['joueur'] = 'jaune'
    else:
        grille['joueur'] = 'rouge'

if grille.get('joueur') == 'rouge':  #pour annuler le changement de joueur apres une victoire: afficher le gagnant
    grille['joueur'] = 'jaune'
else:
    grille['joueur'] = 'rouge'

d_grille(ligne_afficher)
if grille.get('joueur') == 'rouge':
    print('LA PARTIE EST TERMINEE LE GAGNANT EST : LE JOUEUR ROUGE (les croix)')
else:
    print('LA PARTIE EST TERMINEE LE GAGNANT EST : LE JOUEUR JAUNE (les ronds)')