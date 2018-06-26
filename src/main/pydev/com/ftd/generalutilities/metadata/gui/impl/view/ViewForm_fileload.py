'''
Created on Jun 20, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_loaddir import Frame_loaddir
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_main import Frame_main
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.view.IViewForm import IViewForm
from tkinter.messagebox import askyesno

class ViewForm_fileload(IViewForm):
    '''
    classdocs
    '''


    def __init__(self, master=None):
        '''
        Constructor
        '''
        #main frame
        self.__main = Frame_main()
        #add children
        self.create_widgets(self.__main)
        #layout maintain
        self.adjust_children(self.__main)
        
        
    def create_widgets(self, master):
        #load frame
        self.__body = Frame_loaddir(master)
        self.__body.pack(fill=X)
        #bottom frame
        exFuncs = {'Load':{'loadFunc':self.__body.get_dicinput, 'setFunc':self.refresh_resultlabel},
                   'Next':self.clean_mainframe}
        self.__buttom = Frame_bottom(master, ['Next','Load'], exFuncs)
        self.__buttom.pack(fill=X)
        

    def adjust_children(self, master):
        for child in master.winfo_children():
            child.set_conf(font=master.labelfont, bg='white', fg='black', relief=RAISED)
        
    
    def on_closing(self):
        if askyesno("Quit", 'Do you want to quit?'):
            self.__main.quit()
    
    
    def refresh_resultlabel(self, filename):
        newname = "Selected metadata: " + filename
        self.__body.update_selection(newname)

    
    def clean_mainframe(self):
        self.__main.destroy()
        
        
    def get_mainframe(self):
        return self.__main
        