'''
Created on Jul 14, 2019

@author: ftd
'''
from tkinter import *
from numpy.core.tests.test_mem_overlap import xrange
from tkinter.ttk import Combobox

class Popup_table_maint(Toplevel):
    '''
    class doc
    '''
    
    def __init__(self, filelists, parent=None, **configs):
        '''
        Constructor
        '''

        Toplevel.__init__(self, parent, **configs)
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
        canv_left_top = Canvas(self.__table_body, bg="red")
        canv_left_top.place(width=170, height=80, x=0, y=0)
        #label
        label1 = Label(canv_left_top, text='Please choose a database')
        label1.place(height=20, width=160, x=5, y=10)
        #combox database name
        self.__comvalue = StringVar() 
        self.__comboxlist = Combobox(canv_left_top,textvariable=self.__comvalue)
        self.__comboxlist.place(height=20, width=160, x=5, y=40)
        self.__comboxlist.bind("<<ComboboxSelected>>",self.load_collections)
        self.__comboxlist["state"] = "readonly"
        
        #---- left bottom panel ----------
        canv_left_bottom = Canvas(self.__table_body, bg="blue")
        canv_left_bottom.place(width=170, height=380, x=0, y=90)
        #label
        label2 = Label(canv_left_bottom, text='Please choose a table')
        label2.place(height=20, width=160, x=5, y=10)
        #table list
        self.__listbox = Listbox(canv_left_bottom, width=30)
        self.__scroll = Scrollbar(canv_left_bottom)
        self.__listbox.config(yscrollcommand = self.__scroll.set)
        self.__scroll.place(height=300, width=10, x=155, y=40)
        self.__scroll.config(command = self.__listbox.yview)
        self.__listbox.place(height=300, width=150, x=5, y=40)
        for name in ['a','b','c','d','e','f','g','h','i','j','k','l']:
            self.__listbox.insert(0, name)
        
        #---- right panel ----------
        canv_right = Canvas(self.__table_body, bg="yellow")
        canv_right.place(width=730, height=450, x=180, y=0)
        
        # link a scroll bar to the canvas yview
        vsb1 = Scrollbar(self.__table_body, orient="vertical", command=canv_right.yview)
        vsb1.place(width=20, height=450, x=910, y=0)
        canv_right.configure(yscrollcommand=vsb1.set)
        # link a scroll bar to the canvas xview
        vsb2 = Scrollbar(self.__table_body, orient="horizontal", command=canv_right.xview)
        vsb2.place(width=720, height=20, x=180, y=450)
        canv_right.configure(xscrollcommand=vsb2.set)
        
        # Create a frame to contain the grid cells
        frame_cells = Frame(canv_right, bg="black")
        canv_right.create_window((0, 0), window=frame_cells, anchor='nw')
        
        # add a table
        rows = 30
        columns = 15
        cells = [[Entry() for j in xrange(columns)] for i in xrange(rows)]
        for i in range(0, rows):  # Rows
            for j in range(0, columns):  # Columns
                text_var = StringVar()
                # here we are setting cell text value
                text_var.set('%s,%s' % (i+1, j+1)) 
                cells[i][j] = Entry(frame_cells, textvariable=text_var)
                cells[i][j].grid(row=i, column=j, sticky='news')

        # Update cell frames idle tasks to let tkinter calculate cell sizes
        frame_cells.update_idletasks()
        
        # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
        first5columns_width = sum([cells[0][j].winfo_width() for j in range(0, 5)])
        first20rows_height = sum([cells[i][0].winfo_height() for i in range(0, 20)])
        self.__table_body.config(width=first5columns_width + vsb1.winfo_width(), height=first20rows_height + vsb2.winfo_height())

        # Set the canvas scrolling region
        canv_right.config(scrollregion=canv_right.bbox("all"))
        
        
    def load_collections(self):
        '''
        load the collections (tables)
        '''
        pass