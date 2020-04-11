from menu import Menu
from displayhelper import *
from textdecorator import *
from textelement import Text

# This class represents a simple message dialogue that displays a message:
#
# ----------------------
# |                    |
# |                    |
# |      Message       |
# |                    |
# |                    |
# ----------------------
#
# This class handles all the drawing and input updates. The client simply has to
# call the appropriate methods.
#
class NotificationDialogue(Menu):

    # Creates a new message dialogue
    # message must be a Text object that may be decorated. If the underlying text
    # contains more than 60 characters, it gets truncated
    # displayhelper must be a DisplayHelper object that's used to draw the elements
    # on the screen. It must always hold a reference to the correct console size to function.
    def __init__(self, message, displayhelper):
        if (len(message.getRawText()) > 60):
            message = Text(message.getRawText()[:57] + "...")
        
        self.heading = message
        self.active = False
        self.displayhelper = displayhelper
    
    # Sets this menu's active flag to the value of state
    # state must be boolean
    def setActive(self, state):
        self.active = state

    # This function has no effect in this dialogue.
    def getSelectedIndex(self):
        pass
        
    # This function has no effect in this dialogue.
    def getSelectedAction(self):
        pass

    # Forces the menu to be (re)drawn
    def redrawMenu(self):
        boxWidth = 30
        boxHeight = 5
        boxPosition = self.displayhelper.createCenteredBox(boxWidth, boxHeight, 47)
        
        headingText = ColoredText(HighlightedText(LeftAlignedText(self.heading, boxPosition[0] + 4), 47), 30)
        
        self.displayhelper.writeToLine(boxPosition[1] + 2, headingText)
    
    # This function has no effect in this dialogue.
    def moveSelectionUp(self):
        pass

    # This function has no effect in this dialogue.
    def moveSelectionDown(self):
        pass
    
    # This function has no effect in this dialogue.
    def moveSelectionLeft(self):
        pass
        
    # This function has no effect in this dialogue.
    def moveSelectionRight(self):
        pass
    
    # This function has no effect in this dialogue.
    def selectionMade(self):
        pass
