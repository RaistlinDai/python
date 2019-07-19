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
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.CustomNotebook import CustomNotebook
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.CustomGridCell import CustomGridCell

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
        # opened tables
        self.__opened_tables = []
        # current table
        self.__current_table_columns = []
        self.__current_table_records = []
        
        # set title
        self.title('Table content')
        
        # forbidden resize
        self.resizable(width=False, height=False)
        # set close event
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
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
        self.__comboxlist.bind("<<ComboboxSelected>>",self.event_load_tables)
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
        self.__listbox.bind('<Double-Button>', self.event_load_records)
        
        #---- right panel ----------
        self.__note_right = CustomNotebook(self.__table_body)
        self.__note_right.bind('<<NotebookTabClosed>>', self.event_close_tab)
        self.__note_right.bind('<<After_NotebookTabClosed>>', self.event_after_close_tab)
        self.__note_right.place(width=730, height=470, x=180, y=0)
        
        # Validation for database driver
        if not isinstance(database_driver, IDatabase_driver):
            showerror('Error', 'Incorrect database parameters, please close!')
            return
        
        result, message = self.load_databases()
        if not result:
            showerror('Error', message)
    
    
    def on_closing(self):
        '''
        close event
        '''
        self.__database_driver.shutdown_connection()
        self.destroy()
        
    
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
        
        
    def event_load_tables(self, event):
        '''
        load the tables
        '''
        if not self.__comboxlist.get():
            return
        
        table_list = self.__database_driver.get_table_list(self.__comboxlist.get())
        
        self.__listbox.delete(0, END)
        for name in table_list:
            self.__listbox.insert(END, name)
            
    
    def event_load_records(self, event):
        '''
        load records
        '''
        selection = None
        if len(self.__listbox.curselection()) > 0:
            selection = self.__listbox.selection_get()
            
        if selection in self.__opened_tables:
            return
        
        if selection:
            columns, column_types, records = self.__database_driver.get_records(self.__comboxlist.get(), selection)
        
        # record the selected table
        self.__opened_tables.append(selection)
        # render grid
        self.render_table_grid(selection, columns, records)
    
    
    def render_table_grid(self, table_name, table_columns=None, table_records=None):
        '''
        render the grid
        '''
        tab_frame = Frame(self.__note_right, width=730, height=470)
        self.__note_right.add(tab_frame, text=table_name)
        
        table_canv_right = Canvas(tab_frame, bg="WhiteSmoke")
        table_canv_right.place(width=710, height=430, x=0, y=0)
        
        # link a scroll bar to the canvas yview
        self.__vsb1 = Scrollbar(tab_frame, orient="vertical", command=table_canv_right.yview)
        self.__vsb1.place(width=20, height=430, x=710, y=0)
        table_canv_right.configure(yscrollcommand=self.__vsb1.set)
        # link a scroll bar to the canvas xview
        self.__vsb2 = Scrollbar(tab_frame, orient="horizontal", command=table_canv_right.xview)
        self.__vsb2.place(width=710, height=20, x=0, y=430)
        table_canv_right.configure(xscrollcommand=self.__vsb2.set)
        
        # Create a frame to contain the grid cells
        frame_cells = Frame(table_canv_right, bg="black")
        table_canv_right.create_window((0, 0), window=frame_cells, anchor='nw')
        
        # add a table
        rows_count = 0
        column_count = 0
        
        # render the grid columns
        columns = None
        if table_columns and len(table_columns) > 0:
            column_count = len(table_columns)
            columns = [Entry() for col_idx in xrange(column_count)]
            for col_idx in range(0, column_count):
                text_var = StringVar()
                text_var.set(table_columns[col_idx])
                columns[col_idx] = Entry(frame_cells, textvariable=text_var, borderwidth=3, foreground='black', relief=RAISED)
                columns[col_idx].grid(row=0, column=col_idx, sticky='news')
                columns[col_idx]["state"] = "readonly"
        self.__current_table_columns = columns
        
        # render the grid cells
        cells = None
        if table_records and len(table_records) > 0:
            rows_count = len(table_records)
            cells = [[CustomGridCell() for j in xrange(column_count+1)] for i in xrange(rows_count)]
            for i in range(0, rows_count):  # Rows
                for j in range(0, column_count):  # Columns
                    text_var = StringVar()
                    # here we are setting cell text value
                    text_var.set(table_records[i][j]) 
                    cells[i][j] = CustomGridCell(frame_cells, row=i, column=j, textvariable=text_var, foreground='blue')
                    cells[i][j].grid(row=i+1, column=j, sticky='news')
                    cells[i][j].bind('<ButtonPress-1>', self.event_grid_cell_click)
                    cells[i][j].bind('<FocusOut>', self.event_grid_cell_leave)
                    if i%2 == 0:
                        cells[i][j].config(bg='LightCyan')
                        cells[i][j].set_origin_color('LightCyan')
                    else:
                        cells[i][j].config(bg='white')
                        cells[i][j].set_origin_color('white')
                cells[i][column_count] = 'V'  # the last column of grid cell - row status
                        
        self.__current_table_records = cells
    
        # render the scroll bar
        if rows_count > 0 or column_count > 0:
            # Update cell frames idle tasks to let tkinter calculate cell sizes
            frame_cells.update_idletasks()
            
            # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
            first5columns_width = 0
            if column_count > 5:
                first5columns_width = sum([columns[j].winfo_width() for j in range(0, 5)])
            elif column_count > 0:
                first5columns_width = sum([columns[j].winfo_width() for j in range(0, column_count-1)])
            
            first20rows_height = 0
            if rows_count > 20:
                first20rows_height = sum([cells[i][0].winfo_height() for i in range(0, 20)])
            elif rows_count > 0:
                first20rows_height = sum([cells[i][0].winfo_height() for i in range(0, rows_count-1)])
            
            tab_frame.config(width=first5columns_width + self.__vsb1.winfo_width(), height=first20rows_height + self.__vsb2.winfo_height())
        
        # Set the canvas scrolling region
        table_canv_right.config(scrollregion=table_canv_right.bbox("all"))
        
    
    def event_close_tab(self, event):
        '''
        remove the table name from cache when closing the TAB
        '''
        tab = event.widget.get_active_tab_text()
        if not tab:
            return
        if tab in self.__opened_tables:
            self.__opened_tables.remove(tab)
        
    
    def event_after_close_tab(self, event):
        '''
        after close the Tab
        '''
        pass
    
    
    def event_grid_cell_click(self, event):
        '''
        click on the grid cell
        '''
        idx = 0
        for cell in self.__current_table_records[event.widget.get_row()]:
            if idx == len(self.__current_table_columns):
                break
            cell.config(bg='darkblue', foreground='white')
            idx += 1
            
    
    def event_grid_cell_leave(self, event):
        '''
        focus leave from the grid cell
        '''
        idx = 0
        for cell in self.__current_table_records[event.widget.get_row()]:
            if idx == len(self.__current_table_columns):
                break
            cell.config(bg=event.widget.get_origin_color(), foreground='blue')
            idx += 1
    
