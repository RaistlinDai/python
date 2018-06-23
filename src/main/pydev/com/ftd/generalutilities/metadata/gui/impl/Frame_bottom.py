'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Button_load import Button_load
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.IFrameConf import IFrameConf
from tkinter.messagebox import askyesno


class Frame_bottom(Frame, IFrameConf):
    '''
    classdocs
    '''


    def __init__(self, parent=None, exFunc=None, **configs):
        '''
        Constructor
        '''
        Frame.__init__(self, parent, **configs)
        #button
        self.loadButton = Button_load(self, exFunc, text='Load') #set function as input parameter
        self.loadButton.grid(column=5, row=0, sticky=(E,S))
        self.loadButton.config(cursor='hand2')
        
        self.quitButton = Button(self, text='Quit', command=self.quit_callback)
        self.quitButton.grid(column=7, row=0, sticky=(E,S))
        self.quitButton.config(cursor='hand2')
        
        self.adjust_children()
    
    
    def adjust_children(self):
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)
            
    
    def quit_callback(self):
        if askyesno('Verify', 'Do you really want to quit?'):
            self.quit()