'''
Created on Jun 25, 2018

@author: ftd
'''
from tkinter import Frame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.frame.IFtdFrame import IFtdFrame


class FtdFrame(Frame, IFtdFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, **params):
        '''
        Constructor
        '''
        Frame.__init__(self, parent, params)