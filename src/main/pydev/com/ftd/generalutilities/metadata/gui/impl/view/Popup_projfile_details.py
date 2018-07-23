'''
Created on Jul 17, 2018

@author: ftd
'''
from tkinter import *
from tkinter.messagebox import showerror
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Xmlfile_processor import Xmlfile_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Java_processor import Java_processor
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_select_file import Button_select_file
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor

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
        self.__label01.place(height=20, width=75, relx=0.01, rely=0.02)
        if fileinfo and fileinfo['filename']:
            self.__text01 = Text(canv1, height=1)
            self.__text01.place(width=450, relx=0.15, rely=0.02)
            self.__text01.insert(INSERT, fileinfo['filename'])
            self.__text01.config(state=DISABLED)
        
        self.__label02 = Label(canv1, text='File type :')
        self.__label02.place(height=20, width=75, relx=0.01, rely=0.3)
        if fileinfo and fileinfo['filetype']:
            self.__text02 = Text(canv1, height=1)
            self.__text02.place(width=200, relx=0.15, rely=0.3)
            self.__text02.insert(INSERT, fileinfo['filetype'])
            self.__text02.config(state=DISABLED)
            
        if not fileinfo['iscorrect'] and fileinfo['filetype'] == 'JAR':
            self.__button01 = Button_select_file(canv1, self.file_button_callback, text='File select :', cursor='hand2')
            self.__button01.place(height=20, width=75, relx=0.01, rely=0.6)
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
        if not self.__fileinfo['iscorrect']:
            fullpath = self.__text03.get(1.0, END).replace('\n','')
            if not fullpath or fullpath == '':
                showerror('Error', 'You must select a %s file!' % self.__fileinfo['filetype'])
                return
            
            result, message = self.verify_files(fullpath)
            if not result:
                showerror('Error', message)
                return
            else:
                self.__fileinfo['filename'] = File_processor.get_file_name(fullpath)
                self.__fileinfo['filepath'] = fullpath
                self.__fileinfo['iscorrect'] = True
        self.destroy()
    
    
    def file_button_callback(self, fullpath):
        '''
        file directory button click event
        @param fullpath: the selected file fullpath
        '''
        if not fullpath or fullpath == '':
            return
        
        self.__text03.config(state=NORMAL)
        self.__text03.delete(1.0, END)
        self.__text03.insert(END, fullpath)
        self.__text03.config(state=DISABLED)
        
    
    def verify_files(self, fullpath):
        '''
        verify the file according to the file type
        @param fullpath: the selected file fullpath in textarea
        @return: result status
        @return: error message if validation failed
        '''
        if self.__fileinfo['filetype'] == 'ViewMetadata':
            return Xmlfile_processor.veriy_view_metadata(fullpath)
        elif self.__fileinfo['filetype'] == 'ResourceMetadata':
            return Xmlfile_processor.veriy_resource_metadata(fullpath)
        elif self.__fileinfo['filetype'] == 'POM':
            return Xmlfile_processor.verify_pom(fullpath)
        elif self.__fileinfo['filetype'] == 'beans':
            return Xmlfile_processor.verify_beans_app_context(fullpath)
        elif self.__fileinfo['filetype'] == 'entityMap':
            return Xmlfile_processor.verify_entity_map(fullpath)
        elif self.__fileinfo['filetype'] == 'JAR':
            return Java_processor.verify_jar_type(fullpath)
        
        return True, None
    
    
    def return_selection(self):
        '''
        this function is an external function, it will return back the selected file fullpath
        @return: the selected file name and fullpath
        '''
        return self.__fileinfo
