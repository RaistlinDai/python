'''
Created on Jun 23, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FtdFrame import FtdFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.base.IFormatableFrame import IFormatableFrame

class FormatableFrame(FtdFrame, IFormatableFrame):
    '''
    classdocs
    '''
    
    
    def __init__(self, parent=None, nextframe=None, dtos=None, trans=None, **configs):
        '''
        Constructor
        '''
        FtdFrame.__init__(self, parent, nextframe, dtos, trans, **configs)