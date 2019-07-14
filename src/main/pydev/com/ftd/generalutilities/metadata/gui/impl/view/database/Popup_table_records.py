'''
Created on Jul 14, 2019

@author: ftd
'''
from tkinter import *
from numpy.core.tests.test_mem_overlap import xrange

class Popup_table_records(Toplevel):
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
        self.__background.config(width=800,height=520)
        self.__background.pack_propagate(0)
        self.__background.pack(fill=X)

        # top frame
        self.__top = Frame(self.__background)
        self.__top.pack(side=TOP, fill=X)
        self.__label = Label(self.__top, width=15, text='Metadata list:')
        self.__label.pack(side=LEFT)
        
        # table grid frame
        self.__table_body = Frame(self.__background)
        self.__table_body.place(width=750, height=480, x=30, y=40)
        
        # add a canvas in body frame
        canv1 = Canvas(self.__table_body, bg="yellow")
        canv1.place(width=720, height=450, x=0, y=0)
        
        # link a scroll bar to the canvas yview
        vsb1 = Scrollbar(self.__table_body, orient="vertical", command=canv1.yview)
        vsb1.place(width=20, height=450, x=720, y=0)
        canv1.configure(yscrollcommand=vsb1.set)
        # link a scroll bar to the canvas xview
        vsb2 = Scrollbar(self.__table_body, orient="horizontal", command=canv1.xview)
        vsb2.place(width=720, height=20, x=0, y=450)
        canv1.configure(xscrollcommand=vsb2.set)
        
        # Create a frame to contain the grid cells
        frame_cells = Frame(canv1, bg="blue")
        canv1.create_window((0, 0), window=frame_cells, anchor='nw')
        
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
        canv1.config(scrollregion=canv1.bbox("all"))