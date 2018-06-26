'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_load import Button_load
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_next import Button_next
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_prev import Button_prev

class Frame_bottom(Frame):
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
        
        if 'Load' in buttons:
            self.__loadButton = Button_load(self, loadFunc, text='Load', bg='white', fg='black', relief=RAISED) #set function as input parameter
            self.__loadButton.pack(side=LEFT)
            
        if 'Prev' in buttons:
            self.__prevButton = Button_prev(self, prevFunc, text='Prev', bg='white', fg='black', relief=RAISED) #set function as input parameter
            self.__prevButton.pack(side=LEFT)
        
        if 'Next' in buttons:
            self.__quitButton = Button_next(self, nextFunc, text='Next', bg='white', fg='black', relief=RAISED)
            self.__quitButton.pack(side=RIGHT)
    