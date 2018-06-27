'''
Created on Jun 25, 2018

@author: ftd
'''
from tkinter import *
from builtins import AttributeError
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.base.IFormatableFrame import IFormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.base.IUnFormatableFrame import IUnFormatableFrame


class FtdFrame(Frame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, nextframe=None, dtos=None, **configs):
        '''
        Constructor
        '''
        Frame.__init__(self, parent, **configs)
        #next frame
        self.__nextframe = nextframe
        #dtos
        self.__dtos = dtos
        
    
    def get_nextframe(self):
        return self.__nextframe
    
    
    def set_nextframe(self, nextframe):
        self.__nextframe = nextframe
        

    def set_dtos(self, dtos):
        self.__dtos = dtos
        
        
    def get_dtos(self):
        return self.__dtos
    

    def before_next(self):
        pass
    
    
    def after_next(self):
        pass
    
    
    def add_bottom(self, parent):
        pass
    
    
    def adjust_children(self, master):
        for child in master.winfo_children():
            try:
                child.set_conf(font=master.labelfont, bg='white', fg='black', relief=RAISED)
            except AttributeError:
                continue
            
            
    def set_conf(self, **confs):
        
        for child in self.winfo_children():
                    
            if isinstance(child, IFormatableFrame):
                child.set_conf(**confs)
            elif isinstance(child, IUnFormatableFrame):
                continue
            
            #config
            for key in confs.keys():
                try:
                    if key == 'font':
                        child.config(font=confs[key])
                    elif key == 'bg':
                        child.config(bg=confs[key])
                    elif key == 'fg':
                        child.config(fg=confs[key])
                    elif key == 'relief':
                        child.config(relief=confs[key])
                except TclError :
                    next