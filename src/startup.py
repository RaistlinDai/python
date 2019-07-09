'''
Created on Jun 26, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.view.ViewForm_fileload import ViewForm_fileload

'''
    function 1: File generator for QRA
    function 2: Cassandra database connection
'''
if __name__ == '__main__': 
    ViewForm_fileload(2).get_mainframe().mainloop()