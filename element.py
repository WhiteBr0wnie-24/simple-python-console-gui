from abc import ABCMeta, abstractmethod
  
class Element():
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass
