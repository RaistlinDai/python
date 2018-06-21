'''
Created on Jun 20, 2018

@author: ftd
'''

class UiObject(object):
    
    def __init__(self, row, column, parentObj=None):
        self.row = row
        self.column = column
        
        if parentObj:
            self.parentObj = parentObj
            print('Parent is not none')