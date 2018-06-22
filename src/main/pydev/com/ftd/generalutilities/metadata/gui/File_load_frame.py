'''
Created on Jun 20, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.Buttom_frame import Buttom_frame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.Load_body_frame import Load_body_frame

class File_load_frame(Frame):
    '''
    classdocs
    '''


    def __init__(self, master=None):
        '''
        Constructor
        '''
        Frame.__init__(self, master)
        
        #main window
        self.master.title('File loader')
        self.master.geometry('600x200')
        self.grid(column=0, row=0, sticky=(N,W,E,S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        #add children
        self.create_widgets()
        #layout maintain
        self.adjust_children()
        
        
    def create_widgets(self):
        #body
        self.body = Load_body_frame(self)
        self.body.grid(column=0, row=0, sticky=(N))
        #buttom
        self.buttom = Buttom_frame(self, self.body.nameInput.get)
        self.buttom.grid(column=0, row=2, sticky=(S))
        

    def adjust_children(self):
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.body.nameInput.focus()
    
