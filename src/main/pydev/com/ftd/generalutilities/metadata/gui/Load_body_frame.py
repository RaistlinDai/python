'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *

class Load_body_frame(Frame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, **configs):
        '''
        Constructor
        '''
        Frame.__init__(self, parent, **configs)
        
        feet = StringVar()

        #label1
        self.label01 = Label(self, text="Select or Input the project path:")
        self.label01.grid(column=0, row=1, sticky=(E))
        
        #input
        self.nameInput = Entry(self, width=40, textvariable=feet)
        self.nameInput.grid(column=1, row=1, sticky=(E))
        
        