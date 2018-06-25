'''
Created on Jun 20, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Frame_dicload import Frame_dicload
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.FtdFrame import FtdFrame
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
        self.master.geometry('600x200')
        #font
        self.labelfont = ('times', 15, 'bold')
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
        #load frame
        self.__body = Frame_dicload(self)
        self.__body.pack(fill=X)
        #select result
        self.__result_frame = FtdFrame(self)
        self.__result_frame.pack(fill=X)
        self.__label02 = Label(self.__result_frame, text="Selected metadata: ")
        self.__label02.pack(side=LEFT)
        #bottom
        exFuncs = {'Load':{'loadFunc':self.__body.get_dicinput, 'setFunc':self.refresh_resultlabel}}
        self.__buttom = Frame_bottom(self, exFuncs)
        self.__buttom.pack(fill=X)
        

    def adjust_children(self):
        for child in self.winfo_children():
            child.set_conf(font=self.labelfont, bg='white', fg='black', relief=RAISED)

        
    def on_closing(self):
        if askyesno("Quit", 'Do you want to quit?'):
            self.quit()
    
    
    def refresh_resultlabel(self, filename):
        newname = "Selected metadata: " + filename
        self.__label02.config(text=newname)