from abc import ABCMeta, abstractmethod

class Decorator():
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def __init__(self, textElement):
        self.textElement = textElement
    
    @abstractmethod
    def getText(self):
        return self.textElement.getText()
        
    @abstractmethod
    def getLength(self):
        return self.textElement.getLength()
        
    @abstractmethod
    def getRawText(self):
        return self.textElement.getRawText()

# Renders the underlying text element with a bold font
class BoldText(Decorator):
    # Creates a new instance of this decorator
    # textElement must be a Text object and may have any number of decorators applied to it
    def __init__(self, textElement):
        self.textElement = textElement
        
    def getText(self):
        return "\033[1m" + self.textElement.getText()
        
# Renders the underlying text element with inverted colors
class InvertedText(Decorator):
    # Creates a new instance of this decorator
    # textElement must be a Text object and may have any number of decorators applied to it
    def __init__(self, textElement):
        self.textElement = textElement
        
    def getText(self):
        return "\033[7m" + self.textElement.getText()

# Renders the underlying text element with a blinking font
class BlinkingText(Decorator):
    # Creates a new instance of this decorator
    # textElement must be a Text object and may have any number of decorators applied to it
    def __init__(self, textElement):
        self.textElement = textElement
        
    def getText(self):
        return "\033[5m" + self.textElement.getText()

# Renders the underlying text element with an underlined font
class UnderlinedText(Decorator):
    # Creates a new instance of this decorator
    # textElement must be a Text object and may have any number of decorators applied to it
    def __init__(self, textElement):
        self.textElement = textElement
        
    def getText(self):
        return "\033[4m" + self.textElement.getText()
        
# Renders the underlying text element with a specific foreground color
class ColoredText(Decorator):
    # Creates a new instance of this decorator
    # textElement must be a Text object and may have any number of decorators applied to it
    # color must be one of the colors defined in the FontColor enum
    def __init__(self, textElement, color):
        self.textElement = textElement
        self.color = str(color)
        
    def getText(self):
        return "\033[" + self.color + "m" + self.textElement.getText()

# Renders the underlying text element with a background color
class HighlightedText(Decorator):
    # Creates a new instance of this decorator
    # textElement must be a Text object and may have any number of decorators applied to it
    # highlightColor must be one of the colors defined in the FontColor enum
    def __init__(self, textElement, highlightColor):
        self.textElement = textElement
        self.highlightColor = str(highlightColor)
        
    def getText(self):
        return "\033[" + self.highlightColor + "m" + self.textElement.getText()

# Not implemented
class AbsolutePositionedText():
    pass # TODO

# Renders the underlying text element on the left side of the screen with
# a certain padding on the left
class LeftAlignedText(Decorator):
    # Creates a new instance of this decorator
    # textElement must be a Text object and may have any number of decorators applied to it
    # padding must be an integer. If a value <= 0 is supplied, 1 is used for the padding
    def __init__(self, textElement, padding):
        self.textElement = textElement
        self.padding = (padding) if (padding >= 0) else 1
        
    def getText(self):
        return "\033[" + str(self.padding) + "C" + self.textElement.getText()

# Renders the underlying text element on the right side of the screen with
# a certain padding on the right
class RightAlignedText(Decorator):
    # Creates a new instance of this decorator
    # textElement must be a Text object and may have any number of decorators applied to it
    # padding must be an integer. If a value <= 0 is supplied, 1 is used for the padding
    # columns must be an integer that contains the number of columns in the console window
    def __init__(self, textElement, padding, columns):
        self.textElement = textElement
        # Subtract 2 from the padding because the first character is insterted
        # one position after the cursor and the first index of the console is 1.
        self.padding = padding if (padding >= 0) else 1
        self.columns = columns if (columns > self.padding) else 80
        
    def getText(self):
        return "\033[" + str(self.columns - self.textElement.getLength() - self.padding) + "C" + self.textElement.getText()

# Adds spaces to the both sides of the underlying Text object
class PaddedText(Decorator):
    # Creates a new instance of this decorator
    # textElement must be a Text object and may have any number of decorators applied to it
    # padding must be an integer. If a value <= 0 is supplied, 1 is used for the padding
    def __init__(self, textElement, padding):
        self.textElement = textElement
        self.padding = padding if (padding >= 0) else 1
        
    def getText(self):
        return (" " * self.padding) + self.textElement.getRawText() + (" " * self.padding)
