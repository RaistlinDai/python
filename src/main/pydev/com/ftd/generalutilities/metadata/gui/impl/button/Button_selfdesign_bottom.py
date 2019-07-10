'''
Created on Jul 10, 2019

@author: ftd
'''
from tkinter import Button

class Button_selfdesign_bottom(Button):
    '''
    classdocs
    '''

    def __init__(self, parent=None, exFuncs=None, btnText='Button', **configs):
        '''
        Constructor
        '''
        Button.__init__(self, parent, **configs)
        self.bind('<Button-1>', self.click_event) #bind button click event
        self.config(text=btnText)
        
        if isinstance(exFuncs, dict):
            self.__selffunc = exFuncs.get('process')
        
    
    '''
    Event
    
    '''
    def click_event(self, event):
        self.__selffunc()