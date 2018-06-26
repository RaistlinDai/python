'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Button_load import Button_load
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Button_next import Button_next
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.FtdFrame import FtdFrame

class Frame_bottom(FtdFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, exFuncs={}, **configs):
        '''
        Constructor
        '''
        Frame.__init__(self, parent, **configs)
        #button
        loadFunc = None
        if isinstance(exFuncs, dict):
            loadFunc = exFuncs.get('Load')
            nextFunc = exFuncs.get('Next')
        
        self.__loadButton = Button_load(self, loadFunc, text='Load') #set function as input parameter
        self.__loadButton.pack(side=LEFT)
        
        self.__quitButton = Button_next(self, nextFunc, text='Next')
        self.__quitButton.pack(side=RIGHT)
        
        self.adjust_children()
    
    
    def adjust_children(self):
        for child in self.winfo_children():
            if isinstance(child, Button):
                child.config(cursor='hand2')
            
    