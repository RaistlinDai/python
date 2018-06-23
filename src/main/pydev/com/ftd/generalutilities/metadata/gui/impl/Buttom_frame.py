'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Load_button import Load_button
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.IFrameConf import IFrameConf


class Buttom_frame(Frame, IFrameConf):
    '''
    classdocs
    '''


    def __init__(self, parent=None, exFunc=None, **configs):
        '''
        Constructor
        '''
        Frame.__init__(self, parent, **configs)
        #button
        self.loadButton = Load_button(self, exFunc, text='Load') #set function as input parameter
        self.loadButton.grid(column=5, row=0, sticky=(E,S))
        self.loadButton.config(cursor='hand2')
        
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(column=7, row=0, sticky=(E,S))
        self.quitButton.config(cursor='hand2')
        
        self.adjust_children()
    
    
    def adjust_children(self):
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)