'''
Created on Jul 4, 2018

@author: ftd
'''
import os

class File_generator(object):
    '''
    classdocs
    '''

    @staticmethod
    def update_bean_app_context(filepath):
        # verify if file is existing
        if os.path.exists(filepath):
            #backup file
            filepath_new = filepath + '.bck'
            