'''
Created on Jun 25, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FtdFrame import FtdFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.frame.IUnFormatableFrame import IUnFormatableFrame

class Frame_checkbox(FtdFrame, IUnFormatableFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, **configs):
        '''
        Constructor
        '''
        Frame.__init__(self, parent, **configs)