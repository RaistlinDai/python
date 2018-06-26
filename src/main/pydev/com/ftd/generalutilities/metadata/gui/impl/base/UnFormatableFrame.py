'''
Created on Jun 26, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.FtdFrame import FtdFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.frame.IUnFormatableFrame import IUnFormatableFrame

class UnFormatableFrame(FtdFrame):
    '''
    classdocs
    '''

    def __init__(self, parent=None, nextframe=None, **configs):
        '''
        Constructor
        '''
        FtdFrame.__init__(self, parent, nextframe)
        