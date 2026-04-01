#
#
#
#
#
# Ne pas supprimer cette ligne. <trace>tictactoe.py</trace>

####################
# Jeu du Tic Tac Toe
####################

from random import randint
from random import random
from time import sleep

def initiation_grille() -> list[list[str]]:
    """ créer un grille 3x3 vide (liste de liste)
    Précondition : /
    Exemple(s) :
    $$$ initiation_grille()
    [['', '', ''], ['', '', ''], ['', '', '']]
    """
    return [['',  '', ''], ['', '', ''], ['', '', '']]

def demande_pseudo(pseudo:str, joueur:str) -> str:
    """ prends deux chaines de caractères pseudo et joueur en paramètre afin de demander le pseudo du joueur <joueur>
    , celui-ci doit être différent de celui passé en paramètre. De plus le pseudo écrit par le joueur ne doit pas être vide.

    Précondition : /
    Exemple(s) : /
    """
    while True:
        nom = input(f'Veuillez écrire le nom du joueur {joueur} : ').strip()
        while nom == pseudo or nom == '':
            print('\nErreur pseudo incorrect veuillez réessayer\n')
            nom = input(f'Veuillez écrire le nom du joueur {joueur} : ').strip()
        y_or_n = input(f'Joueur {joueur}, validez vous le nom {nom} Y/N : ')
        while y_or_n.lower() not in ['y', 'n']:
            print('\nErreur réponse incorrect veuillez réessayer\n')
            y_or_n = input(f'Joueur {joueur}, validez vous le nom {nom} Y/N : ')
        if y_or_n == 'Y' or y_or_n == 'y':
            print(f'\nBienvenue {nom}\n')
            return nom
        
def random_or_choice() -> bool:
    """ demande à l'utilistateur s'il veut choisir le joueur qui commence ou si il veut que ça soit aléatoire.
    Renvoie True si le joueur veut choisir et False si le joueur veut l'aléatoire

    Précondition : /
    Exemple(s) : /
    """
    choix = input('\nSouhaitez vous :\n\n\t- Choisir qu\'elle joueur commence (écrire "1")\n\t- Aléatoire (écrire "2")\n\nChoix : ')
    while choix not in ('1', '2'):
        print('Erreur, veuillez seulement répondre par "1" ou "2"')
        choix = input('\nSouhaitez vous :\n\n\t- Choisir qu\'elle joueur commence (écrire "1")\n\t- Aléatoire (écrire "2")\n\nChoix : ')
    return choix == '1'

def demande_qui_commence(noms:list[str]) -> bool:
    """ prend une liste de chaines de caractère en paramètres et demande au joueur
    s'il veut que le joueur A (noms[0]) ou le le joueur B (noms[1]) commence
    Précondition : len(nom) >= 2
    Exemple(s) : /
    """
    choix = input(f'\n\nQuelle joueur commences à jouer ?\n\n\t- Joueur A : {noms[0]} (écrire "A")\n\t- Joueur B : {noms[1]} (écrire "B")\n\nChoix : ')
    while choix.upper() not in ['A', 'B']:
        print('Erreur, veuillez seulement répondre par "A" ou "B"')
        choix = input(f'\n\nQuelle joueur commences à jouer ?\n\n\t- Joueur A : {noms[0]} (écrire "A")\n\t- Joueur B : {noms[1]} (écrire "B")\n\nChoix : ')
    return choix.upper() == 'A'
          
def qui_commence_random(liste:list[str]) -> list[str]:
    """ prend une liste de deux éléments et renvoie de façon aléatoire la liste inversée ou non
    Précondition : len(liste) >= 2
    Exemple(s) :
    $$$ qui_commence_random(['a', 'b'])
    ['a', 'b'] or ['b', 'a']
    """
    i = randint(0, 1)
    liste[i], liste[0] = liste[0], liste[i]
    return liste

def affiche_qui_commence_avant_chargement(noms:list[str]) -> None:
    """ prend une liste de chaine de caractère en paramètre et affiche le noms du joueur qui commenceras (le premier de la liste)
    et du deuxième également en précisant leur symbole respectif
    Précondition : len(noms) == 2
    Exemple(s) : /
    """
    print(f'\n{noms[0]} commencera donc la partie avec les X, quant à {noms[1]} vous aurez les O')

def qui_commence_general(noms:list[str]) -> list[str]:
    """ prend une liste de chiane de caractères noms en paramètre et renvoie
    en fonction du choix du joueur la liste inversée ou non
    Précondition : len(noms) == 2
    Exemple(s) : /
    """
    if random_or_choice(): # Le joueur à choisi de choisir qui commence
        if demande_qui_commence(noms): # Le joueur a choisi que le joueur A commence
            affiche_qui_commence_avant_chargement(noms)
            return noms
        else: # Le joueur a choisi que le joueur A commence
            noms = inverse_liste2(noms) # On inverse pour que le joueur B commence
            affiche_qui_commence_avant_chargement(noms)
            return noms
    else: # Le joueur à choisi l'aléatoire
        noms = qui_commence_random(noms) # détermine aléatoirement qui commence
        affiche_qui_commence_avant_chargement(noms)
        return noms
    
    
