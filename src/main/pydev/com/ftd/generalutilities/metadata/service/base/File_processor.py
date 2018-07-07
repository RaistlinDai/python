'''
Created on Jun 21, 2018

@author: ftd
'''
import os
import shutil

class File_processor(object):
    '''
    classdocs
    '''    
    
    @staticmethod
    def verify_dir_existing(path):
        return os.path.exists(path)
    
    
    @staticmethod
    def verify_dir_format(path):
        return os.path.isdir(path)
    
        
    @staticmethod
    def create_folder(directory):
        os.makedirs(directory)
    
    
    @staticmethod
    def create_file(filename, directory=None):
        if directory:
            os.chdir(directory)
        
    
    @staticmethod
    def copy_file(srcfile, dstfile):
        '''
        copy file
        @param srcfile: the source file
        @param dstfile: the new file
        @return: return status
        @return: message if validation failed
        '''
        if not os.path.isfile(srcfile):
            return False, "File not exist!"
        else:
            fpath,fname=os.path.split(dstfile)
            if not os.path.exists(fpath):
                os.makedirs(fpath)
            shutil.copyfile(srcfile, dstfile)
        return True, None
    
    
    @staticmethod
    def update_bean_app_context(filepath):
        # verify if file is existing
        if os.path.exists(filepath):
            #backup file
            filepath_new = filepath + '.bck'
            