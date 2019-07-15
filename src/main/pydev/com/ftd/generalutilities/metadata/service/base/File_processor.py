'''
Created on Jun 21, 2018

@author: ftd
'''
import os
import shutil
from pathlib import Path
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant

class File_processor(object):
    '''
    classdocs
    '''    
    
    @staticmethod
    def get_home_dir():
        return str(Path.home())
    
    
    @staticmethod
    def verify_dir_existing(path):
        return os.path.exists(path)
    
    
    @staticmethod
    def verify_file(file_path):
        return os.path.isfile(file_path)
        
    
    @staticmethod
    def verify_dir_format(path):
        return os.path.isdir(path)
    
        
    @staticmethod
    def create_folder(directory):
        os.makedirs(directory)
        
        
    @staticmethod
    def create_file(srcfile):
        '''
        create file
        @param srcfile: the target file
        '''
        Path(srcfile).touch()
        srcfile.close()
    
    
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
    def remove_file(srcfile):
        '''
        remove file
        @param srcfile: the target file
        @return: return status
        @return: message if validation failed
        '''
        if not os.path.isfile(srcfile):
            return False, "File not exist!"
        else:
            os.remove(srcfile)
        return True, None
        
    
    @staticmethod
    def remove_folder(dir_path):
        '''
        remove folder
        @param srcfile: the target folder
        @return: return status
        @return: message if validation failed
        '''
        try:
            shutil.rmtree(dir_path)
        except Exception as e:
            return False, e.value
        return True, None
        
            
    @staticmethod
    def dir_iterbrowse(dir_path):
        '''
        this is a generator, to retrieve all of the inter files (include the files in the sub folder)
        @param dir_path: the target directory
        '''
        for home, dirs, files in os.walk(dir_path):
            for filename in files:
                #generator
                yield os.path.join(home, filename)
        
    @staticmethod
    def get_user_home():
        '''
        get the user home directory
        @return: user home directory
        '''
        return os.path.expanduser('~')
    
    
    @staticmethod
    def get_file_type(dir_path):
        '''
        get the file type
        @param dir_path: file directory
        @return: return file type
        '''
        fileconstant = File_constant()
        
        #open file as bytes
        bytefile = open(dir_path, 'rb')
        ftype = 'unknown'
        #read the file header
        bins = bytefile.read(20)
        #close file
        bytefile.close()
        #convert bytes to 16 bit
        bins = File_processor.__bytes2hex(bins)
        #keys comparing
        for hcode in fileconstant.FILE_TYPE.keys():
            lens = len(hcode) #length of key
            if bins[0:lens] == hcode:
                ftype = fileconstant.FILE_TYPE[hcode]
                break
        
        return ftype
    
    
    @staticmethod
    def __bytes2hex(filebytes):
        '''
        convert the bytes to 16 bit
        @param filebytes: the bytes list
        @return: the 16 bit list
        '''
        num = len(filebytes)
        hexstr = u""
        for i in range(num):
            t = u"%x" % filebytes[i]
            if len(t) % 2:
                hexstr += u"0"
            hexstr += t
        return hexstr.upper()
    
    
    @staticmethod
    def get_file_name(filepath):
        '''
        get the file name according to the file's full path
        @param filepath: the file full path
        @return: file name
        '''
        if not File_processor.verify_file(filepath):
            return None
        else:
            return os.path.basename(filepath)
        
    