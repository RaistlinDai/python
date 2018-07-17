'''
Created on Jul 17, 2018

@author: ftd
'''
from tkinter import *

class Popup_projfile_details(object):
    '''
    classdocs
    '''


    def __init__(self, fileinfo, parent=None, **configs):
        '''
        Constructor
        '''
        Toplevel.__init__(self, parent, **configs)
        self.title('File list')
        
        #default parameters
        self.__curselection = None
        
        #forbidden resize
        self.resizable(width=False, height=False)
        
        #top label
        self.__top = Frame(self)
        self.__label = Label(self.__top, width=15, text='Metadata list:')
        self.__top.pack(side=TOP, fill=X)
        self.__label.pack(side=LEFT)
        
    
    