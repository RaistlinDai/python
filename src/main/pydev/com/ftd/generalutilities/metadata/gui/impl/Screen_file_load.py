'''
Created on Jun 20, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Frame_body_load import Frame_body_load
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Popup_filelist import Popup_filelist

class Screen_file_load(Frame):
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
        #font
        self.labelfont = ('times', 15, 'bold')
        
        self.grid(column=0, row=0, sticky=(N,W,E,S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        #add children
        self.create_widgets()
        #layout maintain
        self.adjust_children()
        
        
    def create_widgets(self):
        #body
        self.body = Frame_body_load(self)
        self.body.grid(column=0, row=0, sticky=(N))
        #buttom
        self.buttom = Frame_bottom(self, self.data_load)
        self.buttom.grid(column=0, row=2, sticky=(S))
        

    def adjust_children(self):
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
            child.set_conf(font=self.labelfont, bg='black', fg='yellow', relief=RAISED)
    
        
    def data_load(self):
        Popup_filelist(self)
    