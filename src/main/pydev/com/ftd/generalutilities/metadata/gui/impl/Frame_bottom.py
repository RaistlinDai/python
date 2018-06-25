'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Button_load import Button_load
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
        
        self.loadButton = Button_load(self, loadFunc, text='Load') #set function as input parameter
        self.loadButton.pack(side=LEFT)
        
        self.quitButton = Button(self, text='Next', command=self.next_callback)
        self.quitButton.pack(side=RIGHT)
        
        self.adjust_children()
    
    
    def adjust_children(self):
        for child in self.winfo_children():
            if isinstance(child, Button):
                child.config(cursor='hand2')
            
    
    def next_callback(self):
        pass