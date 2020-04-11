from menu import Menu
from displayhelper import *
from textdecorator import *
from textelement import Text

# This class represents a simple yes/no dialogue that requests a binary decision:
#
# ----------------------
# |                    |
# |                    |
# |      Message       |
# |                    |
# |  [No]       [Yes]  |
# ----------------------
#
# This class handles all the drawing and input updates. The client simply has to
# call the appropriate methods.
#
class YesNoMenu(Menu):
    
    # Creates a new yes/no dialogue that displays a text and two buttons
    # The negative option is selected by default.
    # heading must be a Text object and may have any number of decorators applied to it.
    # If the underlying text contains more than 60 characters, it gets truncated
    # yes must be a tuple that consists of a Text object and a function that should
    # be called if the user clicks the yes-button: (Text, Function)
    # no must have the same format as yes
    # displayhelper must be a DisplayHelper object that's used to draw the elements
    # on the screen. It must always hold a reference to the correct console size to function.
    # dangerous is optional. If set to true, it will apply a blink decorator to the heading text
    def __init__(self, heading, yes, no, displayhelper, dangerous = False):
        if (len(heading.getRawText()) > 60):
            heading = Text(heading.getRawText()[:57] + "...")
            
        self.yesText = yes[0]
        self.noText = no[0]
        self.yesAction = yes[1]
        self.noAction = no[1]
        self.heading = heading
        self.dangerous = dangerous
        self.selected = 0
        self.active = False
        self.displayhelper = displayhelper
    
    # Sets this menu's active flag to the value of state
    # state must be boolean
    def setActive(self, state):
        self.active = state

    # Returns the currently selected option as an integer starting with 0
    # in this dialogue, the negative option is always 0, the positive option
    # is represented by 1.
    def getSelectedIndex(self):
        return self.selected
        
    # Returns the function that is linked to the currently selected menu option.
    def getSelectedAction(self):
        if (self.selected == 0):
            return self.noAction
        else:
            return self.yesAction

    # Forces the menu to be (re)drawn
    def redrawMenu(self):
        boxWidth = len(self.heading.getRawText()) + 10
        boxHeight = 10
        boxPosition = self.displayhelper.createCenteredBox(boxWidth, boxHeight, 47)
        
        headingText = HighlightedText(LeftAlignedText(self.heading, boxPosition[0] + 4), 47)
        noText = LeftAlignedText(PaddedText(self.noText, 3), boxPosition[0] + 4)
        yesText = LeftAlignedText(PaddedText(self.yesText, 3), boxPosition[0] - 1 + boxWidth - 1 - noText.getLength() - 6 - 5)
        
        if (self.dangerous):
            headingText = ColoredText(BlinkingText(headingText), 31)
        else:
            headingText = ColoredText(headingText, 30)
            
        if (self.selected == 0):
            noText = InvertedText(noText)
            yesText = ColoredText(HighlightedText(yesText, 47), 30)
        else:
            yesText = InvertedText(yesText)
            noText = ColoredText(HighlightedText(noText, 47), 30)
        
        self.displayhelper.writeToLine(boxPosition[1] + 2, headingText)
        self.displayhelper.writeToLine(boxPosition[1] + boxHeight - 2, yesText)
        self.displayhelper.writeToLine(boxPosition[1] + boxHeight - 2, noText)
    
    # This function has no effect in this dialogue.
    def moveSelectionUp(self):
        pass

    # This function has no effect in this dialogue.
    def moveSelectionDown(self):
        pass
    
    # Moves the cursor to the left and selects the previous option.
    # If the cursor gets moved beyond the first element, it gets moved to the
    # last element
    def moveSelectionLeft(self):
        self.selected = 0 if self.selected == 1 else 1
    
    # Moves the cursor to the right and selects the next option.
    # If the cursor gets moved beyond the last element, it gets moved to the
    # first element
    def moveSelectionRight(self):
        self.moveSelectionLeft()
    
    # This function has no effect in this dialogue.
    def selectionMade(self):
        pass
