'''
Created on Jun 20, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_loaddir import Frame_loaddir
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_maintgene import Frame_maintgene
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
        #load frame
        self.open_loaddir()
        #self.open_maintgene()
        
    
    def on_closing(self):
        if askyesno("Quit", 'Do you want to quit?'):
            self.__main.quit()
    
    
    def get_mainframe(self):
        return self.__main
    
    
    def open_loaddir(self):
        #load frame
        self.__body = Frame_loaddir(self.__main, self.open_maintgene)
        self.__body.pack(fill=X)
        
        
    def open_maintgene(self):
        #destroy the body before rendering it
        try:
            self.__body.destroy()
        except AttributeError:
            pass
        #maint generation frame
        self.__body = Frame_maintgene(self.__main, None)
        self.__body.pack(fill=X)