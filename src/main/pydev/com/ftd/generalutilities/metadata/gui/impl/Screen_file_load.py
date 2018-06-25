'''
Created on Jun 20, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Frame_dicload import Frame_dicload
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Popup_filelist import Popup_filelist
from tkinter.messagebox import askyesno

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
        self.master.geometry('500x200')
        #font
        self.labelfont = ('times', 15, 'bold')
        
        #self.grid(column=0, row=0, sticky=(N,W,E,S))
        self.pack()
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        #add children
        self.create_widgets()
        #layout maintain
        self.adjust_children()
        #
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        
    def create_widgets(self):
        #body
        self.body = Frame_dicload(self)
        #self.body.grid(column=0, row=0, sticky=(N))
        self.body.pack(fill=X)
        #bottom
        self.buttom = Frame_bottom(self, self.body.get_dicinput)
        #self.buttom.grid(column=0, row=2, sticky=(S))
        self.buttom.pack(fill=X)
        

    def adjust_children(self):
        for child in self.winfo_children():
            child.set_conf(font=self.labelfont, bg='white', fg='black', relief=RAISED)

        
    def on_closing(self):
        if askyesno("Quit", 'Do you want to quit?'):
            self.quit()
    