from element import Element

# This class contains helper functions to make it easier to draw
# a progressbar. However, it doesn't draw a progressbar. It just
# returns a text that can be drawn by the client.
class ProgressBar(Element):
    # Creates a new progressbar
    # length must be an integer and represents the number of bars in the progressbar
    # character must be a char (or a string with on element). This character gets
    # used to represent the filled section of the progressbar
    # value must be an integer between 0 and 100 (including those values)
    def __init__(self, length, character, value):
        self.progress = value
        self.length = length
        self.character = character
        
    # Increases the stored value of the progressbar
    # amount must be a positive whole number
    def increaseProgress(self, amount):
        if(amount < 0):
            return
            
        if (self.progress >= 100 or self.progress + amount > 100):
            self.progress = 100
        else:
            self.progress = self.progress + amount
        
    # Decreases the stored value of the progressbar
    # amount must be a positive whole number
    def decreaseProgress(self, amount):
        if (self.progress <= 0 or self.progress - amount < 0):
            self.progress = 0
        else:
            self.progress = self.progress - amount
    
    # Sets the new stored value
    # value must be an integer between 0 and 100 (inclusive)
    def setProgress(self, value):
        if (value > 100 or value < 0):
            return
        else:
            self.progress = value
    
    # Returns a string that represents the progressbar and that
    # can be drawn anywhere in the application
    def getProgressText(self):
        bars = int(self.progress / int(100 / self.length))
        empty = self.length - bars
        
        return str(self.progress) + "% [" + (self.character * bars) + (" " * empty) + "]"
