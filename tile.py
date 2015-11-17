#Rodrigo Rogel-Perez
#COM 110
#Domino Game
#December 17, 2013

class Tile:

    def __init__(self,side2,side1):
        self.side2 = side2
        self.side1 = side1

    def getSide2(self):
        return self.side2

    def getSide1(self):
        return self.side1
    
    def __str__(self):
        
        Nums = {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six"}
        return Nums[self.side2] + "," + Nums[self.side1]

    def Domvalue(self):
        totalPips = self.side2 + self.side1
        print(totalPips)

        return totalPips

if __name__=="__main__": 
    main()
