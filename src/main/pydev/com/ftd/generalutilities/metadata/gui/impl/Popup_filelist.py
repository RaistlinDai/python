'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Frame_selectbox import Frame_selectbox

class Popup_filelist(Toplevel):
    '''
    classdocs
    '''


    def __init__(self, filelists, parent=None, **configs):
        '''
        Constructor
        '''
        Toplevel.__init__(self, parent, **configs)
        
        self.title('File lsit')
        self.geometry('300x500')
        
        row = Frame(self)
        lab = Label(row, width=15, text='Metadata list:')
        
        row.pack(side=TOP, fill=X)
        lab.pack(side=LEFT)
        
        for name in filelists:
            checkbox_row = Frame_selectbox(name)
            checkbox_row.pack(side=BOTTOM)
        
    
    def show(self):
        self.destroy()