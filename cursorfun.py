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
# and reacts to user input.
#
# 2020 | www.nerdhut.de
#

showProgress = False
statusText = ""
rows, columns = os.popen('stty size', 'r').read().split()

def activateSelected():
    # Call the function that's associated with
    # the selected menu entry
    # The method has to be called here so that
    # the context is correct (otherwise, the
    # menu class wouldn't know the function)
    (activeMenu.getSelectedAction())()
        
def keyPressed(event):
    global rows
    
    if(event.name == "up"):
        activeMenu.moveSelectionUp()
    elif(event.name == "down"):
        activeMenu.moveSelectionDown()
    elif(event.name == "left"):
        activeMenu.moveSelectionLeft()
    elif(event.name == "right"):
        activeMenu.moveSelectionRight()
    elif(event.name == "enter"):
        activateSelected()
    
    redrawScreen()
    
    # Display the pressed key in the last line of the console window
    print("\033[" + str(int(rows) - 1) + ";1H");
    
def returnFromOptions():
    global activeMenu
    activeMenu = mainMenu
    redrawScreen()
    
def options():
    global activeMenu
    activeMenu = MessageDialogue(Text("No options available!"), (Text("OK"), returnFromOptions), displayhelper)
    redrawScreen()
    
def delete():
    global activeMenu
    activeMenu = MessageDialogue(Text("File deleted!"), (Text("OK"), returnFromOptions), displayhelper)
    redrawScreen()
    
def saveDone():
    global activeMenu, showProgress
    showProgress = False
    activeMenu = MessageDialogue(Text("File saved!"), (Text("Close"), returnFromOptions), displayhelper)
    redrawScreen()
    
def doSave():
    progressbar.setProgress(0)
    redrawScreen()
    time.sleep(0.2)
    progressbar.setProgress(35)
    redrawScreen()
    time.sleep(0.15)
    progressbar.setProgress(76)
    redrawScreen()
    time.sleep(0.5)
    progressbar.setProgress(100)
    redrawScreen()
    saveDone()
    
def saveFile():
    global activeMenu, showProgress
    activeMenu = NotificationDialogue(Text("Saving file..."), displayhelper)
    showProgress = True
    redrawScreen()
    doSave()
    
def deleteFile():
    global activeMenu
    activeMenu = YesNoMenu(Text("Are you sure you want to delete this file?"), (Text("Yes"), delete), (Text("No"), returnFromOptions), displayhelper, dangerous = True)
    redrawScreen()
    
def printingDone():
    global statusText, showProgress, activeMenu
    activeMenu = mainMenu
    statusText = "The receipt got printed!"
    showProgress = False
    redrawScreen()
    
def doPrint():
    global statusText, showProgress
    statusText = "Printing..."
    showProgress = True
    
    for i in range(0,101):
        progressbar.setProgress(i)
        time.sleep(0.055)
        redrawScreen()
        
    printingDone()
    
def printReceipt():
    doPrint()
    
def redrawScreen():
    displayhelper.setScreenSize(rows, columns)
    displayhelper.clearScreen()

    rightText = progressbar.getProgressText() if showProgress else ""
    displayhelper.createHeaderBar(int(rows) - 1, statusText, rightText, 47, 30)

    displayhelper.createHeaderBar(1, "", "", 44, 93)
    displayhelper.createHeaderBar(2, "nerdhut | 6x6 Control Firmware", "v1.0 RC", 44, 93)
    displayhelper.createHeaderBar(3, "", "", 44, 93)

    displayhelper.writeToLine(5, LeftAlignedText(ColoredText(HighlightedText(Text("Main Content goes here!"), 97), 45), 2))
    print(LeftAlignedText(Text("This window has: "), 2).getText())
    displayhelper.writeToLine(6, RightAlignedText(Text(str(rows) + " rows and " + str(columns) + " columns."), 2, int(columns)))
    
    displayhelper.writeToLine(8, LeftAlignedText(Text("Please select an option:"), 2))

    activeMenu.redrawMenu()

displayhelper = DisplayHelper(rows, columns)
menuElements = [(Text("[S]ave to logfile"), saveFile),
                (Text("[O]ptions"), options),
                (Text("[D]elete File"), deleteFile),
                (Text("[P]rint receipt"), printReceipt)
]

mainMenu = MainMenu(menuElements, 10, 2, displayhelper)
progressbar = ProgressBar(20, '#', 30)
activeMenu = mainMenu

if __name__ == "__main__":
    try:
        keyboard.on_press(keyPressed, suppress=False)
        redrawScreen()
        
        while True:
            old_rows = rows
            old_columns = columns
            rows, columns = os.popen('stty size', 'r').read().split()
            
            if (old_rows != rows or old_columns != columns):
                redrawScreen()
            
            time.sleep(0.5)
        
    except KeyboardInterrupt:
        quit()