def inverse_liste2(liste:list) -> list:
    """ prend une liste de longueur 2 en paramètre et la renvoie inversée

    Précondition : len(liste) == 2
    Exemple(s) :
    $$$ inverse_liste2(['1', '2'])
    ['2', '1']
    """
    liste[0], liste[1] = liste[1], liste[0]
    return liste

def chargement_partie() -> None:
    """ affiche un chargement de 0 à 100 %
    Précondition : /
    Exemple(s) : /
    """
    print('\n\n\n\nChargement de la partie, veuillez patienter\n')
    p = 0
    while p < 100:
        sleep(random())
        print(f'{p}%')
        p += randint(2, 15)
    print('100%')
    print('\nLa partie commence!\n')
    
def affichage_grille(grille:list[list[str]]) -> None:
    """ affiche la grille passée en paramètre
    Précondition : len(grille) == len(grille[0]) == len(grille[1]) == len(grille[2]) == 3
    Exemple(s) : /
    """
    print(f"\n   {'1':^7} {'2':^7} {'3':^7}")
    for i in range(3):
        print(f"{i+1}  {grille[i][0]:^7}|{grille[i][1]:^7}|{grille[i][2]:^7}")
        if i < 2:
            print("   -------+-------+-------")
        else:
            print('\n')

def affichage_j_courant(ljoueur:list[str]) -> None:
    """ prend une liste de chiane de caractère ljoueur en paramètre et affiche le joueur courant
    Précondition : len(ljoueur) > 0
    Exemple(s) : /
    """
    n = randint(0, 2)
    if n == 0:
        print(f'A {ljoueur[0]} de jouer')
    elif n == 1:
        print(f'{ljoueur[0]}, c\'est votre tour')
    else:
        print(f'Au tour de {ljoueur[0]}')
        
def demande_indice_ligne() -> int:
    """ demande au joueur l'indice de la ligne où il veut mettre son symbole sur la grille
    Précondition : /
    Exemple(s) : /
    """
    ligne = input("Choisissez la ligne pour votre symbole : ")
    while ligne not in ['1', '2', '3']:
        print('Erreur, le numéro de ligne doit être compris entre 1 et 3')
        ligne = input("Choisissez la ligne pour votre symbole : ")
    return int(ligne) - 1
 
def demande_indice_colonne() -> int:
    """ demande au joueur l'indice de la ligne où il veut mettre son symbole sur la grille

    Précondition : /
    Exemple(s) : /
    """
    colonne = input("Choisissez la colonne pour votre symbole : ")
    while colonne not in ['1', '2', '3']:
        print('Erreur, le numéro de colonne doit être compris entre 1 et 3')
        colonne = input("Choisissez la colonne pour votre symbole : ")
    return int(colonne) - 1

def verif_grille_win(grille:list[list[str]]) -> bool:
    """ prend une grille de tictactoe et vérifie si il y a victoire (renvoie True),
    égalité (renvoie True) ou que la partie n'est pas fini (renvoie False)
    Précondition : len(grille) == len(grille[0]) == len(grille[1]) == len(grille[2]) == 3
    Exemple(s) :
    $$$ verif_grille_win([['', '', ''], ['', '', ''], ['', '', '']])
    False
    $$$ verif_grille_win([['X', 'X', 'X'], ['', 'O', ''], ['O', '', '']])
    True
    $$$ verif_grille_win([['O', 'X', 'X'], ['', 'O', ''], ['', '', 'O']])
    True
    $$$ verif_grille_win([['', 'X', 'X'], ['', 'O', ''], ['', '', 'O']])
    False
    $$$ verif_grille_win([['O', 'X', 'X'], ['O', 'O', ''], ['O', '', '']])
    True
    $$$ verif_grille_win([['O', 'X', 'X'], ['O', 'O', 'X'], ['', 'O', 'X']])
    True
    $$$ verif_grille_win([['O', 'X', 'X'], ['X', 'O', 'O'], ['O', 'O', 'X']])
    True
    """
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != '':
            return True
        elif grille[0][i] == grille[1][i] == grille[2][i] != '':
            return True
    if grille[0][0] == grille[1][1] == grille[2][2] != '':
        return True
    elif grille[0][2] == grille[1][1] == grille[2][0] != '':
        return True
    for liste in grille:
        if '' in liste:
            return False
    return True

