'''
Created on Jun 25, 2018

@author: ftd
'''
from tkinter import *

class Frame_selectbox(Frame):
    '''
    classdocs
    '''


    def __init__(self, labelname, parent=None, **configs):
        '''
        Constructor
        '''
        Frame.__init__(self, parent, **configs)
        #checkbox
        checkbox = Checkbutton()
        checkbox.pack(side=LEFT)
        lab = Label(self, text=labelname)
        lab.pack(side=RIGHT)