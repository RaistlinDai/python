'''
Created on Jun 20, 2018

@author: ftd
'''

class uiObject(object):
    
    def __init__(self, row, column, parentObj):
        self.row = row
        self.column = column
        self.parentObj = parentObj