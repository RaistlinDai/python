'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from tkinter.messagebox import showerror
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_openfile import Button_openfile
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.service.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.UnFormatableFrame import UnFormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.service.File_reader import File_reader

class Frame_load_dir(FormatableFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, nextframe=None, dtos=None, **configs):
        '''
        Constructor
        '''
        #analysis parent viewForm
        FormatableFrame.__init__(self, parent.get_mainframe(), nextframe, dtos, **configs)
                
    
    #overwrite create_widges
    def create_widges(self):
        #frame
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #title
        self.__label01 = Label(self.__frame1, text="Select or Input the project src path:", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        #input
        feet = StringVar()
        self.__dicinput = Entry(self.__frame1, textvariable=feet)
        self.__dicinput.pack(side=LEFT, fill=BOTH, expand=1)
        #button
        self.__dicload = Button_openfile(self.__frame1, self.reset_dicinput, height=1)
        self.__dicload.pack(side=LEFT)
        #focus
        self.__dicinput.focus()
        
        #selected result
        self.__frame2 = FormatableFrame(self)
        self.__frame2.pack(fill=X)
        self.__label02 = Label(self.__frame2, text="Selected entity: ")
        self.__label02.pack(side=LEFT, fill=X)
        
        #selected details
        self.__frame3 = UnFormatableFrame(self)
        self.__frame3.pack(fill=X)
        self.__label03 = Label(self.__frame3, text="View metadata: ")
        self.__label03.pack(side=LEFT, fill=X)
        self.__frame4 = UnFormatableFrame(self)
        self.__frame4.pack(fill=X)
        self.__label04 = Label(self.__frame4, text="Source metadata: ")
        self.__label04.pack(side=LEFT, fill=X)
        
    
    #overwrite create_widges
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Load':{'loadFunc':self.get_dicinput, 'setFunc':self.get_selection},
                   'Next':{'process':self.get_nextframe(), 'before':self.before_next}}
        self.__buttom = Frame_bottom(parent, ['Next','Load'], exFuncs)
        self.__buttom.pack(side=BOTTOM, fill=X, ipady=10)
        
    
    def reset_dicinput(self, dicname):
        self.__dicinput.delete(0, END)
        self.__dicinput.insert(END, dicname)
        
        
    def get_dicinput(self):
        return self.__dicinput.get()
        
    
    def get_selection(self, fileinfo):
        #path constant
        fileconstant = File_constant()
        #update label
        if isinstance(fileinfo, tuple):
            filename = fileinfo[0]
            viewfullpath = fileinfo[1]
        elif isinstance(fileinfo, str):
            filename = fileinfo
            viewfullpath = self.__dicinput.get() + fileconstant.viewmetadata_path + filename
        else:
            return
        
        #verify source metadata
        resource_exist = False
        if filename:
            resourcefullpath = self.__dicinput.get() + fileconstant.resource_metadata_path + filename +fileconstant.resource_metadata_suffix
            resource_exist = File_reader.verify_file(resourcefullpath)
        
        newname = "Selected entity: " + filename
        self.__label02.config(text=newname)
        
        newviewpath = "View metadata: Verified"
        self.__label03.config(text=newviewpath)
        
        if resource_exist:
            newsourcepath = "Source metadata: Verified"
            self.__label04.config(text=newsourcepath)
        else:
            newsourcepath = "Source metadata: Failed"
            self.__label04.config(text=newsourcepath)
            showerror('Error', 'There is no matching resource metadata!')
            return
        
        #set the entity name and full path in dto set
        self.get_dtos().set_entityname(filename)
        self.get_dtos().set_projectpath(self.__dicinput.get())
        self.get_dtos().set_viewfullpath(viewfullpath)
        self.get_dtos().set_resourcefullpath(resourcefullpath)
        
    
    def before_next(self):
        if self.__dicinput.get():
            return True
        else:
            showerror('Error', 'You must select an existing entity!')
            return False