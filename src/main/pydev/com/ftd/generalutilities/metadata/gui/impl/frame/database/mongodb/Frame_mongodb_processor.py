'''
Created on Jun 27, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from tkinter.ttk import Combobox

class Frame_mongodb_processor(FormatableFrame):
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
        
        #frame
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #---- panel 01 ----------
        canv1 = Canvas(self, height=300, width=550)
        
        #label
        label1 = Label(canv1, text='Please choose the mongodb database:')
        label1.place(height=20, width=250, relx=0.01, rely=0.06)
        
        #combox name
        self.__comvalue = StringVar() 
        self.__comboxlist = Combobox(canv1,textvariable=self.__comvalue)
        self.__comboxlist.place(height=20, width=100, relx=0.2, rely=0.2)
        self.__comboxlist.bind("<<ComboboxSelected>>",self.load_collections)
        self.__comboxlist["state"] = "readonly"
    
     
    #overwrite create_widges   
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':{'process':self.get_nextframe(), 'before':self.before_next},
                   'Prev':None}
        self.__buttom = Frame_bottom(parent, ['Next','Prev'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10,side=BOTTOM)
        
        
    def load_collections(self, db_name):
        '''
        load the collections(tables) from target database
        '''
        print('OPEN TABLES')