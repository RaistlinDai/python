'''
Created on Jun 22, 2018

@author: ftd
'''
from tkinter import Button
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Popup_filelist import Popup_filelist
from src.main.pydev.com.ftd.generalutilities.metadata.service.File_reader import File_reader
from tkinter.messagebox import showerror

class Button_load(Button):
    '''
    classdocs
    '''


    def __init__(self, parent=None, exFuncs=None, **configs):
        '''
        Constructor
        '''
        Button.__init__(self, parent, **configs)
        self.bind('<Button-1>', self.click_event) #bind button click event
        
        if isinstance(exFuncs, dict):
            self.__loadfunc = exFuncs.get('loadFunc')
            self.__setfunc = exFuncs.get('setFunc')
        
    
    '''
    Event
    
    '''
    def click_event(self, event):
        
        print('Message button_load click')
        #call reader service
        reader = File_reader()
        if self.__loadfunc:
            result, metas, err_message = reader.read_dir(self.__loadfunc())
            
            if result:
                popup = Popup_filelist(metas)
                popup.grab_set()
                popup.focus_set()
                popup.wait_window()
                
                if self.__setfunc:
                    self.__setfunc(popup.return_selection())
            else:
                self.__returnvalue = None
                showerror('Error', err_message)
        
        else:
            pass