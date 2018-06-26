'''
Created on Jun 26, 2018

@author: ftd
'''
from tkinter import Button

class Button_prev(Button):
    '''
    classdocs
    '''


    def __init__(self, parent=None, exFuncs=None, **configs):
        '''
        Constructor
        '''
        Button.__init__(self, parent, **configs)
        self.bind('<Button-1>', self.click_event)
        
        self.__exfunc = exFuncs
        
        
    '''
    Event
    
    '''
    def click_event(self, event):
        if self.__exfunc:
            self.__exfunc()
                
    