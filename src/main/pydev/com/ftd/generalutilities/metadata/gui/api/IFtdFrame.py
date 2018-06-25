'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import Frame

class IFtdFrame(object):
    '''
    classdocs
    '''


    def set_conf(self, **confs):
        
        for child in self.winfo_children():
            
            if isinstance(child, IFtdFrame):
                self.set_conf(child, **confs)
            elif isinstance(child, Frame):
                continue
            
            #config
            for key in confs.keys():
                if key == 'font':
                    child.config(font=confs[key])
                elif key == 'bg':
                    child.config(bg=confs[key])
                elif key == 'fg':
                    child.config(fg=confs[key])
                elif key == 'relief':
                    child.config(relief=confs[key])