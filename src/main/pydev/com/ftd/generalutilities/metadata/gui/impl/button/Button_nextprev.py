'''
Created on Jun 26, 2018

@author: ftd
'''
from tkinter import Button
from tkinter.messagebox import askyesno

class Button_nextprev(Button):
    '''
    classdocs
    '''


    def __init__(self, parent=None, exFuncs=None, module=None, **configs):
        '''
        Constructor
        '''
        Button.__init__(self, parent, **configs)
        self.bind('<Button-1>', self.click_event)
        
        self.__module = module
        
        if isinstance(exFuncs, dict):
            self.__click_event = exFuncs.get('process')
            self.__before_click_event = exFuncs.get('before')
        else:
            self.__click_event = None
            self.__before_click_event = None
    
        
    '''
    Event
    
    '''
    def click_event(self, event):
        #Before button click
        if not self.before_click_event():
            return 
        
        if self.__module == 'Next':
            title = "Note"
            message = 'Please verify your selection before going to next step.'
        else:
            title = "Warning"
            message = 'Are you sure roll back to the previous step?'
        
        if askyesno(title, message):
            if self.__click_event:
                self.__click_event()
                
    
    def before_click_event(self):
        if self.__before_click_event:
            result = self.__before_click_event()
            if result:
                return True
            else:
                return False
        else:
            return True
        