def is_case_empty(grille:list[list[str]], i_ligne:int, i_colonne:int) -> bool:
    """ prend en paramètre une liste de liste de chaine de caractère grille et deuxi entier i_ligne et i_colonne
    et renvoie True si la case d'indice i_ligne et i_colonne est une chaine vide
    Précondition : 0 <= i_ligne < 3
                   0 <= i_colonne < 3
                   len(grille) == len(grille[0]) == len(grille[1]) == len(grille[2]) == 3
    Exemple(s) :
    $$$ is_case_empty([['', '', ''], ['', '', ''], ['', '', '']], 2, 2)
    True
    $$$ is_case_empty([['', '', ''], ['', '', ''], ['', '', 'X']], 2, 2)
    False
    $$$ is_case_empty([['', '', ''], ['', '', ''], ['', '', 'X']], 0, 1)
    True
    $$$ is_case_empty([['', 'O', ''], ['', '', ''], ['', '', 'X']], 0, 1)
    False
    """
    return grille[i_ligne][i_colonne] == ''
    
def boucle_indice_grille(grille:list[list[str]]) -> list[int]:
    """ prend en paramètre une liste de liste de chaine de caractère grille et renvoie les indices saisie par l'utilisateur
    si ces derniers correspondent à une case vide et comprise dans la grille
    Précondition : len(grille) == len(grille[0]) == len(grille[1]) == len(grille[2]) == 3
    Exemple(s) : /
    """
    i_ligne = demande_indice_ligne()
    i_colonne = demande_indice_colonne()
    while not is_case_empty(grille, i_ligne, i_colonne):
        print('\nErreur, vous ne pouvez pas changer un signe déjà présent. Veuillez réessayer\n')
        i_ligne = demande_indice_ligne()
        i_colonne = demande_indice_colonne()
    return [i_ligne, i_colonne]
    
def qui_a_gagne(grille:list[list[str]]) -> int:
    """ prend une grille de tictactoe et vérifie si il y a victoire du joueur avec les X (renvoie 1), du joueur avec les O (renvoie 0)
    ou égalité (renvoie -1)
    Précondition : len(grille) == len(grille[0]) == len(grille[1]) == len(grille[2]) == 3
    Exemple(s) :
    $$$ qui_a_gagne([['O', 'X', 'X'], ['O', 'X', ''], ['O', '', 'X']])
    0
    $$$ qui_a_gagne([['X', 'X', 'X'], ['', 'O', ''], ['O', '', '']])
    1
    $$$ qui_a_gagne([['O', 'X', 'X'], ['', 'O', ''], ['', '', 'O']])
    0
    $$$ qui_a_gagne([['X', 'X', 'X'], ['', 'O', ''], ['', '', 'O']])
    1
    $$$ qui_a_gagne([['O', 'X', 'X'], ['O', 'O', ''], ['O', '', '']])
    0
    $$$ qui_a_gagne([['O', 'X', 'X'], ['O', 'O', 'X'], ['', 'O', 'X']])
    1
    $$$ qui_a_gagne([['O', 'X', 'X'], ['X', 'O', 'O'], ['O', 'O', 'X']])
    -1
    """
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != '':
            if grille[i][0] == 'X':
                return 1
            return 0
        elif grille[0][i] == grille[1][i] == grille[2][i] != '':
            if grille[0][i] == 'X':
                return 1
            return 0
    if grille[1][1] == grille[2][2] == grille[0][0] != '':
        if grille[0][0] == 'X':
            return 1
        return 0
    elif grille[0][2] == grille[1][1] == grille[2][0] != '':
        if grille[2][0] == 'X':
            return 1
        return 0
    return -1
             
def affichage_resultat_jeu(resultat:int, nom:str) -> None:
    """ prend un resultat (entre -1 et 1 inclus) et une chaine de caractère nom et affiche le resultat avec le nom du gagnant (ou égalité)
    Précondition : resultat in [-1, 0, 1]
    Exemple(s) : /
    """
    if resultat == 1:
        print(f'{nom} a gagné, trois signes X sont alignées!')
    elif resultat == 0:
        print(f'{nom} a gagné, trois signes 0 sont alignées!')
    else:
        print("Egalité, il n'y a plus aucun coup possible")
    
def jouer() -> None:
    """Fonction principale pour jouer au morpion.
    """
    nom_jA = demande_pseudo('', 'A') # demande nom joueur A
    noms = [nom_jA, demande_pseudo(nom_jA, 'B')] # demande nom joueur B et affecte les deux pseudo dans liste noms
    noms = qui_commence_general(noms) # Le joueur à choisi de choisir qui commence ou de laisser l'aléatoire faire
    grille = initiation_grille() # Création de la grille vide
    symboles = ['X', 'O'] # Création des symboles
    chargement_partie() # Faux chargement pour le style

    ### boucle de jeu
    while not verif_grille_win(grille) :
        
        affichage_grille(grille)
        affichage_j_courant(noms)
        indices = boucle_indice_grille(grille) # demande les indices au joueur et vérifie si la case est valide (case vide et dans la grille)
        grille[indices[0]][indices[1]] = symboles[0] # Le case que le joueur a choisi devient le symbole du joueur
        noms, symboles = inverse_liste2(noms), inverse_liste2(symboles) # Changement joueur courant
    affichage_grille(grille)
    resultat = qui_a_gagne(grille)
    affichage_resultat_jeu(resultat, noms[1])
    
if __name__ == '__main__':
    jouer()

