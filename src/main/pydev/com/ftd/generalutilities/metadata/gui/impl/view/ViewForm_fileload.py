'''
Created on Jun 20, 2018

@author: ftd
'''
from tkinter import *
from tkinter.messagebox import askyesno
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_load_dir import Frame_load_dir
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_maint_gene import Frame_maint_gene
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_main import Frame_main
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.view.IViewForm import IViewForm
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FileDTOSet import FileDTOSet
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_verify_file import Frame_verify_file

class ViewForm_fileload(IViewForm, FileDTOSet):
    '''
    classdocs
    '''


    def __init__(self, master=None):
        '''
        Constructor
        '''
        #main frame
        self.__main = Frame_main()
        self.__dtos = FileDTOSet()
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
        self.__body = Frame_load_dir(self, self.open_maintgene, self.__dtos)
        self.__body.config(width=540,height=280)
        self.__body.pack_propagate(0)
        self.__body.pack(fill=X)
        
        
    def open_maintgene(self):
        #destroy the body before rendering it
        try:
            self.__body.destroy()
        except AttributeError:
            pass
        #maint generation frame
        self.__body = Frame_maint_gene(self, self.open_verifyfile, self.__dtos)
        self.__body.config(width=540,height=280)
        self.__body.pack_propagate(0)
        self.__body.pack(fill=X)
        
        
    def open_verifyfile(self):
        #destroy the body before rendering it
        try:
            self.__body.destroy()
        except AttributeError:
            pass
        #maint verification frame
        self.__body = Frame_verify_file(self, None, self.__dtos)
        self.__body.config(width=540,height=280)
        self.__body.pack_propagate(0)
        self.__body.pack(fill=X)
        
        
        
        