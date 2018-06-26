'''
Created on Jun 25, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.FtdFrame import FtdFrame

class Frame_selectbox(FtdFrame):
    '''
    classdocs
    '''


    def __init__(self, labelname, parent=None, **configs):
        '''
        Constructor
        '''
        Frame.__init__(self, parent, **configs)
        #checkbox
        checkbox = Checkbutton(self)
        checkbox.pack(side=LEFT)
        lab = Label(self, text=labelname)
        lab.pack(side=LEFT)