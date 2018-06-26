'''
Created on Jun 26, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.FtdFrame import FtdFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom

class Frame_maintgene(FtdFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, nextframe=None, **configs):
        '''
        Constructor
        '''
        FtdFrame.__init__(self, parent, nextframe, **configs)
        self.__frame1 = FtdFrame(self)
        self.__frame1.pack(side=TOP)
        #label1
        self.__label01 = Label(self.__frame1, text="Select the generated file")
        self.__label01.pack(side=TOP, fill=X)
        
        #bottom
        self.add_bottom(self)
    
    
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':None,
                   'Prev':None}
        self.__buttom = Frame_bottom(self, ['Next','Prev'], exFuncs)
        self.__buttom.pack(fill=X)
        
        