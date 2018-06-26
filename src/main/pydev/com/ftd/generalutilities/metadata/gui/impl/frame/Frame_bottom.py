'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_load import Button_load
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_next import Button_next
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_prev import Button_prev
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.frame.IUnFormatableFrame import IUnFormatableFrame

class Frame_bottom(Frame, IUnFormatableFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, buttons=[], exFuncs={}, **configs):
        '''
        Constructor
        '''
        Frame.__init__(self, parent, **configs)
        #button
        if isinstance(exFuncs, dict):
            loadFunc = exFuncs.get('Load')
            nextFunc = exFuncs.get('Next')
            prevFunc = exFuncs.get('Prev')
        
        curFont = dict(family='Courier New, monospace', size=25, color='#7f7f7f')
        
        if 'Load' in buttons:
            self.__loadButton = Button_load(self, loadFunc, font=curFont, text='Load', bg='grey', fg='yellow', relief=RAISED, cursor='hand2')
            self.__loadButton.pack(side=LEFT)
            
        if 'Prev' in buttons:
            self.__prevButton = Button_prev(self, prevFunc, font=curFont, text='Prev', bg='grey', fg='yellow', relief=RAISED, cursor='hand2')
            self.__prevButton.pack(side=LEFT)
        
        if 'Next' in buttons:
            self.__quitButton = Button_next(self, nextFunc, font=curFont, text='Next', bg='grey', fg='yellow', relief=RAISED, cursor='hand2')
            self.__quitButton.pack(side=RIGHT)
