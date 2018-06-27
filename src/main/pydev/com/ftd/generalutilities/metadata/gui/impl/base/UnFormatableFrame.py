'''
Created on Jun 26, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FtdFrame import FtdFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.base.IUnFormatableFrame import IUnFormatableFrame

class UnFormatableFrame(FtdFrame, IUnFormatableFrame):
    '''
    classdocs
    '''

    def __init__(self, parent=None, nextframe=None, **configs):
        '''
        Constructor
        '''
        FtdFrame.__init__(self, parent, nextframe, dtos=None, **configs)
        