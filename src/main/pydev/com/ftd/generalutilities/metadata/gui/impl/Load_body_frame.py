'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.IFrameConf import IFrameConf

class Load_body_frame(Frame, IFrameConf):
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
        self.label01.grid(column=0, row=1, sticky=(W))
        
        #input
        self.nameInput = Entry(self, width=40, textvariable=feet)
        self.nameInput.grid(column=0, row=2, sticky=(E))
        
        