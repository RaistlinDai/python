'''
Created on Jul 6, 2018

@author: ftd
'''
import os
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_select_folder import Button_select_folder
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Xmlfile_processor import Xmlfile_processor
from tkinter.messagebox import showerror, showinfo
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.User_default_file_processor import User_default_file_processor

class Frame_database_startup(FormatableFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, dtos=None, trans=None, **configs):
        '''
        Constructor
        '''
        FormatableFrame.__init__(self, parent.get_mainframe(), dtos, trans, **configs)
        
    
    #overwrite create_widges
    def create_widges(self):
        #frame
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #Title
        self.__label01 = Label(self.__frame1, text="Database connection", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        #---- panel 01 ----------
        canv1 = Canvas(self, height=150, width=550)
        #label
        label1 = Label(canv1, text='Please select a database pattern:')
        label1.place(height=20, width=200, relx=0.01, rely=0.05)
        #radio box
        self.__vari1 = IntVar()
        self.__rad1 = Radiobutton(canv1, text='Cassandra database', variable=self.__vari1, value=11)
        self.__rad1.place(height=20, width=160, x= 100, rely=0.3)
        self.__rad1.select()
        self.__rad2 = Radiobutton(canv1, text='Mongodb database', variable=self.__vari1, value=12)
        self.__rad2.place(height=20, width=160, x= 100, rely=0.52)
        self.__rad2.deselect()
        canv1.pack()
        
        #---- panel 02 ----------
        canv2 = Canvas(self, height=100, width=550)
        #label
        label2 = Label(canv2, text='Please select a workspace folder:')
        label2.place(height=20, width=200, relx=0.01, rely=0.05)
        #input
        self.__feet = StringVar()
        self.__dicinput = Entry(canv2, textvariable=self.__feet, borderwidth=3, bg='black', foreground='yellow', highlightcolor='red', insertbackground='red')
        self.__dicinput.place(height=20, width=430, relx=0.1, rely=0.4)
        #button
        self.__dicload = Button_select_folder(canv2, self.reset_dicinput, height=1)
        self.__dicload.place(height=20, width=20, relx=0.9, rely=0.4)
        #label
        label3 = Label(canv2, text='(This folder will be used for storing the backup files)', fg='blue')
        label3.place(height=20, width=310, relx=0.1, rely=0.6)
        
        canv2.pack()
        
        #load the user default
        self.load_user_default()
        
    
    #overwrite before_next
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':{'process':self.get_nextframe(), 'cancel':self.remove_subsequent_frame_exclude_current(), 'before':self.before_next}}
        self.__buttom = Frame_bottom(parent, ['Next'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10,side=BOTTOM)
        
    
    def before_next(self):
        '''
        overwrite the function in super class
        verify the input directory
        generating the next frames according to the selections
        '''
        tempdir = None
        #--- verify the input value
        if self.__dicinput.get():
            if not Xmlfile_processor.verify_dir_format(self.__dicinput.get()):
                showerror('Error', 'The directory format is incorrect!')
                return False
            
            if not Xmlfile_processor.verify_dir_existing(self.__dicinput.get()):
                Xmlfile_processor.create_folder(self.__dicinput.get())
                showinfo('Note', 'A new folder has been created in your workspace path.')
                
            #--- set the workspace path into transaction dto
            self.get_trans().set_workspacepath(self.__dicinput.get())
            tempdir = self.__dicinput.get()
        else:
            tempdir = os.path.join(os.path.expanduser('~'), "Desktop") + '\\PyWorkspace'
            #--- desktop temp folder already existing
            self.__feet.set(tempdir)
            if Xmlfile_processor.verify_dir_existing(tempdir):
                showinfo('Note', 'The temp folder(PyWorkspace) on your desktop has been set as the default workspace.')
            else:
                Xmlfile_processor.create_folder(tempdir)
                showinfo('Note', 'A temp folder(PyWorkspace) has been created on your desktop.')
                
            #--- set the workspace path into transaction dto
            self.get_trans().set_workspacepath(tempdir)
        
        #--- update default file
        fileconstant = File_constant()
        userdefault = File_processor.get_home_dir()
        userdefault = userdefault + fileconstant.USER_DEFAULT
        User_default_file_processor.update_default_file(userdefault, 'workspace', tempdir)
        
        #--- set the process flow according to the selection
        self.get_trans().remove_subsequent_process_flows_exclude_current()
        self.get_trans().update_process_flow_by_start_selection(self.__vari1.get())
        
        return True
    
    
    def reset_dicinput(self, dicname):
        '''
        update the workspace directory
        @param dicname: the workspace directory
        '''
        print(dicname)
        if dicname and dicname != "":
            self.__dicinput.delete(0, END)
            self.__dicinput.insert(END, dicname)
            
    
    def load_user_default(self):
        '''
        load the local user default
        '''
        fileconstant = File_constant()
        userdefault = File_processor.get_home_dir()
        userdefault = userdefault + fileconstant.USER_DEFAULT
        
        #create default file if not existing
        if not File_processor.verify_dir_existing(userdefault):
            User_default_file_processor.create_default_file(userdefault)
        #read default file
        default_info = User_default_file_processor.read_default_file(userdefault)
        
        if default_info['workspace'] and default_info['workspace'] != "":
            self.get_trans().set_workspacepath(default_info['workspace'])
            self.__dicinput.delete(0, END)
            self.__dicinput.insert(END, default_info['workspace'])
        
        if default_info['project'] and default_info['project'] != "":
            self.get_trans().set_projectpath(default_info['project'])
        
        