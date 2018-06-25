'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.IFrameConf import IFrameConf
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Button_openfile import Button_openfile

class Frame_dicload(Frame, IFrameConf):
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
        self.__label01 = Label(self, text="Select or Input the project src path:")
        #self.__label01.grid(column=0, row=1, sticky=(W))
        self.__label01.pack(side=TOP, fill=X)
        #input
        self.__dicinput = Entry(self, width=40, textvariable=feet)
        #self.__dicinput.grid(column=0, row=2, sticky=(E))
        self.__dicinput.pack(side=LEFT, fill=Y)
        #button
        self.__dicload = Button_openfile(self, self.reset_dicinput, height=1)
        #self.__dicload.grid(column=1, row=2, sticky=(W))
        self.__dicload.pack(side=LEFT)
        #focus
        self.__dicinput.focus()
        
    
    def reset_dicinput(self, dicname):
        self.__dicinput.delete(0, END)
        self.__dicinput.insert(END, dicname)
        
        
    def get_dicinput(self):
        return self.__dicinput.get()
        
        
        