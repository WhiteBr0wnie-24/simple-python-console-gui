import math

# This class represents a helper that can draw various commonly used objects
class DisplayHelper:

    # Creates a new helper. rows and columns must be integers and they must
    # always hold the correct number of rows and columns of the active
    # console window. The client must update these values if the console
    # size changes
    def __init__(self, rows, columns):
        self.rows = int(rows)
        self.columns = int(columns)

    # Can be used to update the rows and columns
    def setScreenSize(self, r, c):
        self.rows = int(r)
        self.columns = int(c)

    # Creates a bar that spans over the entire width of the console window with two
    # text fields and a distinct background color.
    # line must be an integer (larger than 0). The bar gets placed in this row of the console.
    # leftText and rightText must be strings and may not be longer than the entire console
    # width (when combined).
    # backgroundColor: The bar will have this color. This must be a value from the BackgroundColor enum
    # fontColor: The text will have this color. Must be a value from the FontColor enum.
    def createHeaderBar(self, line, leftText, rightText, backgroundColor, fontColor):
        backgroundColor = str(backgroundColor)
        fontColor = str(fontColor)
        line = str(line)
        
        # Create the empty space in the center
        for x in range(1, self.columns + 1):
            print("\033[" + line + ";" + str(x) + "H\033[" + backgroundColor + "m ")
        
        # Only print the text if it fits on the screen
        if (len(leftText) + len(rightText) + 4 > self.columns):
            return

        # Print the left text
        print("\033[" + line + ";1H\033[" + backgroundColor + "m\033[" + fontColor + "m  " + leftText);
            
        # Print the right text
        print("\033[" + line + ";" + str(self.columns - (len(rightText) + 1)) + "H\033[" + backgroundColor + "m\033[" + fontColor + "m" + rightText + "  \033[0m")

    # Creates a box with a set width and height that sits in the middle of the screen
    # (centered vertically and horizontally) and that has a specific color.
    # width must be an integer between 1 and the number of columns in the console
    # height must be an integer between 1 and the number of rows in the console
    # color must be a color from the BackgroundColor enum
    def createCenteredBox(self, width, height, color):
        boxStartX = math.ceil((self.columns / 2) - (width / 2))
        boxStartY = math.ceil((self.rows / 2) - (height / 2))
        
        self.createBox(boxStartX, boxStartY, width, height, color)
        
        return (boxStartX, boxStartY)

    # Creates a box with a set width and height that can sit anywhere in the console.
    # startLine, startColumn must be integers greater than 0
    # width must be an integer between 1 and the number of columns in the console
    # height must be an integer between 1 and the number of rows in the console
    # If the size of the box + start values is larger than the console window, the
    # behaviour of this function is undefined (some console might overflow and hide
    # the output, but most consoles will wrap to the next line and draw a mess).
    # color must be a color from the BackgroundColor enum
    def createBox(self, startLine, startColumn, width, height, color):
        text = ""
        for y in range (0, height):
            for x in range (0, width):
                # Move the cursor to the start
                text += ("\033[" + str(startColumn + y) + ";" + str(startLine + x) + "H\033[" + str(color) + "m " + "\033[0m")
                
        print(text)

    # Clears the entire console window
    def clearScreen(self):
        text = ""
        for _ in range(1, self.rows + 1):
            text += ("\033[2K\n")
            text += ("\033[E\n")
        
        print(text)
        
    # Writes a text to a specific line
    # line must be an integer
    # text must be a Text object that may be decorated
    def writeToLine(self, line, text):
        if (line <= 0):
            line = 1
            
        if (line > self.rows):
            line = self.rows
        
        print("\033[" + str(line) + ";1H" + text.getText() + "\033[0m");
