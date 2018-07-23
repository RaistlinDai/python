'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from tkinter.messagebox import showerror
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_select_folder import Button_select_folder
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Xmlfile_processor import Xmlfile_processor

class Frame_load_dir(FormatableFrame):
    '''
    classdocs
    '''

    def __init__(self, parent=None, dtos=None, trans=None, **configs):
        '''
        Constructor
        '''
        #initialize
        self.__filelists = {}       #file list backup
        
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
        self.__dicinput.place(height=20, width=430, relx=0.05, rely=0.4)
        #button
        self.__dirloadbutton = Button_select_folder(canv1, self.__select_folder, height=1)
        self.__dirloadbutton.place(height=20, width=20, relx=0.85, rely=0.4)
        self.__appbutton = Button(canv1, height=1, text='Apply')
        self.__appbutton.bind('<Button-1>', self.__apply_click_event) #bind button click event
        self.__appbutton.place(height=20, width=40, relx=0.89, rely=0.4)
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
        self.__button01.bind('<Button-1>', self.__to_right_click_event) #bind button click event
        self.__button01.place(height=35, width=25, relx=0.465, rely=0.3)
        
        self.__button02 = Button(canv2, text='<<', relief=RAISED, cursor='hand2')
        self.__button02.bind('<Button-1>', self.__to_left_click_event) #bind button click event
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
        exFuncs = {'Next':{'process':self.get_nextframe(), 'before':self.before_next},
                   'Prev':{'process':self.get_prevframe(), 'before':self.before_prev}}
        self.__buttom = Frame_bottom(parent, ['Next','Prev'], exFuncs)
        self.__buttom.pack(side=BOTTOM, fill=X, ipady=10)
        
    
    def __select_folder(self, proj_dir):
        if proj_dir and proj_dir != "":
            self.__dicinput.delete(0, END)
            self.__dicinput.insert(END, proj_dir)
        
        
    def get_dicinput(self):
        return self.__dicinput.get()
        
    
    def __apply_click_event(self, event):
        '''
        get the entities according to the input project path
        '''
        fileconstant = File_constant()
        proj_dir = self.__input01.get()
        #verify the input directory
        if not File_processor.verify_dir_existing(proj_dir):
            showerror('Error', 'Please select a valid directory.')
        if not File_processor.verify_dir_format(proj_dir):
            showerror('Error', 'Please select a valid forlder, not a file.')
            return
        if not File_processor.verify_file(proj_dir + fileconstant.POM_PATH):
            showerror('Error', 'Please select a valid project directory\n(the directory of pom.xml in webui).')
            return
        
        #read the entity metadatas
        result, metas, err_message = Xmlfile_processor.read_proj_dir(proj_dir)
        if result:
            #clear the list box first
            self.__listboxleft.delete(0, END)
            #backup the list
            self.__filelists = metas
            #add items into list box
            for name in metas.keys():
                self.__listboxleft.insert(END, name)
        else:
            showerror('Error', err_message)
    
    
    def __to_right_click_event(self, event):
        '''
        move the selection to the right list box
        '''
        if not self.__listboxleft or self.__listboxleft.size() == 0:
            return
        if self.__listboxright and self.__listboxright.size() > 0:
            showerror('Error', 'Multiple entity is not supported for now!')
            return
        
        select_item = None
        if len(self.__listboxleft.curselection()) > 0:
            selection = self.__listboxleft.selection_get()
            #the dict.items() will convert to tuple
            for tup in self.__filelists.items():
                if tup[0] == selection:
                    select_item = tup
                    break
        
        if select_item:
            #add into right
            self.__listboxright.insert(END, select_item[0])
            select_idx = self.__listboxleft.curselection()
            #remove from left
            self.__listboxleft.delete(select_idx[0])
            
    
    def __to_left_click_event(self, event):
        '''
        move the selection to the left list box
        '''
        if not self.__listboxright or self.__listboxright.size() == 0:
            return
        
        if len(self.__listboxright.curselection()) > 0:
            selection = self.__listboxright.selection_get()
            #the dict.items() will convert to tuple
            idx = 0
            for tup in self.__filelists.items():
                if tup[0] == selection:
                    select_item = tup
                    break
                idx = idx + 1
        
        if select_item:
            #add into left
            self.__listboxleft.insert(idx, select_item[0])
            select_idx = self.__listboxright.curselection()
            #remove from right
            self.__listboxright.delete(select_idx[0])
            
    
    def before_next(self):
        '''
        overwrite the function in super class
        verify the input directory
        '''
        if self.__listboxright.size() > 0:
            #the dict.items() will convert to tuple
            for index in range(self.__listboxright.size()):
                for tup in self.__filelists.items():
                    if tup[0] == self.__listboxright.get(index):
                        #save the entity info
                        self.get_dtos().set_entityname(tup[0])
                        self.get_dtos().set_viewfullpath(tup[1])
            
        if self.get_dtos().get_entityname() and self.get_dtos().get_viewfullpath():
            #save the project path
            self.get_trans().set_projectpath(self.__input01.get())
            return True
        else:
            showerror('Error', 'You must select an existing entity!')
            return False