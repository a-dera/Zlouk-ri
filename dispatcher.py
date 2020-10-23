"""
Dispatcher function for the separation of the words.

Receive keywords (one line string in witch words 
are separated using simple comma) from the database 
as parameters and return each keyword separately
"""
#use cerberus for form validation
__title__ = 'dispatcher'
__version__ = '0.0.1a'
__author__ = 'Amédée DERA'
__license__ = 'MIT'
import os

class Dispatcher(object):
    def __init__(self, data=0):
        self.data = data
    def setdata(self, data):
            self.data = data

Test = Dispatcher()
Test2 = Dispatcher()
# Test.setdata (['working', 'eating', 'sliping', 'enjoying', 'life'])
Test.setdata (['working, eating, sliping, enjoying, life'])
Test2.setdata ('working, eating, sliping, enjoying, life')
""" 
A faire

compter le nombre d'items et ne garder que les 3 premiers, puis rajouter endoffile de
sorte à avoir un point de fin de lecture bien connue.

compter les redondances et supprimer les copies


"""
def parserLine(line):
    i = 0
    x = line.data
    a,b = len(x), len(x)
    if b == 3:
        return True
    a:a = 'endoffile' #make sure the last item is known (for better parsing)

    k = x.split(",")

    print(k)
parserLine(Test2)

def parserList(list):
    i = 0
    x = list.data
    a,b = len(x), len(x)
    if b == 3:
        return True
    a:a = 'endoffile' #make sure the last item is known (for better parsing)
    #x *= 
    for t in x:
        print(x[i])
        #.cpaitalize(), upper(), lower()
        i += 1
    print(b)
parserList(Test)

"""def tokenize(chaine):
	ponc = [' ','.',',','!','?',';',':']
	mot=""
	for char in chaine:
		if char in ponc:
			print(mot)
			print(char)
			mot=""
		else:
			mot = mot + char			
print (tokenize("il marche, elle marche."))
"""


