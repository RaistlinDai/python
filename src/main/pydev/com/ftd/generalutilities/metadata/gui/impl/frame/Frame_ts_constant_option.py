'''
Created on Jun 27, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Java_processor import Java_processor
from tkinter.messagebox import showwarning, showerror
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.TS_processor import TS_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Xmlfile_processor import Xmlfile_processor

class Frame_ts_constant_option(FormatableFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, dtos=None, trans=None, **configs):
        '''
        Constructor
        '''
        self.__result = True
        
        FormatableFrame.__init__(self, parent.get_mainframe(), dtos, trans, **configs)
        
    
    #overwrite create_widges
    def create_widges(self):
        
        fileconstant = File_constant()
        
        #frame
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #Title
        self.__label01 = Label(self.__frame1, text="TS Constants generator options", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        #---- panel 01 ----------
        canv1 = Canvas(self, height=30, width=550)
        #label
        self.__label01 = Label(canv1, text='TS Constants name :')
        self.__label01.place(height=20, width=130, relx=0.03, rely=0.2)
        #input
        self.__feet = StringVar()
        self.__dicinput = Entry(canv1, textvariable=self.__feet, borderwidth=3, bg='black', foreground='yellow', highlightcolor='red', insertbackground='red')
        self.__dicinput.place(height=20, width=250, relx=0.3, rely=0.2)
        
        if self.get_dtos().get_businessentityname():
            temp_name = self.get_dtos().get_businessentityname() + fileconstant.TS_CONSTANT_SUFFIX + fileconstant.TS_SUFFIX
            self.__feet.set(temp_name)
        else:
            self.__result, self.__error, business_entity_name, self.__classlist = Java_processor.validate_lib_javas(self.get_trans(), self.get_dtos())
            if not self.__result:
                #---- panel 02 ----------
                self.__pack_errorpanel()
                return
            if business_entity_name:
                self.get_dtos().set_businessentityname(business_entity_name)
                temp_name = self.get_dtos().get_businessentityname() + fileconstant.TS_CONSTANT_SUFFIX + fileconstant.TS_SUFFIX
                self.__feet.set(temp_name)
        
        canv1.pack()
    
        #---- panel 02 ----------
        canv2 = Canvas(self, height=100, width=550)
        #label
        label1 = Label(canv2, text='Options:')
        label1.place(height=20, width=60, relx= 0, rely=0)
        #radio box
        self.__vari1 = IntVar()
        self.__rad1 = Radiobutton(canv2, text='Re-write the previous file', variable=self.__vari1, value=1)
        self.__rad1.place(height=20, width=170, relx= 0.1, rely=0.2)
        self.__rad1.select()
        self.__rad2 = Radiobutton(canv2, text='Attach new functions to the file', variable=self.__vari1, value=2)
        self.__rad2.place(height=20, width=210, relx= 0.1, rely=0.45)
        self.__rad2.deselect()
        self.__rad3 = Radiobutton(canv2, text='Save the previous file as backup', variable=self.__vari1, value=3)
        self.__rad3.place(height=20, width=220, relx= 0.1, rely=0.7)
        self.__rad3.deselect()
        canv2.pack()
        
     
    #overwrite create_widges   
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':{'process':self.get_nextframe(), 'before':self.before_next},
                   'Prev':None}
        self.__buttom = Frame_bottom(parent, ['Next','Prev'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10,side=BOTTOM)
        
    
    def before_next(self):
        '''
        overwrite the function in super class
        verify the input directory
        '''
        if not self.__result:
            showwarning('Warning', 'There are error existing, the TSConstant cannot be generated.')
            return
        
        # read the view metadata
        self.__result, self.__message = Xmlfile_processor.read_view_metadata(self.get_dtos())
        if not self.__result:
            showerror('Error', self.__message)
            return False
        
        # create the observable object
        self.__result, self.__message = TS_processor.create_TS_Constant(self.get_dtos(), self.get_trans(), self.__feet.get())
        if not self.__result:
            showerror('Error', self.__message)
            return False
        
        return True
    
    
    def __pack_errorpanel(self):
        '''
        pack the error panel
        '''
        canv2 = Canvas(self, height=50, width=550)
        #label01
        self.__label01 = Label(canv2, text=self.__error, fg='red')
        self.__label01.place(height=40, width=500, relx=0.01, rely=0.05)     
        canv2.pack()