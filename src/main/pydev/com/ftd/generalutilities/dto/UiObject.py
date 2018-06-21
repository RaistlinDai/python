'''
Created on Jun 20, 2018

@author: ftd
'''

class UiObject(object):
    
    def __init__(self, row, column, parentObj=None):
        if isinstance(row, int):
            self.__row = row
        else:
            self.__row = 0
            
        if isinstance(column, int):
            self.__column = column
        else:
            self.__column = 0
        
        if parentObj:
            self.__parentObj = parentObj
            
            
    def get_row(self):
        return self.__row
    
    def set_row(self, row):
        if isinstance(row, int):
            self.__row = row
    
    def get_column(self):
        return self.__column
    
    def set_column(self, column):
        if isinstance(column, int):
            self.__column = column