from pile import*
from button import*
from dombutton import*
from tile import*
from graphics import*
from random import*
from time import*
import math


class DominoGame:
    """A grid of squares/buttons"""
    #Domino grid class repressenting actual game setup
    def __init__(self, win, startX, startY, numCols, numRows, squareWidth, space1, squareHeight, space2):
        """initializes a 2D list of blank button objects"""
        self.space1 = space1
        self.space2 = space2
        self.dominopile = Dominopile()
        self.dominopile.Mixpile()
        self.buttonList = []
        self.dominoList = []
        self.scoreList = []
        self.numCols = numCols
        self.numRows = numRows
        self.startX = startX
        self.startY = startY
        self.compareList = []
        self.holdList = []
        self.scores = []
        for x in range(startX, numCols, space1):
            for y in range(startY, numRows, space2):
                self.imaDraw = self.dominopile.DealDomino()
                self.tileFront = Image(Point(x,y),"images/" + str(self.imaDraw.side2) + str(self.imaDraw.side1) + ".gif")
                self.tileBack = Image(Point(x,y),"images/tilecover.gif")
                self.domino = dominoButton(win,Point(x,y),squareWidth,squareHeight,"",self.tileFront,self.tileBack)
                self.domino.activate()
                self.domino.setFront(win)
                self.domino.setBack(win)
                self.buttonList.append(self.domino)
                self.dominoList.append(self.imaDraw)#this list will carry the images whom which we can attain the values
                
    def getList(self):
        return self.buttonList
    
##########################################################################################################################################   
    def startGame(self,win):
        while len(self.compareList) != 2:
            pt = win.getMouse()
            for x in range(len(self.buttonList)):#Click random tile
                if self.buttonList[x].clicked(pt):
                    self.holdList.append(self.buttonList[x])
                    self.buttonList[x].deactivate()
                    self.buttonList[x].reveal()
                    self.buttonList[x].undoButton()
                    t = self.dominoList[x].Domvalue()
                    self.compareList.append(t)
        t1 = self.compareList[0]
        t2 = self.compareList[1]

        if t1 + t2 == 12: #If sums of pips add up you get two points      
            self.scoreList.append(t1)
            self.scoreList.append(t2)
            
            noteG = Text(Point(1100,400),"Nice, You Found a Pair!")
            noteG.setFill("green3")
            noteG.setSize(20)
            noteG.setStyle("bold italic")
            noteG.draw(win)
            sleep(.5)
            noteG.undraw()
            del self.holdList[:]
            del self.compareList[:]

        else:#If tiles don't add up to 12 then cover it up again
            noteB = Text(Point(1100,400),"Sorry try another pair!")
            noteB.setFill("red3")
            noteB.setSize(20)
            noteB.setStyle("bold italic")
            noteB.draw(win)
            sleep(.5)
            noteB.undraw()
            for y in range(len(self.holdList)):
                self.holdList[y].setBack(win)
                self.holdList[y].activate()
            del self.holdList[:]
            del self.compareList[:]
##########################################################################################################################                                                          
    def evaluateScore(self):#adds number of tiles won
        
        Score = 0
        for x in self.scoreList:
            Score = Score + 1
        Score = round(Score/2)
        return Score
##########################################################################################              
    def getscoreList(self):
        return self.scoreList
###########################################################################################################################
    def clearBoard(self):
        for x in range(len(self.buttonList)):
            self.buttonList[x].undoButton()
            self.buttonList[x].deactivate()
################################################################################################        
    def Countdown(self,win):
        for t in range(60,-1,-1):
            seconds = t % 60
            print (seconds)
            timer = Text(Point(1100,400),"Seconds left: " + str(seconds))
            timer.setTextColor("white")
            timer.setSize(10)
            timer.draw(win)
            sleep(1.0)
            timer.undraw()
##################################################################################################  
    def clearScore(self):
        del self.scoreList[:]
#############################################       
    def getScore(self,nameScorePair):
        self.scores.append(nameScorePair)
        for i in range(len(self.scores)):
            print(self.scores[i])
        return nameScorePair[1]
