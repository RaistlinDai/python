'''
Created on Jul 10, 2019

@author: ftd
'''
from tkinter import Button

class Button_selfdesign(Button):
    '''
    classdocs
    '''

    def __init__(self, parent=None, exfunc=None, btnText='Button', **configs):
        '''
        Constructor
        '''
        Button.__init__(self, parent, **configs)
        self.bind('<Button-1>', self.click_event) #bind button click event
        self.config(text=btnText)
        self.__exfunc = exfunc
        
    '''
    Event
    
    '''
    def click_event(self, event):
        self.__exfunc()
        
        
    