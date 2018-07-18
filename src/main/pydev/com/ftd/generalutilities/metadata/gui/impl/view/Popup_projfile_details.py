'''
Created on Jul 17, 2018

@author: ftd
'''
from tkinter import *
from tkinter.messagebox import showerror
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Xmlfile_processor import Xmlfile_processor

class Popup_projfile_details(Toplevel):
    '''
    classdocs
    '''


    def __init__(self, fileinfo, parent=None, **configs):
        '''
        Constructor
        '''
        #current fileinfo
        self.__fileinfo = fileinfo
        
        Toplevel.__init__(self, parent, **configs)
        self.title('File Info')
        
        #default parameters
        self.__curselection = None
        
        #forbidden resize
        self.resizable(width=False, height=False)
        
        #body
        canv1 = Canvas(self, height=150, width=550)
        #label
        self.__label01 = Label(canv1, text='File name :')
        self.__label01.place(height=20, width=80, relx=0.01, rely=0.02)
        if fileinfo and fileinfo['filename']:
            self.__text01 = Text(canv1, height=1)
            self.__text01.place(width=450, relx=0.15, rely=0.02)
            self.__text01.insert(INSERT, fileinfo['filename'])
            self.__text01.config(state=DISABLED)
        
        self.__label02 = Label(canv1, text='File type :')
        self.__label02.place(height=20, width=80, relx=0.01, rely=0.3)
        if fileinfo and fileinfo['filetype']:
            self.__text02 = Text(canv1, height=1)
            self.__text02.place(width=200, relx=0.15, rely=0.3)
            self.__text02.insert(INSERT, fileinfo['filetype'])
            self.__text02.config(state=DISABLED)
            
        if not fileinfo['iscorrect']:
            self.__button01 = Button(canv1, text='File select :')
            self.__button01.place(height=20, width=80, relx=0.01, rely=0.6)
        else:
            self.__label03 = Label(canv1, text='File path :')
            self.__label03.place(height=20, width=80, relx=0.01, rely=0.6)
        if fileinfo and fileinfo['filepath']:
            self.__text03 = Text(canv1, height=4)
            self.__text03.place(width=450, relx=0.15, rely=0.6)
            self.__text03.insert(INSERT, fileinfo['filepath'])
            if fileinfo['iscorrect']:
                self.__text03.config(state=DISABLED)
            else:
                self.__text03.config(state=DISABLED, bg='black', fg='yellow')
        
        canv1.pack()
    
        #bottom frame
        self.__bottom = Frame(self)
        self.__bottom.pack(side=BOTTOM, fill=X)
        self.__button = Button(self.__bottom, text='OK', command=self.ok_callback)
        self.__button.config(width=10)
        self.__button.pack(side=RIGHT)
        
    
    def show(self):
        self.destroy()
        
        
    def ok_callback(self):
        '''
        'OK' button click event
        '''
        #if not self.__fileinfo['iscorrect']:
        result, message = self.verify_files()
        if not result:
            showerror('Error', message)
            return
        self.destroy()
    
    
    def verify_files(self):
        '''
        verify the file according to the file type
        '''
        if self.__fileinfo['filetype'] == 'ViewMetadata':
            return Xmlfile_processor.veriy_view_metadata(self.__fileinfo['filepath'])
        elif self.__fileinfo['filetype'] == 'ResourceMetadata':
            return Xmlfile_processor.veriy_resource_metadata(self.__fileinfo['filepath'])
        
        return True, None