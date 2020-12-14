# -*- coding: utf-8 -*-

"""
Logiciel de cryptage et décryptage
Permet de crypter et décrypter un texte par substitution mono-alphabétique
    
@author: Hugueny Louis & Charles Stchepinsky
"""

from browser import document, html, alert

def cryptage(cle:int, text:str)->str:                       #définit fonction cryptage avec cle et text comme paramètres
    """
    Crypte une chaine de caractère selon la clé
    \n Pré : clé de cryptage -> cle:int, texte à crypter -> text:str
    \n Post : texte crypté -> textCrypte:str
    """
    assert type(cle)==int and type(text)==str, "La clé doit être un nombre entier et le texte une chaine de caractères"     #affiche si cle n'est pas un nombre entier et si text n'est pas une chaine de caractères
    textCrypte=''                                           #définit une chaine de caractère vide appelée textCrypte
    if cle >=26:                                            #condition si cle est supérieur ou égal à 26
        cle-=26*(cle//26)                                   #soustrait 26 fois le quotient de cle par 26
    elif -25<=cle<=-1:                                      #sinon si cle est supérieur ou égal à -25 et est inférieur ou égal à -1
        cle+=26                                             #ajoute 26 à cle
    elif cle<=-26:                                          #sinon si cle est inférieur ou égal à -26
        cle+=26*(-cle//26)+26                               #ajoute 26 + 26 fois le quotient de cle par 26
    for i in text:                                          #répète les instructions ci-dessous en parcourant la chaine
        if 'A'<= i <='Z' and chr(ord(i)+cle) <= 'Z':        #condition si i est compris dans l'alphabet majuscule et que i+cle ne dépasse pas la lettre Z
            textCrypte+=chr(ord(i)+cle)                     #ajoute à textCrypte le caractère crypté avec la clef
        elif 'A'<= i <='Z':                                 #sinon si i est compris dans l'alphabet majuscule
            textCrypte+=chr(ord(i)+cle-26)                  #ajoute à textCrypte le caractère crypté avec la cle-26 (pour revenir au début de l'alphabet)
        else:                                               #sinon
            textCrypte+=i                                   #ajoute à textCrypte le même caractère que dans le texte à crypter
    return textCrypte                                       #retourne la variable textCrypte

def decryptage(cle:int, text:str)->str:                     #définit fonction decryptage avec comme paramètres cle et text 
    """
    Décrypte une chaine de caractère selon la clé
    \n Pré : clé de cryptage -> cle:int, texte à décrypter -> text:str
    \n Post : texte décrypté -> textCrypte:str
    """
    assert type(cle)==int and type(text)==str, "La clé doit être un nombre entier et le texte une chaine de caractères"     #affiche si cle n'est pas un nombre entier et si text n'est pas une chaine de caractères
    textDecrypte=''                                         #définit une chaine de caractère vide appelée textCrypte
    if cle >=26:                                            #condition si cle est supérieur ou égal à 26
        cle-=26*(cle//26)                                   #soustrait 26 fois le quotient de cle par 26
    elif -25<=cle<=-1:                                      #sinon si cle est supérieur ou égal à -25 et est inférieur ou égal à -1
        cle+=26                                             #ajoute 26 à cle
    elif cle<=-26:                                          #sinon si cle est inférieur ou égal à -26
        cle+=26*(-cle//26)+26                               #ajoute 26 + 26 fois le quotient de cle par 26
    for i in text:                                          #répète les instructions ci-dessous en parcourant la chaine
        if 'A'<= i <='Z' and chr(ord(i)-cle) >= 'A':        #condition si i est compris dans l'alphabet majuscule et que i-cle dépasse la lettre A
            textDecrypte+=chr(ord(i)-cle)                   #ajoute à textCrypte le caractère crypté avec la clef
        elif 'A'<= i <='Z':                                 #sinon si i est compris dans l'alphabet majuscule
            textDecrypte+=chr(ord(i)-cle+26)                #ajoute à textCrypte le caractère crypté avec la cle+26 (pour revenir au début de l'alphabet)
        else:                                               #sinon
            textDecrypte+=i                                 #ajoute à textDecrypte le même caractère que dans le texte d'origine
    return textDecrypte                                     #retourne la variable textDecrypte

def decryptageSansCle(text:str)->str:                       #définit fonction decryptageSansCle avec text comme paramètre
    """
    Décrypte une chaine sans clé    
    \n Pré : texte à décrypter -> text:str
    \n Post : texte décrypté -> textDecrypte:str ou message erreur décryptage -> str 
    """

    assert type(text)==str, "Le texte doit être une chaine de caractères"    #affiche si text n'est pas une chaine de caractères
    i=0                                                     #définit variable i = 0
    while i <= 26:                                          #répète les instructions ci-dessous tant que i est inférieur ou égal à 26
        print("\n Tentative de décryptage avec clé de {} : {}".format(i, decryptage(i, text)))     #affiche le message précèdant avec la variable i et le résultat de la fonction decryptage avec les paramètres i et text
        textClair=input("Si vous visualisez le texte en clair tapez F (majuscule ou minuscule), sinon tapez entrée : ")         #assigne à la variable textClair le choix de l'utilisateur
        if textClair=='f' or textClair=='F':                #si textClair = lettre f ou si textClair = lettre F
            return decryptage(i, text)                      #retourne le résultat de la fonction decryptage avec les paramètres i et text
        else:                                               #sinon
            i+=1                                            #ajoute 1 à i
    return "Désolé, vous avez essayé toutes les valeurs de clé, le texte a été crypté selon une méthode non mono-alphabétique"     #retourne le texte précédant



#code principal du programme
def main(n):
    menu=0                                                                              #définit variable menu = 0
    while menu!=4:                                                                      #répète les instructions ci-dessous tant que menu n'est pas égal à 4
        try:                                                                            #éxécute les instructions suivantes
            menu=int(input("MENU : \n 1-Cryptage d'un texte à partir d'une clé fournie \n 2-Décryptage d'un texte à partir d'une clé fournie \n 3-Décryptage d'un texte sans la clé \n 4-Fin du programme \n \n Quel est votre choix ? "))       #demande à l'utilisateur son choix de programme
            assert menu==1 or menu==2 or menu==3 or menu==4, "Utilisez uniquement les chiffres 1,2,3 et 4 pour faire votre choix"       #affiche ce message si l'utilisateur ne met pas le bon chiffre
        except (ValueError, AssertionError):                                            #si une erreur de type ValueError ou AssertionError servient dans le try
            alert("Utilisez uniquement les chiffres 1,2,3 et 4 pour faire votre choix") #affiche le message précèdant

        if menu==1:                                                                     #si l'utilisateur choisit le menu n°1
            try:                                                                        #éxécute les instructions suivantes
                alert("\n texte crypté : ",cryptage(int(input("Quel est votre clé ? ")), input("texte à crypter : ")))       #demande à l'utilisateur sa cle et son texte à crypter et affiche le texte crypté
            except ValueError :                                                         #si une erreur de type ValueError servient dans le try
                alert("La clé doit être un nombre entier")                          #affiche le message précèdant
        elif menu==2:                                                                   #si l'utilisateur choisit le menu n°2
            try:                                                                        #éxécute les instructions suivantes
                alert("\n texte décrypté : ",decryptage(int(input("Quel est votre clé ? ")), input("texte à décrypter : ")))       #demande à l'utilisateur sa cle et son texte à décrypter et affiche le texte décypté
            except ValueError:                                                          #si une erreur de type ValueError servient dans le try
                alert("La clé doit être un nombre entier")                              #affiche le message précèdant
        elif menu==3:                                                                   #si l'utilisateur choisit le menu n°3
            alert("\n texte décrypté : ",decryptageSansCle(input("texte à décrypter : ")))  #demande à l'utilisateur son texte à décrypter et affiche le texte décrypté

    alert("\n Fin du programme")                                                        #affiche fin du programme

document["echo"].bind("click", main)