'''
Created on Jun 26, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_checkbox import Frame_checkbox
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from tkinter.messagebox import showerror

class Frame_gene_selection(FormatableFrame):
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
        self.__label01 = Label(self.__frame1, text="Select the generated file", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        #check buttons
        checkbut_frame1 = Frame_checkbox(self)
        checkbut_frame1.pack(fill=X)
        Label(checkbut_frame1, text = 'Xml:', width=10).pack(side=LEFT)
        self.__checkvalues01 = {"EntityMap & BeanAppContext":IntVar()}
        for chkv in self.__checkvalues01.keys():
            chk1 = Checkbutton(checkbut_frame1, text = chkv, variable = self.__checkvalues01[chkv], onvalue = 1, offvalue = 0)
            chk1.pack(side=LEFT)
        
        checkbut_frame2 = Frame_checkbox(self)
        checkbut_frame2.pack(fill=X)
        Label(checkbut_frame2, text = 'Java:', width=10).pack(side=LEFT)
        self.__checkvalues02 = {"DataController":IntVar(), "ServiceImpl":IntVar() }
        for chkv in self.__checkvalues02.keys():
            chk1 = Checkbutton(checkbut_frame2, text = chkv, variable = self.__checkvalues02[chkv], onvalue = 1, offvalue = 0)
            chk1.pack(side=LEFT)
            
        checkbut_frame3 = Frame_checkbox(self)
        checkbut_frame3.pack(fill=X)
        Label(checkbut_frame3, text = 'TsHandler:', width=10).pack(side=LEFT)
        self.__checkvalues03 = {"Constants":IntVar(), "TSHandler":IntVar(), "MockDTO":IntVar(), "ObservableObj":IntVar() }
        for chkv in self.__checkvalues03.keys():
            chk1 = Checkbutton(checkbut_frame3, text = chkv, variable = self.__checkvalues03[chkv], onvalue = 1, offvalue = 0)
            chk1.pack(side=LEFT)
    
    
    #overwrite before_next
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':{'process':self.get_nextframe(), 'before':self.before_next},
                   'Prev':{'process':self.get_prevframe(), 'before':self.before_prev}}
        self.__buttom = Frame_bottom(parent, ['Next','Prev'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10,side=BOTTOM)
        
    
    def before_next(self):
        '''
        overwrite the function in super class
        generating the next frames according to the selections
        '''
        #check box flag
        checkFlag = False
        selections = dict(self.__checkvalues01, **self.__checkvalues02, **self.__checkvalues03)
        
        for val in selections.values():
            if val.get() == 1:
                checkFlag = True
                break
                
        if checkFlag:
            #merge the selections into process flow
            self.get_trans().update_process_flow_by_selection(selections)
            return True
        else:
            showerror('Error', 'You must select at least one generation file!')
            return False
        
    
    