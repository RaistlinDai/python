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


    def __init__(self, parent=None, dtos=None, trans=None, **configs):
        '''
        Constructor
        '''
        Frame.__init__(self, parent, **configs)
        #dtos
        self.__dtos = dtos
        #trans
        self.__trans = trans
        #create children
        self.create_widges()
        #add buttom
        self.add_bottom(self)
        #format
        self.__adjust_children__(parent)
        
    
    def create_widges(self):
        pass
    
    
    def get_nextframe(self):
        func = self.__trans.get_next_frame_func()
        return func
    
    
    def get_prevframe(self):
        func = self.__trans.get_prev_frame_func()
        return func
        
        
    def remove_subsequent_frame_exclude_current(self):
        func = self.__trans.remove_subsequent_process_flows_exclude_current
        return func
    
    
    def remove_subsequent_frame_include_current(self):
        func = self.__trans.remove_subsequent_process_flows_include_current
        return func
    

    def set_dtos(self, dtos):
        self.__dtos = dtos
        
        
    def get_dtos(self):
        return self.__dtos
    
    
    def set_trans(self, trans):
        self.__trans = trans
        
        
    def get_trans(self):
        return self.__trans
    

    def before_next(self):
        return True
    
    
    def after_next(self):
        return True
    
    
    def before_prev(self):
        return True
    
    
    def after_prev(self):
        return True
    
    
    def add_bottom(self, parent):
        pass
    
    
#------------------ private function -------------

    def __adjust_children__(self, master):
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