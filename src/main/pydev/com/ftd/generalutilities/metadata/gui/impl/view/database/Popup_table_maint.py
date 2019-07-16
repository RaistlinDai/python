'''
Created on Jul 14, 2019

@author: ftd
'''
from tkinter import *
from numpy.core.tests.test_mem_overlap import xrange
from tkinter.ttk import Combobox
from src.main.pydev.com.ftd.generalutilities.metadata.service.database.api.IDatabase_driver import IDatabase_driver
from tkinter.messagebox import showerror
from cassandra.cluster import NoHostAvailable

class Popup_table_maint(Toplevel):
    '''
    class doc
    '''
    
    def __init__(self, database_driver, parent=None, **configs):
        '''
        Constructor
        '''
        
        Toplevel.__init__(self, parent, **configs)
        # set database driver
        self.__database_driver = database_driver
        
        # set title
        self.title('Table content')
        
        # forbidden resize
        self.resizable(width=False, height=False)
        
        # background layer frame
        self.__background = Frame(self)
        self.__background.config(width=950,height=550)
        self.__background.pack_propagate(0)
        self.__background.pack(fill=X)

        # top frame
        self.__top = Frame(self.__background)
        self.__top.pack(side=TOP, fill=X)
        self.__label = Label(self.__top, width=15, text='Metadata list:')
        self.__label.pack(side=LEFT)
        
        # table grid frame
        self.__table_body = Frame(self.__background)
        self.__table_body.place(width=930, height=480, x=10, y=30)
        
        #---- left top panel ----------
        self.__canv_left_top = Canvas(self.__table_body, bg="white")
        self.__canv_left_top.place(width=170, height=80, x=0, y=0)
        #label
        label1 = Label(self.__canv_left_top, text='Please choose a database')
        label1.place(height=20, width=160, x=5, y=10)
        #combox database name
        self.__comvalue = StringVar() 
        self.__comboxlist = Combobox(self.__canv_left_top,textvariable=self.__comvalue)
        self.__comboxlist.place(height=20, width=160, x=5, y=40)
        self.__comboxlist.bind("<<ComboboxSelected>>",self.load_tables)
        self.__comboxlist["state"] = "readonly"
        
        #---- left bottom panel ----------
        self.__canv_left_bottom = Canvas(self.__table_body, bg="white")
        self.__canv_left_bottom.place(width=170, height=380, x=0, y=90)
        #label
        label2 = Label(self.__canv_left_bottom, text='Please choose a table')
        label2.place(height=20, width=160, x=5, y=10)
        #table list
        self.__listbox = Listbox(self.__canv_left_bottom, width=30)
        self.__scroll = Scrollbar(self.__canv_left_bottom)
        self.__listbox.config(yscrollcommand = self.__scroll.set)
        self.__scroll.place(height=300, width=10, x=155, y=40)
        self.__scroll.config(command = self.__listbox.yview)
        self.__listbox.place(height=300, width=150, x=5, y=40)
        self.__listbox.bind('<Double-Button>', self.load_records)
        
        #---- right panel ----------
        self.__canv_right = Canvas(self.__table_body, bg="yellow")
        self.__canv_right.place(width=730, height=450, x=180, y=0)
        
        # link a scroll bar to the canvas yview
        self.__vsb1 = Scrollbar(self.__table_body, orient="vertical", command=self.__canv_right.yview)
        self.__vsb1.place(width=20, height=450, x=910, y=0)
        self.__canv_right.configure(yscrollcommand=self.__vsb1.set)
        # link a scroll bar to the canvas xview
        self.__vsb2 = Scrollbar(self.__table_body, orient="horizontal", command=self.__canv_right.xview)
        self.__vsb2.place(width=720, height=20, x=180, y=450)
        self.__canv_right.configure(xscrollcommand=self.__vsb2.set)
        
        # render the table grid
        columns = ['batch_job_id', 'batch_job_execution_id', 'batch_job_step_id', 'detail_no', 'batch_job_step_detail_id',
                   'error_severity', 'record_display_text', 'record_link_url', 'record_text', 'result_label_term', 'result_returned', 
                   'submit_result']
        records = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.render_table_grid(columns, records)
        
        # Validation for database driver
        if not isinstance(database_driver, IDatabase_driver):
            showerror('Error', 'Incorrect database parameters, please close!')
            return
        
        result, message = self.load_databases()
        if not result:
            showerror('Error', message)
        
    
    def load_databases(self):
        '''
        load the database name list from database_driver
        '''
        result = True
        message = None
        database_list = []
        
        try:
            database_list = self.__database_driver.get_database_list()
            if not database_list or len(database_list) == 0:
                result = False
                message = 'No valid database!'
        except TypeError as te:
            message = te
            result = False
        except ValueError:
            message = 'Incorrect port number!'
            result = False
        except NoHostAvailable as ne:
            message = ne.args[0]
            result = False
        except Exception as e:
            message = f'Connect failed:{e}'
            result = False
        
        self.__comboxlist["values"] = database_list
        
        return result, message
        
        
    def load_tables(self, event):
        '''
        load the tables
        '''
        if not self.__comboxlist.get():
            return
        
        table_list = self.__database_driver.get_table_list(self.__comboxlist.get())
        
        self.__listbox.delete(0, END)
        for name in table_list:
            self.__listbox.insert(END, name)
            
    
    def load_records(self, event):
        '''
        load records
        '''
        selection = None
        if len(self.__listbox.curselection()) > 0:
            selection = self.__listbox.selection_get()
        if selection:
            columns, column_types, records = self.__database_driver.get_records(self.__comboxlist.get(), selection)
        
        self.render_table_grid(columns, records)
    
    
    def render_table_grid(self, table_columns=None, table_records=None):
        '''
        render the grid
        '''
        # Create a frame to contain the grid cells
        frame_cells = Frame(self.__canv_right, bg="black")
        self.__canv_right.create_window((0, 0), window=frame_cells, anchor='nw')
        
        # add a table
        rows_count = 0
        column_count = 0
        
        # render the grid columns
        if table_columns and len(table_columns) > 0:
            column_count = len(table_columns)
            columns = [Entry() for col_idx in xrange(column_count)]
            for col_idx in range(0, column_count):
                text_var = StringVar()
                text_var.set(table_columns[col_idx])
                columns[col_idx] = Entry(frame_cells, textvariable=text_var, borderwidth=3, bg='black', foreground='blue', relief=RAISED)
                columns[col_idx].grid(row=0, column=col_idx, sticky='news')
                columns[col_idx]["state"] = "readonly"
        
        # render the grid cells
        if table_records and len(table_records) > 0:
            rows_count = len(table_records)
            cells = [[Entry() for j in xrange(column_count)] for i in xrange(rows_count)]
            for i in range(0, rows_count):  # Rows
                for j in range(0, column_count):  # Columns
                    text_var = StringVar()
                    # here we are setting cell text value
                    text_var.set('%s,%s' % (i+1, j+1)) 
                    cells[i][j] = Entry(frame_cells, textvariable=text_var)
                    cells[i][j].grid(row=i+1, column=j, sticky='news')
    
        # render the scroll bar
        if rows_count > 0 or column_count > 0:
            # Update cell frames idle tasks to let tkinter calculate cell sizes
            frame_cells.update_idletasks()
            
            # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
            first5columns_width = 0
            if rows_count > 5:
                first5columns_width = sum([cells[0][j].winfo_width() for j in range(0, 5)])
            else:
                first5columns_width = sum([cells[0][j].winfo_width() for j in range(0, rows_count-1)])
            
            first20rows_height = 0
            if column_count > 20:
                first20rows_height = sum([cells[i][0].winfo_height() for i in range(0, 20)])
            else:
                first20rows_height = sum([cells[i][0].winfo_height() for i in range(0, column_count-1)])
            
            self.__table_body.config(width=first5columns_width + self.__vsb1.winfo_width(), height=first20rows_height + self.__vsb2.winfo_height())
        
        # Set the canvas scrolling region
        self.__canv_right.config(scrollregion=self.__canv_right.bbox("all"))
        
        