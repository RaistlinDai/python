'''
Created on Jun 25, 2018

@author: ftd
'''
from tkinter import *
from builtins import AttributeError
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.frame.IFormatableFrame import IFormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.frame.IUnFormatableFrame import IUnFormatableFrame


class FtdFrame(Frame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, nextframe=None, **configs):
        '''
        Constructor
        '''
        Frame.__init__(self, parent, **configs)
        #next frame
        self.nextframe = nextframe
        
    
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