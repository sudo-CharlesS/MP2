
function cryptage(cle, text) {

    let textCrypte = ' ';
    for (let i = 0; i<(text.length); i++) {
        alert("e");
        if ((('A').charCodeAt) <= (text[i].charCodeAt) && (text[i].charCodeAt) <= (('Z').charCodeAt)) {
            textCrypte += (((text[i].charCodeAt) + cle).charAt());
            alert((((text[i].charCodeAt) + cle).charAt()));
        }              
        else if ('A' <= text[i] <= 'Z') {
            textCrypte += chr(ord(tex[i]) + cle - 26);
        }
        else {
            textCrypte += text[i];
        }
    }
    return( textCrypte);
}

/*
def decryptage(cle: int, text: str) -> str:
"""
Décrypte une chaine de caractère selon la clé
\n Pré: clé de cryptage -> cle: int, texte à décrypter -> text: str
\n Post: texte décrypté -> textCrypte: str
"""
assert type(cle) == int and type(text) == str, "La clé doit être un nombre entier et le texte une chaine de caractères"     #affiche si cle n'est pas un nombre entier et si text n'est pas une chaine de caractères
textDecrypte = ''                                         #définit une chaine de caractère vide appelée textCrypte
if cle >= 26:                                            #condition si cle est supérieur ou égal à 26
cle -= 26 * (cle//26)                                   #soustrait 26 fois le quotient de cle par 26
    elif - 25 <= cle <= -1:                                      #sinon si cle est supérieur ou égal à - 25 et est inférieur ou égal à - 1
cle += 26                                             #ajoute 26 à cle
elif cle <= -26:                                          #sinon si cle est inférieur ou égal à - 26
cle += 26 * (-cle//26)+26                               #ajoute 26 + 26 fois le quotient de cle par 26
    for i in text:                                          #répète les instructions ci - dessous en parcourant la chaine
if 'A' <= i <= 'Z' and chr(ord(i) - cle) >= 'A':        #condition si i est compris dans l'alphabet majuscule et que i-cle dépasse la lettre A
textDecrypte += chr(ord(i) - cle)                   #ajoute à textCrypte le caractère crypté avec la clef
elif 'A' <= i <= 'Z':                                 #sinon si i est compris dans l'alphabet majuscule
textDecrypte += chr(ord(i) - cle + 26)                #ajoute à textCrypte le caractère crypté avec la cle + 26(pour revenir au début de l'alphabet)
        else:                                               #sinon
            textDecrypte += i                                 #ajoute à textDecrypte le même caractère que dans le texte d'origine
    return textDecrypte                                     #retourne la variable textDecrypte

def decryptageSansCle(text: str) -> str:                       #définit fonction decryptageSansCle avec text comme paramètre
"""
Décrypte une chaine sans clé
\n Pré: texte à décrypter -> text: str
\n Post: texte décrypté -> textDecrypte: str ou message erreur décryptage -> str
"""

assert type(text) == str, "Le texte doit être une chaine de caractères"    #affiche si text n'est pas une chaine de caractères
i = 0                                                     #définit variable i = 0
while i <= 26:                                          #répète les instructions ci - dessous tant que i est inférieur ou égal à 26
print("\n Tentative de décryptage avec clé de {} : {}".format(i, decryptage(i, text)))     #affiche le message précèdant avec la variable i et le résultat de la fonction decryptage avec les paramètres i et text
textClair = input("Si vous visualisez le texte en clair tapez F (majuscule ou minuscule), sinon tapez entrée : ")         #assigne à la variable textClair le choix de l'utilisateur
if textClair == 'f' or textClair == 'F':                #si textClair = lettre f ou si textClair = lettre F
return decryptage(i, text)                      #retourne le résultat de la fonction decryptage avec les paramètres i et text
        else:                                               #sinon
i += 1                                            #ajoute 1 à i
return "Désolé, vous avez essayé toutes les valeurs de clé, le texte a été crypté selon une méthode non mono-alphabétique"     #retourne le texte précédant
*/



let menu = 0;
while (menu != 4) {

    menu = parseInt(prompt("MENU : \n 1-Cryptage d'un texte à partir d'une clé fournie \n 2-Décryptage d'un texte à partir d'une clé fournie \n 3-Décryptage d'un texte sans la clé \n 4-Fin du programme \n \n Quel est votre choix ? "),10);




    if (menu == 1) {

        alert("\n texte crypté : ", cryptage(parseInt(prompt("Quel est votre clé ? "),10), prompt("texte à crypter : ")));
    }

    else if (menu == 2) {

        alert("\n texte décrypté : ", decryptage(parseInt(prompt("Quel est votre clé ? "),10), prompt("texte à décrypter : ")));
    }

    else if (menu == 3) {
        alert("\n texte décrypté : ", decryptageSansCle(prompt("texte à décrypter : ")));
    }
}
alert("\n Fin du programme");

