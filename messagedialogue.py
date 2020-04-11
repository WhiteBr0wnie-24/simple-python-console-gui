from menu import Menu
from displayhelper import *
from textdecorator import *
from textelement import Text

# This class represents a simple message dialogue that displays a message and an OK button:
#
# ----------------------
# |                    |
# |                    |
# |      Message       |
# |                    |
# |              [OK]  |
# ----------------------
#
# This class handles all the drawing and input updates. The client simply has to
# call the appropriate methods.
#
class MessageDialogue(Menu):

    # Creates a new message dialogue that displays a text and a button
    # message must be a Text object and may have any number of decorators applied to it.
    # If the underlying text contains more than 60 characters, it gets truncated
    # button must be a tuple that consists of a Text object and a function that should
    # be called if the user clicks the button: (Text, Function)
    # displayhelper must be a DisplayHelper object that's used to draw the elements
    # on the screen. It must always hold a reference to the correct console size to function.
    def __init__(self, message, button, displayhelper):
        if (len(message.getRawText()) > 60):
            message = Text(message.getRawText()[:57] + "...")
            
        self.buttonText = button[0]
        self.buttonAction = button[1]
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
    
    # Returns the action that got associated with the OK button
    def getSelectedAction(self):
        return self.buttonAction

    # Forces the menu to be (re)drawn
    def redrawMenu(self):
        boxWidth = self.heading.getLength() + 10
        boxHeight = 10
        boxPosition = self.displayhelper.createCenteredBox(boxWidth, boxHeight, 47)
        
        headingText = ColoredText(HighlightedText(LeftAlignedText(self.heading, boxPosition[0] + 4), 47), 30)
        buttonText = InvertedText(LeftAlignedText(PaddedText(self.buttonText, 3), boxPosition[0] - 1 + boxWidth - 1 - 6 - 5))
        
        self.displayhelper.writeToLine(boxPosition[1] + 2, headingText)
        self.displayhelper.writeToLine(boxPosition[1] + boxHeight - 2, buttonText)
    
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
