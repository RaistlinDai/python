'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.IFrameConf import IFrameConf
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Button_openfile import Button_openfile

class Frame_body_load(Frame, IFrameConf):
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
        self.__label01 = Label(self, text="Select or Input the project path:")
        self.__label01.grid(column=0, row=1, sticky=(W))
        
        #input
        self.__dicinput = Entry(self, width=40, textvariable=feet)
        self.__dicinput.grid(column=0, row=2, sticky=(E))
        
        self.__dicload = Button_openfile(self, self.reset_dicinput)
        self.__dicload.grid(column=1, row=2, sticky=(W))
        
        #focus
        self.__dicinput.focus()
        
    
    def reset_dicinput(self, dicname):
        self.__dicinput.delete(0, END)
        self.__dicinput.insert(END, dicname)