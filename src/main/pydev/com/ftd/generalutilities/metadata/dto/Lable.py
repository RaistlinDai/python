'''
Created on Jun 20, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.metadata.dto.UiObject import UiObject

class Label(UiObject):
    
    def __init__(self, row, column, name, parent=None):
        UiObject.__init__(self, row, column, parent)
        self.__name = name

    def get_name(self):
        return self.__name


    def set_name(self, value):
        self.__name = value


    def del_name(self):
        del self.__name

    