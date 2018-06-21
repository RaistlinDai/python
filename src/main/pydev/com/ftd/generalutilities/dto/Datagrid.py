'''
Created on Jun 20, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.dto.UiObject import UiObject
from src.main.pydev.com.ftd.generalutilities.dto.Datagridtable import Datagridtable

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