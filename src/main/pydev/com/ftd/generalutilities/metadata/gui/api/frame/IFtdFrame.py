'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import Frame
from abc import ABCMeta
from _tkinter import TclError

class IFtdFrame(object):
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta #This is a abstract class

    def set_conf(self, **confs):
        
        for child in self.winfo_children():
            
            if isinstance(child, IFtdFrame):
                child.set_conf(**confs)
            elif isinstance(child, Frame):
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