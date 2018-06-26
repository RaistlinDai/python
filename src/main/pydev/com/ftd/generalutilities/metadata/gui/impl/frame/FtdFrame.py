'''
Created on Jun 25, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.frame.IFtdFrame import IFtdFrame
from builtins import AttributeError


class FtdFrame(Frame, IFtdFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, nextframe=None, **configs):
        '''
        Constructor
        '''
        Frame.__init__(self, parent, **configs)
        #next frame
        self.nextframe = nextframe
        
        #layout maintain
        self.adjust_children(parent)
        
    
    def adjust_children(self, master):
        for child in self.winfo_children():
            try:
                child.set_conf(font=self.labelfont, bg='white', fg='black', relief=RAISED)
            except AttributeError:
                continue
            
            if isinstance(child, Button):
                child.config(cursor='hand2')
        