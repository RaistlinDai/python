'''
Created on Jun 22, 2018

@author: ftd
'''
from tkinter import Button
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Popup_filelist import Popup_filelist

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
        
        print('Message', 'No event triggered。')
        popup = Popup_filelist()
        popup.grab_set()
        popup.focus_set()
        popup.wait_window()