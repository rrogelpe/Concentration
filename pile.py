#Rodrigo Rogel-Perez
#COM 110
#Domino Game
#December 17, 2013

from random import*
from tile import*


class Dominopile:

    def __init__(self):
        self.dominopile = []
        for side2 in range(0,7):
            for side1 in range(side2,7):
                self.dominopile.append(Tile(side2,side1))
                self.dominopile.append(Tile(side2,side1))


    def Mixpile(self):
        for x in range(len(self.dominopile)):
            d = self.dominopile[x]
            i = randrange(56)
            domino = self.dominopile[i]
            self.dominopile[i] = d
            self.dominopile[x] = domino
            print(x+1)
            
        return self.dominopile

    def DealDomino(self):
        i = randrange(len(self.dominopile))
        dealtDomino = self.dominopile.pop(i)
        print(dealtDomino)
              
        return dealtDomino
        

    def DominosLeft(self):
        pileLength = len(self.dominopile)
        print(pileLength)
        
        return pileLength
        
if __name__=="__main__": 
    main() 
