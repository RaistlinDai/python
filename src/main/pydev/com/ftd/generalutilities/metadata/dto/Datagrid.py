'''
Created on Jun 20, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.metadata.dto.UiObject import UiObject
from src.main.pydev.com.ftd.generalutilities.metadata.dto.Datagridtable import Datagridtable

class Datagrid(UiObject):
    '''
    classdocs
    '''
    
    def __init__(self, row, column, tablename, datagridtable, parent=None):
        '''
        Constructor
        '''
        UiObject.__init__(self, row, column, parent)
        self.__tablename = tablename
        
        if isinstance(datagridtable, Datagridtable):
            self.__datagridtable = datagridtable
        else:
            self.__datagridtable = None

    def get_tablename(self):
        return self.__tablename


    def get_datagridtable(self):
        return self.__datagridtable


    def set_tablename(self, value):
        self.__tablename = value


    def set_datagridtable(self, value):
        if isinstance(value, Datagridtable):
            self.__datagridtable = value
        else:
            self.__datagridtable = None


    def del_tablename(self):
        del self.__tablename


    def del_datagridtable(self):
        del self.__datagridtable

    