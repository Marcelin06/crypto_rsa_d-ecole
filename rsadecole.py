#Nom : Marcelin
#Prénom : Dieunel
#No : 12207041
#Devoir de cryptologie
#L3 informatique
#Institut galille
#Universite Sorbonne Paris Nord
#Professeur : Ali AKHAVI
#Date de création 26/12/2023
#Mise a jour : 02/01/2024
#Titre : RSA D'ECOLE



import math
from sympy import isprime, mod_inverse, totient
import random
import sys
import os 
from Crypto.PublicKey import RSA #module pour generer une paire ce cle




def end_process():
    print("\n AU REVOIR !!!\n ")
    sys.exit()


def vider_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def bienvenue():
    vider_terminal()    
    print("\n \t\t\t\t***** BIENVENUE DANS LE RSA D'ECOLE *****")


#generer une paire de cle et la retourne
def generer_paire_cle(bits):
    key = RSA.generate(bits)
    return key




#algo de chiffrement
#{pk} clé publique
#{m} texte clair
#renvoie le chiffré
def chiffrage(pk, m):
    n = int(pk[0])
    e = int(pk[1])
    result = int(pow(m, e, n))
    return result



#algo de déchiffrement
#{sk} clé privée
#{c} chiffré
#renvoie le texte clair associé
def dechiffrage(sk, c):
    n = int(sk[0])
    d = int(sk[1])
    result = int(pow(c, d, n))
    return result



#déroulement du programme
while True :
    bienvenue()
    choix = int(input("\n Saisir 1 pour générer une paire de clé. Saisir 0 pour terminer : "))
    if choix == 1 :
        bienvenue()
        cle = generer_paire_cle(2048)
        pk = (cle.n, cle.e)
        sk = (cle.n, cle.d)
        bienvenue()
        print(f"La clé publique est {pk}\n")
        while True :
            choix_1 = int(input("\n\nFaites votre choix :\n\t 1-Chiffrer \n\t 2-Déchiffrer \n\t 3-Accueil \n\t 4-Quitter \n Choix : "))
            if choix_1 == 1:                
                m = int(input(f"\nLe message clair que vous voulez chiffrer :  "))
                c = chiffrage(pk, m)
                print(f"\nLe chiffré de {m} avec la clé est {c}")
                continue
                    
            elif choix_1 == 2:
                c = int(input("\nLe message a déchiffrer : "))
                m1 = dechiffrage(sk, c)
                print(f"\nLe déchiffrage de {c} est {m1}")
                continue
               
            elif choix_1 == 3:
                break
            else:
                end_process()
    else:
        end_process()
