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
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.viewmetadata.ViewMetadataDTO import ViewMetadataDTO

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
        #dtos
        viewDTO = ViewMetadataDTO()
        self.__dtos = {'ViewMetaData':viewDTO}
        #load frame
        #self.open_loaddir()
        self.open_maintgene()
        
    
    def on_closing(self):
        if askyesno("Quit", 'Do you want to quit?'):
            self.__main.quit()
    
    
    def get_mainframe(self):
        return self.__main
    
    
    def set_dtos(self, dtos):
        self.__dtos = dtos
        
        
    def get_dtos(self):
        return self.__dtos
    
    
    def open_loaddir(self):
        #load frame
        self.__body = Frame_loaddir(self, self.open_maintgene)
        self.__body.pack(fill=X)
        
        
    def open_maintgene(self):
        #destroy the body before rendering it
        try:
            self.__body.destroy()
        except AttributeError:
            pass
        #maint generation frame
        self.__body = Frame_maintgene(self, None)
        self.__body.pack(fill=X)