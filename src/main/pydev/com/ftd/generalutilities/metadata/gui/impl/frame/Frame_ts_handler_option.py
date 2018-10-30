'''
Created on Jun 27, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.Frame_constant import Frame_constant
from tkinter.messagebox import showerror

class Frame_ts_handler_option(FormatableFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, dtos=None, trans=None, **configs):
        '''
        Constructor
        '''
        self.__result = True
        self.__error = None
        
        FormatableFrame.__init__(self, parent.get_mainframe(), dtos, trans, **configs)
        
    
    #overwrite create_widges
    def create_widges(self):
        
        frame_constant = Frame_constant()
        
        #frame
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #Title
        self.__label01 = Label(self.__frame1, text="TS Handler generator options", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        #---- panel 01 ----------
        canv1 = Canvas(self, height=200, width=550)
        self.__label01 = Label(canv1, text = 'Please select the generated TS:', width=30)
        self.__label01.place(height=30, width=200, relx=0.05, rely=0.02)
        
        # common service
        self.__checkvalues01 = {frame_constant.TS_HANDLER_COMMON:IntVar() }
        for chkv in self.__checkvalues01.keys():
            self.__checkvalues01[chkv].set(1)
            chk1 = Checkbutton(canv1, text = chkv, variable = self.__checkvalues01[chkv], onvalue = 1, offvalue = 0, state=DISABLED)
            chk1.place(height=20, width=150, relx=0.1, rely=0.2)
            # info label
            lbl1 = Label(canv1, text = 'The CommonService is mandatory.', fg='blue')
            lbl1.place(height=20, width=250, relx=0.5, rely=0.2)
        
        # other ts handlers
        self.__checkvalues02 = {frame_constant.TS_HANDLER_MAINT:IntVar(), 
                                frame_constant.TS_HANDLER_VIEWFORM:IntVar(), 
                                frame_constant.TS_HANDLER_GRID:IntVar(),
                                frame_constant.TS_HANDLER_BROWSE:IntVar()}
        idx = 1
        for chkv in self.__checkvalues02.keys():
            chk1 = Checkbutton(canv1, text = chkv, variable = self.__checkvalues02[chkv], onvalue = 1, offvalue = 0)
            chk1.place(height=20, width=100, relx=0.1, rely=0.2 + idx*0.13)
            idx = idx + 1
        
        canv1.pack()
    
     
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
        generating the next frames according to the selections
        '''
        #check box flag
        frame_constant = Frame_constant()
        checkFlag = False
        selections = dict(self.__checkvalues01, **self.__checkvalues02)
        
        for val in selections.values():
            if val.get() == 1:
                checkFlag = True
                break
                
        if checkFlag:
            #merge the selections into process flow
            self.get_trans().update_process_flow_by_gene_selection(selections)
            self.get_trans().print_processflow()
            
            return True
        else:
            showerror('Error', 'You must select at least one generation file!')
            return False