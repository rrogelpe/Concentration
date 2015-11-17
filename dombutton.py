import math
from graphics import*
from pile import*
from tile import*

class dominoButton:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns true if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label, front, back):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.front = front
        self.back = back
        self.active = True
    
    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()
    

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def setColor(self,color):
        self.rect.setFill(color)

    def undoButton(self):
        self.rect.undraw()
        self.label.undraw()

    def redoButton(self,win):
        self.rect.draw(win)
        self.label.draw(win)
        
    def setBack(self,win):
        self.back.draw(win)

    def setFront(self,win):
        self.front.draw(win)
        
    def reveal(self):
        self.back.undraw()
    
if __name__=="__main__": 
    main()

    