#############################################
def main():
    #creates graphical window which the class and its objects will be projected onto
    win=GraphWin("Domino", 1350,730)
    scores = []

    #Background
    backImg = Image(Point(675,365),"images/woodBoard.gif")
    backImg.draw(win)

    header = Text(Point(1075,50),"Concentration")
    header.setSize(35)
    header.setStyle("italic")
    r = randrange(0,255)
    g = randrange(0,255)
    b = randrange(0,255)
    header.setTextColor(color_rgb(r,g,b))
    header.draw(win)

    posName = Text(Point(325,425),"Enter Player 1 Name")
    posName.setStyle("bold italic")
    posName.setFace("helvetica")
    posName.setTextColor("white")
    posName.setSize(15)
    posName.draw(win)
    
    nameTag = Entry(Point(325,450),50)
    nameTag.setFill("grey")
    nameTag.draw(win)
    
    playButton = Button(win,Point(627,650),95.5,96.5,"Play")
    playButton.activate()

    insButton = Button(win,Point(723,650),95.5,96.5,"Instructions")
    insButton.activate()
    

    quitButton = Button(win,Point(1100,650),193.5,96.5,"Quit")
    quitButton.activate()
        

    bImage = Image(Point(675,650),"images/tilePlay.gif")
    bImage.draw(win)

    qImage = Image(Point(1100,650),"images/return.gif")
    qImage.draw(win)

    playText = Text(Point(627,650),"Play")
    playText.setTextColor("white")
    playText.setSize(15)
    playText.draw(win)

    instText = Text(Point(723,650),"Rules")
    instText.setTextColor("black")
    instText.setSize(15)
    instText.draw(win)

    quitText = Text(Point(1100,650),"Quit")
    quitText.setTextColor("black")
    quitText.setSize(15)
    quitText.draw(win)
    
    pt = win.getMouse()
##############################################################################        
    while not playButton.clicked(pt) or nameTag.getText() == "":
        if insButton.clicked(pt): 
            insImg = Image(Point(675,365),"images/chalk.gif")
            insImg.draw(win)
            
            returnB = Button(win,Point(1100,650),193.5,97.5,"Back")
            returnB.deactivate()

            returnI = Image(Point(1100,650),"images/return.gif")
            returnI.draw(win)

            returnText = Text(Point(1100,650),"Return")
            returnText.setSize(15)
            returnText.draw(win)
            
            insmessage = Text(Point(600,205),"The goal is to collect all pairs of tiles.\n With double-six dominoes, pairs consist of any two tiles whose pips sum to 12.\n"
                              "For example, the 3–5 and the 0–4 form a pair.\n Find all pairs to win the game.\n"
                              "Player starts with 30 tries, and loses a try if attempt fails, but gains one if attempt is successful.")
            insmessage.setSize(15)
            insmessage.setStyle("bold italic")
            insmessage.draw(win)
            nameTag.undraw()
            while not returnB.clicked(pt):
                returnB.activate()
                pt = win.getMouse()
            returnText.undraw()
            returnB.undoButton()
            returnB.deactivate()
            insImg.undraw()
            insmessage.undraw()
            returnI.undraw()
            nameTag.draw(win)
            
        elif quitButton.clicked(pt):
            win.close()
            
        elif nameTag.getText() != "":
            note = Text(Point(325,500),"Please click play to start")
            note.setFace("helvetica")
            note.setStyle("bold italic")
            note.setTextColor("white")
            note.setSize(15)
            note.draw(win)
            sleep(1.25)
            note.undraw()
            
        else:    
            warning = Text(Point(325,500),"Please enter your name and then click Play")
            warning.setFace("helvetica")
            warning.setStyle("bold italic")
            warning.setTextColor("white")
            warning.setSize(15)
            warning.draw(win)
            sleep(1.25)
            warning.undraw()   
        pt = win.getMouse()
###############################################################################
    instText.undraw()
    playText.undraw()
    plaName = nameTag.getText()
    insButton.undoButton()
    insButton.deactivate()
    playButton.undoButton()
    playButton.deactivate()
    nameTag.undraw()
    posName.undraw()
    bImage.undraw()
    quitText.setTextColor("gray")
