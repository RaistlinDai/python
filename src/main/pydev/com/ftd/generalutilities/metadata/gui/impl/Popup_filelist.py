'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *

class Popup_filelist(Toplevel):
    '''
    classdocs
    '''


    def __init__(self, parent=None, conf=None):
        '''
        Constructor
        '''
        Toplevel.__init__(self, parent, conf)
        
        self.title('File lsit')
        self.geometry('300x500')