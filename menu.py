from abc import ABCMeta, abstractmethod
  
class Menu():
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def setActive(self, state):
        pass

    @abstractmethod
    def getSelectedIndex(self):
        pass
        
    @abstractmethod
    def getSelectedAction(self):
        pass
        
    @abstractmethod
    def redrawMenu(self):
        pass
    
    @abstractmethod
    def moveSelectionUp(self):
        pass

    @abstractmethod
    def moveSelectionDown(self):
        pass

    @abstractmethod
    def moveSelectionLeft(self):
        pass

    @abstractmethod
    def moveSelectionRight(self):
        pass

    @abstractmethod
    def selectionMade(self):
        pass
