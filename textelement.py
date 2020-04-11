from abc import ABCMeta, abstractmethod
  
class TextComponent():
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, text):
        pass
    
    @abstractmethod
    def getText(self):
        pass

class Text(TextComponent):
    def __init__(self, text):
        self.text = str(text)
        self.length = len(text)
    
    def getText(self):
        # Return the text itself and reset all decorators
        # that'll prevent other text, that gets printed to
        # the console, to be influenced by previous decorators
        return self.text + "\033[m"
        
    def getRawText(self):
        return self.text
        
    def getLength(self):
        return self.length
