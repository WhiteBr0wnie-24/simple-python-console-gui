import os
import io
import sys
import time
from textdecorator import *
from textelement import Text
import keyboard
from displayhelper import *
from mainmenu import MainMenu
from yesnomenu import YesNoMenu
from messagedialogue import MessageDialogue
from notificationdialogue import NotificationDialogue
from progressbar import ProgressBar

#
#
# This is a sample application that creates a simple GUI
# and reacts to the user's input.
#
# 2020 | www.nerdhut.de
#

menuElements = [(ColoredText(HighlightedText(Text("Subscribe"), 47), 35), lambda x : x),
                (ColoredText(HighlightedText(Text("Like"), 47), 35), lambda x : x),
                (ColoredText(HighlightedText(Text("Share"), 47), 35), lambda x : x),
                (ColoredText(HighlightedText(Text(""), 47), 35), lambda x : x),
                (ColoredText(HighlightedText(Text("Exit"), 47), 35), lambda x : x)
]

rows, columns = os.popen('stty size', 'r').read().split()
displayhelper = DisplayHelper(rows, columns)
menuInitialized = False
activeMenu = MainMenu(menuElements, 1, 1, displayhelper)
        
def keyPressed(event):
    if(event.name == "up"):
        activeMenu.moveSelectionUp()
    elif(event.name == "down"):
        activeMenu.moveSelectionDown()
    elif(event.name == "left"):
        activeMenu.moveSelectionLeft()
    elif(event.name == "right"):
        activeMenu.moveSelectionRight()
    
    redrawScreen()
    
    # Display the pressed key in the last line of the console window
    print("\033[" + str(int(rows) - 1) + ";1H");

def options():
    pass
    
def saveFile():
    pass
    
def deleteFile():
    pass
    
def printReceipt():
    pass
    
def initMenu(boxPos):
    global activeMenu
    activeMenu = MainMenu(menuElements, boxPos[1] + 5, boxPos[0] + 2, displayhelper)
    
def redrawScreen():
    global menuInitialized
    displayhelper.setScreenSize(rows, columns)
    displayhelper.clearScreen()
    
    displayhelper.createBox(1, 1, int(columns), int(rows) - 1, 46)
    boxPos = displayhelper.createCenteredBox(40, 20, 100)
    displayhelper.createBox(boxPos[0] - 1, boxPos[1] - 1, 40, 20, 47)
    
    if (not menuInitialized):
        initMenu(boxPos)
        menuInitialized = True
    
    displayhelper.createHeaderBar(int(rows) - 1, "Ready!", "", "47", "30")
    
    displayhelper.writeToLine(boxPos[1] + 1, LeftAlignedText(ColoredText(HighlightedText(Text("Please select an option:"), 47), 30), boxPos[0] + 2))
    
    activeMenu.redrawMenu()

if __name__ == "__main__":
    try:
        keyboard.on_press(keyPressed, suppress=False)
        menuInitialized = False
        redrawScreen()
        
        while True:
            old_rows = rows
            old_columns = columns
            rows, columns = os.popen('stty size', 'r').read().split()
            
            if (old_rows != rows or old_columns != columns):
                menuInitialized = False
                redrawScreen()
            
            time.sleep(0.5)
        
    except KeyboardInterrupt:
        quit()
