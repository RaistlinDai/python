'''
Created on Jun 22, 2018

@author: ftd
'''
from tkinter import Button

class Load_button(Button):
    '''
    classdocs
    '''


    def __init__(self, parent=None, exFunc=None, **configs):
        '''
        Constructor
        '''
        Button.__init__(self, parent, **configs)
        self.bind('<Button-1>', self.click_event) #bind button click event
        self.exfunc = exFunc
        
    '''
    Event
    
    '''
    def click_event(self, event):
        
        print('Message', 'Test this, %s' % self.exfunc())