'''
Created on Jul 19, 2018

@author: ftd
'''
from tkinter import Button
from tkinter.filedialog import askopenfilename

class Button_select_file(Button):
    '''
    classdocs
    '''

    def __init__(self, parent=None, exfunc=None, **configs):
        '''
        Constructor
        '''
        Button.__init__(self, parent, **configs)
        self.bind('<Button-1>', self.click_event) #bind button click event
        if not configs['text']:
            self.config(text='...')
        self.__exfunc = exfunc
        
    '''
    Event
    
    '''
    def click_event(self, event):
        
        self.__dic = askopenfilename()
        self.__exfunc(self.__dic)
        