'''
Created on Jul 10, 2018

@author: ftd
'''
import os
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_selfdesign import Button_selfdesign
from src.main.pydev.com.ftd.generalutilities.metadata.service.database.cassandra.Cassandra_service_impl import Cassandra_service_impl
from tkinter.messagebox import showerror, showinfo
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Cassandra_connection_file_processor import Cassandra_connection_file_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor

class Frame_cassandra_create_connection(FormatableFrame):
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
        self.__label01 = Label(self.__frame1, text="Cassandra create connection", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        #---- panel 01 ----------
        canv2 = Canvas(self, height=300, width=550)
        #label
        label1 = Label(canv2, text='Please input the database parameters:')
        label1.place(height=20, width=250, relx=0.01, rely=0.06)
        
        #label
        self.__label01 = Label(canv2, text='Name:')
        self.__label01.place(height=20, width=80, relx=0.05, rely=0.2)
        #input1
        self.__feet = StringVar()
        self.__input01 = Entry(canv2, textvariable=self.__feet, borderwidth=3, bg='black', foreground='yellow', highlightcolor='red', insertbackground='red')
        self.__input01.place(height=20, width=100, relx=0.2, rely=0.2)
        #button
        self.__dicload = Button_selfdesign(canv2, self.auto_config, 'Auto Config', height=1)
        self.__dicload.place(height=20, width=100, relx=0.4, rely=0.2)
        
        #label
        self.__label02 = Label(canv2, text='Host:')
        self.__label02.place(height=20, width=80, relx=0.05, rely=0.4)
        #input
        self.__feet = StringVar()
        self.__input02 = Entry(canv2, textvariable=self.__feet, borderwidth=3, bg='black', foreground='yellow', highlightcolor='red', insertbackground='red')
        self.__input02.place(height=20, width=100, relx=0.2, rely=0.4)
        
        #label
        self.__label03 = Label(canv2, text='Port:')
        self.__label03.place(height=20, width=80, relx=0.5, rely=0.4)
        #input
        self.__feet = StringVar()
        self.__input03 = Entry(canv2, textvariable=self.__feet, borderwidth=3, bg='black', foreground='yellow', highlightcolor='red', insertbackground='red')
        self.__input03.place(height=20, width=100, relx=0.65, rely=0.4)
        #label
        label2 = Label(canv2, text='(yab config | grep cassandra.default.node.main.native_transport_port)', fg='blue')
        label2.place(height=20, width=410, relx=0.1, rely=0.47)
        
        #label
        self.__label04 = Label(canv2, text='User:')
        self.__label04.place(height=20, width=80, relx=0.05, rely=0.6)
        #input
        self.__feet = StringVar()
        self.__input04 = Entry(canv2, textvariable=self.__feet, borderwidth=3, bg='black', foreground='yellow', highlightcolor='red', insertbackground='red')
        self.__input04.place(height=20, width=100, relx=0.2, rely=0.6)
        
        #label
        self.__label05 = Label(canv2, text='Password:')
        self.__label05.place(height=20, width=80, relx=0.5, rely=0.6)
        #input
        self.__feet = StringVar()
        self.__input05 = Entry(canv2, textvariable=self.__feet, borderwidth=3, bg='black', foreground='yellow', highlightcolor='red', insertbackground='red')
        self.__input05.place(height=20, width=100, relx=0.65, rely=0.6)
        #label
        label3 = Label(canv2, text='(the default user and password for cassandra both are "qad")', fg='blue')
        label3.place(height=20, width=400, relx=0.1, rely=0.67)
        
        canv2.pack()
        
    
    #overwrite before_next
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Self':{'process':self.test_connection, 'title':'Test'},
                   'Next':{'process':self.get_nextframe(), 'before':self.before_next}}
        self.__buttom = Frame_bottom(parent, ['Next','Self'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10,side=BOTTOM)
        
    
    def before_next(self):
        '''
        overwrite the function in super class
        verify the input directory
        generating the next frames according to the selections
        '''
        #--- verify the input value
        if not self.__input01.get() or not self.__input02.get() or not self.__input03.get() or not self.__input04.get() or not self.__input05.get():
            showerror('Error', 'Please provide the complete info!')
            return False
        
        # validate connection
        
        
        # setup the connection file path into workspace folder
        fileconstant = File_constant()
        workspacepath = self.get_trans().get_workspacepath()
        cassandra_conection_folder = workspacepath + fileconstant.CASSANDRA_CONFIG_FOLDER
        
        if not File_processor.verify_dir_existing(cassandra_conection_folder):
            File_processor.create_folder(cassandra_conection_folder)
        
        cassandra_conection_file = cassandra_conection_folder + fileconstant.CASSANDRA_CONNECTION_FILE
        
        print(cassandra_conection_file)
        
        # combine the connection parameter
        # TODO: this should be implemented as toString() in Cassandra_connection_dto
        connection_param = 'host=' + self.__input02.get() + ',port=' + self.__input03.get() + ',username=' + self.__input04.get() + ',password=' + self.__input05.get()
        
        # store the connection parameters
        if not File_processor.verify_file(cassandra_conection_file):
            Cassandra_connection_file_processor.create_connection_file(cassandra_conection_file, self.__input01.get() + ':' + connection_param)
        else:
            Cassandra_connection_file_processor.update_default_file(cassandra_conection_file, self.__input01.get(), connection_param)
        
        return True
    
    
    def auto_config(self):
        '''
        automatically read yab config
        '''
        showinfo('Info', 'Not available yet ...')
        
    
    def test_connection(self):
        '''
        test the connection
        '''
        print('TEST CONNECTION')
        Cassandra_service_impl()
        