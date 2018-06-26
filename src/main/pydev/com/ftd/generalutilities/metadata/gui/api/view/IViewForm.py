'''
Created on Jun 26, 2018

@author: ftd
'''
from abc import ABCMeta, abstractmethod


class IViewForm(object):
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta #This is a abstract class

    @abstractmethod    
    def clean_frame(self):
        pass