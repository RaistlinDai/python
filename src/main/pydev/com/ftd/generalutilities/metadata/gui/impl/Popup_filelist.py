'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *

class Popup_filelist(Toplevel):
    '''
    classdocs
    '''


    def __init__(self, parent=None, **configs):
        '''
        Constructor
        '''
        Toplevel.__init__(self, parent, **configs)
        
        self.title('File lsit')
        self.geometry('300x500')
        
        row = Frame(self)
        lab = Label(row, width=5, text='Metadata list:')
        
        row.pack(side=TOP, fill=X)
        lab.pack(side=TOP)
        
    
    def show(self):
        self.destroy()