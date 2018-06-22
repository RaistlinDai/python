'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.Load_button import Load_button


class Buttom_frame(Frame):
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
        self.quitButton = Button(self, text='Quit', command=self.quit)
        
        self.loadButton.grid(column=3, row=3, sticky=(E,S))
        self.quitButton.grid(column=4, row=3, sticky=(E,S))
        
        self.adjust_children()
    
    
    def adjust_children(self):
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)