'''
Created on Jun 20, 2018

@author: ftd
'''
from tkinter import *
from tkinter.messagebox import askyesno, showinfo
from tkinter.messagebox import showerror
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_main import Frame_main
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.view.IViewForm import IViewForm
from src.main.pydev.com.ftd.generalutilities.metadata.dto.base.EntityDTO import EntityDTO
from src.main.pydev.com.ftd.generalutilities.metadata.dto.base.TransactionDTO import TransactionDTO
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.Mainframe_enum import Mainframe_enum

class ViewForm_fileload(IViewForm):
    '''
    classdocs
    '''


    def __init__(self, func, master=None):
        '''
        Constructor
        '''
        #main frame
        if func == 1:
            self.__main = Frame_main('File Generator')
        elif func == 2:
            self.__main = Frame_main('Cassandra connector')
        self.__body = None
        self.__dtos = EntityDTO()
        self.__trans = TransactionDTO()
        
        #inject the functions into transaction dto
        self.__trans.set_next_frame_func(self.open_nextframe)
        self.__trans.set_prev_frame_func(self.open_prevframe)
        
        #mock processing flow
        if func == 1:
            self.__trans.add_next_process(Mainframe_enum.START_UP)
            #self.__trans.add_next_process(Mainframe_enum.SERVICEIMPL_OPTION)
            #self.__trans.add_next_process(Mainframe_enum.SERVICEIMPL_OPTION)
        elif func == 2:
            self.__trans.add_next_process(Mainframe_enum.CASSANDRA_STARTUP)
            #self.__trans.add_next_process(Mainframe_enum.CASSANDRA_CREATE_CONNECTION)
        
        #load frame
        self.open_firstframe()
        
    
    def on_closing(self):
        if askyesno("Quit", 'Do you want to quit?'):
            self.__main.quit()
    
    
    def get_mainframe(self):
        return self.__main
    
    
    def get_bodyframe(self):
        return self.__body
    
    
    def set_bodyframe(self, body):
        self.__body = body


#------------------------- frame workflow ---------------
            
    def open_firstframe(self):
        '''
        open the first frame according to the processing list
        '''
        result, procfunc, message = self.__trans.get_first_process()
        #verify the result
        if not result:
            showerror('Error', message)
        else:
            self.__contruct_newframe__(procfunc)
            
        
    def open_nextframe(self):
        '''
        render the next frame according to the processing list
        '''
        #destroy the body before rendering it
        try:
            self.__body.destroy()
        except AttributeError:
            pass
        
        result, procfunc, message = self.__trans.get_next_process()
        #verify the result
        if not result:
            showerror('Error', message)
            return
        elif not procfunc:
            showinfo('Note', message)
            return
        else:
            self.__contruct_newframe__(procfunc)
                    
    
    def open_prevframe(self):
        '''
        open the previous frame according to the processing list
        '''
        #destroy the body before rendering it
        try:
            self.__body.destroy()
        except AttributeError:
            pass
        
        result, procfunc, message = self.__trans.get_prev_process()
        #verify the result
        if not result:
            showerror('Error', message)
        else:
            self.__contruct_newframe__(procfunc)
        
        
#----------------- private function -----------------

    def __contruct_newframe__(self, procfunc):
        self.__body = procfunc.value[0](self, self.__dtos, self.__trans)
        self.__body.config(width=540,height=400)
        self.__body.pack_propagate(0)
        self.__body.pack(fill=X)
        
        for ii in Mainframe_enum:
            if self.__body.__class__ == ii.value[0]:
                self.__trans.set_currentframe(ii)