############################################################################### 
    Game = DominoGame(win,102,85,902,695,40,100,80,95)
    plaPool = Game.getscoreList()
    moves = 30

    while moves > 0:
        plaPool = Game.evaluateScore()
        test = Game.evaluateScore()
        plaTotal = Text(Point(1050,150),str(plaName) + "'s Score: " + str(plaPool))
        plaTotal.setStyle("bold italic")
        plaTotal.setFace("helvetica")
        plaTotal.setTextColor("white")
        plaTotal.setSize(20)
        plaTotal.draw(win)
        movesLeft = Text(Point(1050,200),"Moves Left: " + str(moves))
        movesLeft.setStyle("bold italic")
        movesLeft.setFace("helvetica")
        movesLeft.setTextColor("white")
        movesLeft.setSize(20)
        movesLeft.draw(win)
        Game.startGame(win)
        plaPool = Game.evaluateScore()
        if plaPool > test:
            moves = moves + 1
        plaTotal.undraw()
        movesLeft.undraw()
        moves = moves - 1

    againButton = Button(win,Point(1052,548),95.5,96.5,"Retry")
    againButton.activate()

    menuButton = Button(win,Point(1148,548),95.5,96.5,"Menu")
    menuButton.activate()

    quitText.setTextColor("black")


    choiceImage = Image(Point(1100,548),"images/tilePlay.gif")
    choiceImage.draw(win)

    playText = Text(Point(1052,548),"Retry")
    playText.setTextColor("white")
    playText.setSize(15)
    playText.draw(win)

    menuText = Text(Point(1148,548),"Menu")
    menuText.setTextColor("black")
    menuText.setSize(15)
    menuText.draw(win)

    winTag = Text(Point(1100,125),str(plaName) + "'s Final Score: " + str(plaPool))
    winTag.setFace("helvetica")
    winTag.setStyle("bold italic")
    winTag.setTextColor("white")
    winTag.setSize(20)
    winTag.draw(win)
    ##########################
    scoreList = Game.getScore((plaName,plaPool))
    
    overTag = Text(Point(1100,200),"You're out of tries!")
    overTag.setFace("helvetica")
    overTag.setStyle("bold italic")
    overTag.setTextColor("white")
    overTag.setSize(20)
    overTag.draw(win)

    
    pt = win.getMouse()
    
    Game.clearScore()

    while not quitButton.clicked(pt):
        if againButton.clicked(pt):
            moves = moves + 30
            Game.clearBoard()
            overTag.undraw()
            menuText.undraw()
            playText.undraw()
            winTag.undraw()
            choiceImage.undraw()
            againButton.undoButton()
            menuButton.undoButton()
            quitText.setTextColor("gray")
            Game = DominoGame(win,102,85,902,695,40,100,80,95)
            plaPool = Game.getscoreList()
            while moves > 0:
                plaPool = Game.evaluateScore()
                test = Game.evaluateScore()
                plaTotal = Text(Point(1050,150),str(plaName) + "'s Score: " + str(plaPool))
                plaTotal.setStyle("bold italic")
                plaTotal.setFace("helvetica")
                plaTotal.setTextColor("white")
                plaTotal.setSize(20)
                plaTotal.draw(win)
                movesLeft = Text(Point(1050,200),"Moves Left: " + str(moves))
                movesLeft.setStyle("bold italic")
                movesLeft.setFace("helvetica")
                movesLeft.setTextColor("white")
                movesLeft.setSize(20)
                movesLeft.draw(win)
                Game.startGame(win)
                plaPool = Game.evaluateScore()
                if plaPool > test:
                    moves = moves + 1
                plaTotal.undraw()
                movesLeft.undraw()
                moves = moves - 1
                
            againButton.redoButton(win)
            menuButton.redoButton(win)
            quitText.setTextColor("black")
            choiceImage.draw(win)
            playText.draw(win)
            menuText.draw(win)
            winTag = Text(Point(1100,125),str(plaName) + "'s Final Score: " + str(plaPool))
            winTag.setFace("helvetica")
            winTag.setStyle("bold italic")
            winTag.setTextColor("white")
            winTag.setSize(20)
            winTag.draw(win)
            scoreList = Game.getScore((plaName,plaPool))
            
            overTag.draw(win)

        elif menuButton.clicked(pt):
            win.close()
            main()
        pt = win.getMouse()
        
    win.close()

if __name__=="__main__": 
    main()

    
    
                
