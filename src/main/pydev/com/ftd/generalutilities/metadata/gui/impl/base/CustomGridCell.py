from tkinter import Entry

class CustomGridCell(Entry):
    
    def __init__(self, master=None, row=None, column=None, *args, **kwargs):
        Entry.__init__(self, master, *args, **kwargs)
        self.__row = row
        self.__column = column
        self.__origin_value = None
    
    
    def get_row(self):
        return self.__row
    
    
    def get_column(self):
        return self.__column