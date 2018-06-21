'''
Created on Jun 20, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.metadata.dto.UiObject import UiObject

class Field(UiObject):
    
    def __init__(self, row, column, tablename, name, parent=None):
        UiObject.__init__(self, row, column, parent)
        self.__tablename = tablename
        self.__name = name

    def get_tablename(self):
        return self.__tablename


    def get_name(self):
        return self.__name


    def set_tablename(self, value):
        self.__tablename = value


    def set_name(self, value):
        self.__name = value


    def del_tablename(self):
        del self.__tablename


    def del_name(self):
        del self.__name
    
        