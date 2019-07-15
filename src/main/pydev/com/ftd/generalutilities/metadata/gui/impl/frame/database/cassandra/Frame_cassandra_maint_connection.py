'''
Created on Jul 10, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from tkinter.messagebox import showerror, askyesno, showinfo
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Database_connection_file_processor import Database_connection_file_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor
from tkinter.ttk import Combobox
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_selfdesign import Button_selfdesign
from cassandra.cluster import NoHostAvailable
from src.main.pydev.com.ftd.generalutilities.metadata.service.database.src.cassandra.Cassandra_driver import Cassandra_driver
from src.main.pydev.com.ftd.generalutilities.metadata.dto.database.Database_parameters import Database_parameters
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.view.database.Popup_table_maint import Popup_table_maint

class Frame_cassandra_maint_connection(FormatableFrame):
    '''
    classdocs
    '''
    global BUTTON_TEXT_LOAD
    global BUTTON_TEXT_NEW
    global MATAIN_MODE_LOAD
    global MATAIN_MODE_NEW
    BUTTON_TEXT_LOAD = 'Load existing'
    BUTTON_TEXT_NEW = 'New connection'
    MATAIN_MODE_LOAD = 'LOAD'
    MATAIN_MODE_NEW = 'NEW'

    def __init__(self, parent=None, dtos=None, trans=None, **configs):
        '''
        Constructor
        '''
        FormatableFrame.__init__(self, parent.get_mainframe(), dtos, trans, **configs)
        
    
    #overwrite create_widges
    def create_widges(self):
        # initialize the maintain mode
        self.__maintain_mode = None
        self.set_maintain_mode()
        
        #frame
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #Title
        self.__label01 = Label(self.__frame1, text="Cassandra maint connection", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        #---- panel 01 ----------
        canv2 = Canvas(self, height=300, width=550)
        #label
        label1 = Label(canv2, text='Please choose the database connection:')
        label1.place(height=20, width=250, relx=0.01, rely=0.06)
        
        #label
        self.__label01 = Label(canv2, text='Name:')
        self.__label01.place(height=20, width=80, relx=0.05, rely=0.2)
        #combox name
        self.__comvalue = StringVar() 
        self.__comboxlist = Combobox(canv2,textvariable=self.__comvalue) 
        self.__comboxlist.place(height=20, width=100, relx=0.2, rely=0.2)
        self.__comboxlist.bind("<<ComboboxSelected>>",self.load_connection_parameters)
        self.__comboxlist["state"] = "readonly"
        #input name
        self.__feet = StringVar()
        self.__input01 = Entry(canv2, textvariable=self.__feet, borderwidth=3, bg='black', foreground='yellow', highlightcolor='red', insertbackground='red')
        self.__input01.place(height=20, width=100, relx=0.2, rely=0.2)
        
        #button
        button_text = ''
        if self.__maintain_mode == MATAIN_MODE_LOAD:
            self.__input01.place_forget()
            button_text = BUTTON_TEXT_NEW
        else:
            self.__comboxlist.place_forget()
            button_text = BUTTON_TEXT_LOAD
        self.__modebtn = Button_selfdesign(canv2, self.change_maintain_mode, button_text, height=2)
        self.__modebtn.place(height=20, width=100, relx=0.4, rely=0.2)
        
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
        
        # load saved connections
        if self.__maintain_mode == MATAIN_MODE_LOAD:
            self.load_connection_names()
        
    
    #overwrite before_next
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Prev':{'process':self.get_prevframe(), 'before':self.before_prev},
                   'Self':{'process':self.test_connection, 'title':'Test'},
                   'Next':{'process':self.get_nextframe(), 'before':self.before_next}}
        self.__buttom = Frame_bottom(parent, ['Prev','Next','Self'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10,side=BOTTOM)
        
    
    def before_next(self):
        '''
        overwrite the function in super class
        verify the input directory
        generating the next frames according to the selections
        '''
        # verify the connection name
        if not self.__input01.get() and self.__maintain_mode == MATAIN_MODE_NEW:
            showerror('Error', 'Please provide the connection name!')
            return False
        
        # verify the input value
        if not self.__input02.get() or not self.__input03.get() or not self.__input04.get() or not self.__input05.get():
            showerror('Error', 'Please provide the complete info!')
            return False
        
        # setup the connection file path into workspace folder
        fileconstant = File_constant()
        workspacepath = self.get_trans().get_workspacepath()
        cassandra_conection_folder = workspacepath + fileconstant.CASSANDRA_CONFIG_FOLDER
        
        if not File_processor.verify_dir_existing(cassandra_conection_folder):
            File_processor.create_folder(cassandra_conection_folder)
        
        cassandra_conection_file = cassandra_conection_folder + fileconstant.CASSANDRA_CONNECTION_FILE
        
        # combine the connection parameter
        # TODO: this should be implemented as toString() in Cassandra_connection_dto
        if self.__maintain_mode == MATAIN_MODE_NEW:
            connection_name = self.__input01.get()
            connection_param = self.__input01.get() + ':' + 'host=' + self.__input02.get() + ',port=' + self.__input03.get() + ',username=' + self.__input04.get() + ',password=' + self.__input05.get()
        else:
            connection_name = self.__comboxlist.get()
            connection_param = self.__comboxlist.get() + ':' + 'host=' + self.__input02.get() + ',port=' + self.__input03.get() + ',username=' + self.__input04.get() + ',password=' + self.__input05.get()
        
        # store the connection parameters
        if not File_processor.verify_file(cassandra_conection_file):
            Database_connection_file_processor.create_connection_file(cassandra_conection_file, connection_param)
        else:
            if self.__maintain_mode == MATAIN_MODE_NEW and \
                Database_connection_file_processor.verify_connection_name_exist(cassandra_conection_file, self.__input01.get()):
                
                if not askyesno('Warning', 'The connection name is existing, do you confirm to overwrite?'):
                    return False
            Database_connection_file_processor.update_connection_file(cassandra_conection_file, connection_name, connection_param)
        
        return True
    
    
    def get_nextframe(self):
        '''
        overwrite the super class FtdFrame, set the next frame as database maint popup
        '''
        func = self.open_popup_table_maint
        return func
    
    
    def set_maintain_mode(self):
        '''
        verify the initial maintain mode (create or load)
        '''
        self.__maintain_mode = MATAIN_MODE_LOAD
        
        # setup the connection file path into workspace folder
        fileconstant = File_constant()
        workspacepath = self.get_trans().get_workspacepath()
        cassandra_conection_folder = workspacepath + fileconstant.CASSANDRA_CONFIG_FOLDER
        
        if not File_processor.verify_dir_existing(cassandra_conection_folder):
            self.__maintain_mode = MATAIN_MODE_NEW
            return
        
        cassandra_conection_file = cassandra_conection_folder + fileconstant.CASSANDRA_CONNECTION_FILE
        
        # verify the connection file
        if not File_processor.verify_file(cassandra_conection_file):
            self.__maintain_mode = MATAIN_MODE_NEW
            return
        # load connection names
        connection_names = Database_connection_file_processor.read_connection_names(cassandra_conection_file)
        # set tuple to combox list
        templist = tuple(connection_names)
        if len(templist) == 0:
            self.__maintain_mode = MATAIN_MODE_NEW
            return
    
    
    def change_maintain_mode(self):
        '''
        change the maintain mode
        '''
        # change to NEW
        if self.__maintain_mode == MATAIN_MODE_LOAD:
            self.__maintain_mode = MATAIN_MODE_NEW
            self.__comboxlist.place_forget()
            self.__input01.place(height=20, width=100, relx=0.2, rely=0.2)
            self.__modebtn.config(text=BUTTON_TEXT_LOAD)
            self.__input02.delete(0, END)
            self.__input03.delete(0, END)
            self.__input04.delete(0, END)
            self.__input05.delete(0, END)
        # change to LOAD
        else:
            # load connections
            if self.load_connection_names() > 0:
                self.__maintain_mode = MATAIN_MODE_LOAD
                self.__input01.place_forget()
                self.__comboxlist.place(height=20, width=100, relx=0.2, rely=0.2)
                self.__modebtn.config(text=BUTTON_TEXT_NEW)
    
    
    def load_connection_names(self):
        '''
        load all connection names from workspace
        @return: count of connections
        '''
        # setup the connection file path into workspace folder
        fileconstant = File_constant()
        workspacepath = self.get_trans().get_workspacepath()
        cassandra_conection_folder = workspacepath + fileconstant.CASSANDRA_CONFIG_FOLDER
        
        if not File_processor.verify_dir_existing(cassandra_conection_folder):
            File_processor.create_folder(cassandra_conection_folder)
        
        cassandra_conection_file = cassandra_conection_folder + fileconstant.CASSANDRA_CONNECTION_FILE
        
        # verify connection file existing
        if not File_processor.verify_file(cassandra_conection_file):
            showerror('Error', 'Cassandra connection file does not exist!')
            return 0
        
        # load connection names
        connection_names = Database_connection_file_processor.read_connection_names(cassandra_conection_file)
        # set tuple to combox list
        self.__comboxlist["values"]=tuple(connection_names)
        if len(self.__comboxlist["values"]) == 0:
            showerror('Error', 'No valid connection, please add one first!')
            return 0
        
        # default the first one
        self.__comboxlist.current(0)
        
        # load connection parameters
        connection_params = Database_connection_file_processor.read_connection_params(cassandra_conection_file, self.__comboxlist.get())
        # set parameters
        self.__input02.delete(0, END)
        self.__input02.insert(END, connection_params['host'])
        self.__input03.delete(0, END)
        self.__input03.insert(END, connection_params['port'])
        self.__input04.delete(0, END)
        self.__input04.insert(END, connection_params['username'])
        self.__input05.delete(0, END)
        self.__input05.insert(END, connection_params['password'])
        
        return len(self.__comboxlist["values"])
    
    
    def load_connection_parameters(self, event):
        '''
        load connection parameters from workspace
        '''
        # combine the workspace path
        fileconstant = File_constant()
        workspacepath = self.get_trans().get_workspacepath()
        cassandra_conection_file = workspacepath + fileconstant.CASSANDRA_CONFIG_FOLDER + fileconstant.CASSANDRA_CONNECTION_FILE
        
        # verify connection file existing
        if not File_processor.verify_file(cassandra_conection_file):
            showerror('Error', 'Cassandra connection file does not exist!')
            return
        
        # load connection parameters
        connection_params = Database_connection_file_processor.read_connection_params(cassandra_conection_file, self.__comboxlist.get())
        # set parameters
        self.__input02.delete(0, END)
        self.__input02.insert(END, connection_params['host'])
        self.__input03.delete(0, END)
        self.__input03.insert(END, connection_params['port'])
        self.__input04.delete(0, END)
        self.__input04.insert(END, connection_params['username'])
        self.__input05.delete(0, END)
        self.__input05.insert(END, connection_params['password'])
        
    
    def test_connection(self, is_show_success=True):
        '''
        test the connection
        '''
        cassandra_connection_result = False
        
        #--- verify the input value
        if not self.__input02.get() or not self.__input03.get() or not self.__input04.get() or not self.__input05.get():
            showerror('Error', 'Please provide the complete info!')
            return
        
        connectionParams = Database_parameters()
        connectionParams.set_contact_points(self.__input02.get())
        connectionParams.set_port(self.__input03.get())
        connectionParams.set_username(self.__input04.get())
        connectionParams.set_password(self.__input05.get())
        
        try:
            cassandra_connection = Cassandra_driver(connectionParams)
            cassandra_connection_result = cassandra_connection.test_connection()
        except TypeError as te:
            showerror('Error', te)
        except ValueError:
            message = 'Incorrect port number!'
            showerror('Error', message)
        except NoHostAvailable as ne:
            message = ne.args[0]
            showerror('Error', message)
        except Exception as e:
            message = f'Connect failed:{e}'
            showerror('Error', message)
            
        if cassandra_connection_result and is_show_success:
            message = 'Connect successfully'
            showinfo('Info', message)
            
        return cassandra_connection_result
    
    
    def open_popup_table_maint(self):
        '''
        open the table maint popup
        '''
        connectionParams = Database_parameters()
        connectionParams.set_contact_points(self.__input02.get())
        connectionParams.set_port(self.__input03.get())
        connectionParams.set_username(self.__input04.get())
        connectionParams.set_password(self.__input05.get())
        cassandra_connection = Cassandra_driver(connectionParams)
        
        popup = Popup_table_maint(cassandra_connection)
        popup.grab_set()
        popup.focus_set()
        popup.wait_window()
        