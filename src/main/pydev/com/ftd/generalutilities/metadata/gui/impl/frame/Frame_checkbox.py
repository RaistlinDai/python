'''
Created on Jun 25, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.UnFormatableFrame import UnFormatableFrame

class Frame_checkbox(UnFormatableFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, dtos=None, trans=None, **configs):
        '''
        Constructor
        '''
        UnFormatableFrame.__init__(self, parent, dtos, trans, **configs)