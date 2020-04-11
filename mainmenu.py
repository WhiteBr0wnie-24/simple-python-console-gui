from menu import Menu
from displayhelper import *
from textdecorator import *
from textelement import Text

# This class represents a simple menu that can have any number of elements.
# Each element gets displayed in the order they are supplied to the constructor:
#
# Option A
# Option B
# Option Duck
#
# This class handles all the drawing and input updates. The client simply has to
# call the appropriate methods.
#
class MainMenu(Menu):

    # Creates a new main menu that displays the menu elements in a vertical list
    # The first option is selected by default.
    # elements must be an array that contains tuples of Text objects and an
    # associated action: [(Text, Function), (Text, Function), ...]. The array may
    # contain any number of elements. If the array contains more elements than
    # there are rows in the console window, the behaviour is undefined.
    # startRow and startColumn must both be integers and they can be used
    # to position the menu. Position (1,1) is the top-left corner of the console.
    # displayhelper must be a DisplayHelper object that's used to draw the elements
    # on the screen. It must always hold a reference to the correct console size to function.
    def __init__(self, elements, startRow, startColumn, displayhelper):
        self.elements = elements
        self.startColumn = startColumn
        self.displayhelper = displayhelper
        self.startRow = startRow
        self.selected = 0
        self.active = False
    
    # Sets this menu's active flag to the value of state
    # state must be boolean
    def setActive(self, state):
        self.active = state

    # Returns the currently selected option as an integer starting with 0
    def getSelectedIndex(self):
        return self.selected
        
    # Returns the function that is linked to the currently selected menu option.
    def getSelectedAction(self):
        return self.elements[self.selected][1]

    # Forces the menu to be (re)drawn
    def redrawMenu(self):
        for i in range(0, len(self.elements)):
            if (i == self.selected):
                self.displayhelper.writeToLine((self.startRow + i), LeftAlignedText(InvertedText(self.elements[i][0]), self.startColumn))
            else:
                self.displayhelper.writeToLine((self.startRow + i), LeftAlignedText(self.elements[i][0], self.startColumn))
    
    # Moves the cursor up and selects the previous option.
    # If the cursor gets moved beyond the first element, it gets moved to the
    # last element
    def moveSelectionUp(self):
        if self.selected <= 0:
            self.selected = len(self.elements) - 1
        else:
            self.selected = self.selected - 1

    # Moves the cursor down and selects the next option.
    # If the cursor gets moved beyond the last element, it gets moved to the
    # first element
    def moveSelectionDown(self):
        if self.selected >= len(self.elements) - 1:
            self.selected = 0
        else:
            self.selected = self.selected + 1
    
    # This function has no effect in this dialogue.
    def moveSelectionLeft(self):
        pass
        
    # This function has no effect in this dialogue.
    def moveSelectionRight(self):
        pass
    
    # This function has no effect in this dialogue.
    def selectionMade(self):
        pass
