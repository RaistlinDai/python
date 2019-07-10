'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_load import Button_load
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_nextprev import Button_nextprev
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_selfdesign_bottom import Button_selfdesign_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.api.base.IUnFormatableFrame import IUnFormatableFrame

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
            selfFunc = exFuncs.get('Self')
            nextFunc = exFuncs.get('Next')
            prevFunc = exFuncs.get('Prev')
        
        curFont = dict(family='Courier New, monospace', size=25, color='#7f7f7f')
        
        if 'Load' in buttons:
            self.__loadButton = Button_load(self, loadFunc, font=curFont, text='Load', bg='grey', fg='yellow', relief=RAISED, cursor='hand2')
            self.__loadButton.pack(side=LEFT)
        
        if 'Prev' in buttons:
            self.__prevButton = Button_nextprev(self, prevFunc, 'Prev', font=curFont, text='Prev', bg='grey', fg='yellow', relief=RAISED, cursor='hand2')
            self.__prevButton.pack(side=LEFT)
        
        if 'Next' in buttons:
            self.__quitButton = Button_nextprev(self, nextFunc, 'Next', font=curFont, text='Next', bg='grey', fg='yellow', relief=RAISED, cursor='hand2')
            self.__quitButton.pack(side=RIGHT)

        if 'Self' in buttons:
            self.__selfButton = Button_selfdesign_bottom(self, selfFunc, btnText=selfFunc.get('title'), font=curFont, bg='grey', fg='yellow', relief=RAISED, cursor='hand2')
            self.__selfButton.pack(side=LEFT)
            