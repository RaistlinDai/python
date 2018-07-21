'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from tkinter.messagebox import showerror
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_select_folder import Button_select_folder
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame

class Frame_load_dir(FormatableFrame):
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
        #title
        self.__label01 = Label(self.__frame1, text="Open the financial webui project", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        #---- panel 01 ----------
        canv1 = Canvas(self, height=100, width=550)
        #label01
        self.__label01 = Label(canv1, text='Select the project dir:')
        self.__label01.place(height=20, width=180, relx=0.01, rely=0.1)
        #input
        self.__input01 = StringVar()
        self.__dicinput = Entry(canv1, textvariable=self.__input01, borderwidth=3, bg='black', foreground='yellow', highlightcolor='red', insertbackground='red')
        self.__dicinput.place(height=20, width=430, relx=0.1, rely=0.4)
        #button
        self.__dicload = Button_select_folder(canv1, self.reset_dicinput, height=1)
        self.__dicload.place(height=20, width=20, relx=0.9, rely=0.4)
        #focus
        self.__dicinput.focus()
        #label02
        self.__label02 = Label(canv1, text='( Example : D:/workspace/erp-fin/dev/erp-financials-webui/ )', fg='blue')
        self.__label02.place(height=20, width=400, relx=0.1, rely=0.7)
        
        canv1.pack()
        
        #---- panel 02 -----------
        canv2 = Canvas(self, height=200, width=550)
        #label01
        self.__label01 = Label(canv2, text='Select the entity metadata:')
        self.__label01.place(height=20, width=180, relx=0.01, rely=0.05)
        #left listbox and scrollbar
        self.__listboxleft = Listbox(canv2, width=30)
        self.__scrollleft = Scrollbar(canv2)
        self.__listboxleft.config(yscrollcommand = self.__scrollleft.set)
        self.__listboxleft.place(height=150, width=220, relx=0.02, rely=0.18)
        self.__scrollleft.place(height=150, width=20, relx=0.42, rely=0.18)
        self.__scrollleft.config(command = self.__listboxleft.yview)
        
        #middle buttons
        self.__button01 = Button(canv2, text='>>', relief=RAISED, cursor='hand2')
        self.__button01.place(height=35, width=25, relx=0.465, rely=0.3)
        
        self.__button02 = Button(canv2, text='<<', relief=RAISED, cursor='hand2')
        self.__button02.place(height=35, width=25, relx=0.465, rely=0.6)
        
        #right listbox and scrollbar
        self.__listboxright = Listbox(canv2, width=30)
        self.__scrollright = Scrollbar(canv2)
        self.__listboxright.config(yscrollcommand = self.__scrollright.set)
        self.__listboxright.place(height=150, width=220, relx=0.52, rely=0.18)
        self.__scrollright.place(height=150, width=20, relx=0.92, rely=0.18)
        self.__scrollright.config(command = self.__listboxright.yview)
        
        
        '''self.__filelists = filelists
        for name in filelists.keys():
            self.__listbox.insert(0, name)
        '''
        
        
        '''
        #selected result
        self.__frame2 = FormatableFrame(self)
        self.__frame2.pack(fill=X)
        self.__label02 = Label(self.__frame2, text="Selected entity: ")
        self.__label02.pack(side=LEFT, fill=X)'''
        
        canv2.pack()
        
    
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
        #update label
        if isinstance(fileinfo, tuple):
            filename = fileinfo[0]
            viewfullpath = fileinfo[1]
        elif isinstance(fileinfo, str):
            filename = fileinfo
        else:
            return
        
        #set the entity name and full path into entity dto
        self.get_dtos().set_entityname(filename)
        newlabel02 = "Selected entity: " + filename
        self.__label02.config(text=newlabel02, fg='blue')
        if viewfullpath:
            self.get_dtos().set_viewfullpath(viewfullpath)
        #set the project path into transaction dto
        self.get_trans().set_projectpath(self.__dicinput.get())
        
    
    def before_next(self):
        '''
        overwrite the function in super class
        verify the input directory
        '''
        if self.get_dtos().get_entityname() and self.get_dtos().get_viewfullpath():
            return True
        else:
            showerror('Error', 'You must select an existing entity!')
            return False