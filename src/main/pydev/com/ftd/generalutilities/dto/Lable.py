'''
Created on Jun 20, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.dto.UiObject import UiObject

class Label(UiObject):
    
    def __init__(self, row, column, name, parent=None):
        UiObject.__init__(self, row, column, parent)
        self.__name = name
        