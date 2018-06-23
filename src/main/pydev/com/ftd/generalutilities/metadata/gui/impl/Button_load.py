'''
Created on Jun 22, 2018

@author: ftd
'''
from tkinter import Button

class Button_load(Button):
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
        
        if not self.exfunc:
            print('Message', 'No event triggered。')
            #print('Message', 'No event triggered, %s' % self.exfunc())