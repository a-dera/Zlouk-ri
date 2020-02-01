import os
import string
import random
import os.path
#import names #biblio à part
#import pickle #pour les sauvegarde chiffre dans les fichiers

clé1=[input("Entrer le 1er mot clé: ")]
clé2=[input("Entrer le 2e mot clé: ")]
#la variable qui va contenir tous les éléments affichés
rendu = []
        
def getLetters(length):
	"""Générer une chaîne aléatoire de x lettres"""
	str = string.ascii_lowercase
	return ''.join(random.choice(str)
		       for i in range(length))

def test1(clé1):
    "Tester la première clé"
    for letter in clé2:
        c= letter

    a = clé1[0]
    b=getLetters(1)
    d=a+c
    e=b+c
    f=a+b+c
    print("Voici les noms gérénerés au test1")
    print(d)
    print(e)
    print(f)
    rendu.append(d)
    rendu.append(e)
    rendu.append(f)

test1(clé1)

def test2(clé2):
    "Tester la deuxième clé"
    for letter in clé1:
        c= letter

    a = clé2[0]
    b=getLetters(1)
    d=a+c
    e=b+c
    f=a+b+c
    print("Voici les noms gérénerés au test2")
    print(d)
    print(e)
    print(f)
    print("Avec la génération de lettre ")
    x= getLetters(1)
    y= getLetters(2)
    v=a+x
    w=a+y
    g=e+x
    j=x+e
    print(w)
    print(v)
    print(g)
    print(j)
    rendu.append(d)
    rendu.append(e)
    rendu.append(f)
    rendu.append(w)
    rendu.append(v)
    rendu.append(g)
    rendu.append(j)


test2(clé2)

"""def testx():
    "Tester avec les nouvelles manières"
 

    print("Voici les noms gérénerés avec les nouvelles manières")
    xor= names.get_full_name()
    yor= names.get_full_name()
    print(xor)
    print(yor)
    rendu.append(xor)
    rendu.append(yor)
testx()"""


def test4():
    "test avec les fichiers txt"
    path = '../NameGenerator/brain/santé.txt'

    #print('Le fichier', os.path.abspath(path), end=' ')
    if os.path.exists(path):
    #if os.path.abspath(path):
        print('Enregistrement en cours...')
    else:
        print("le fichier n'existe pas")

    paq = open(path,'a')
    paq.write("les key: \n ")
    paq.write(str(clé1))
    paq.write(str(clé2))
    paq.write("\n Les rendus:  ")
    paq.write(str(rendu))
    paq.write(".....\n")
    paq.close()
    print("les données ont été enregistrées!")
test4()
os.system("pause")