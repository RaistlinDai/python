'''
Created on Jun 20, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.dto.UiObject import UiObject

class Field(UiObject):
    
    def __init__(self, row, column):
        UiObject.__init__(self, row, column)