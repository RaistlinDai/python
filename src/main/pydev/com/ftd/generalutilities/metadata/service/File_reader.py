'''
Created on Jun 21, 2018

@author: ftd
'''
import os

class File_reader(object):
    '''
    classdocs
    '''


    def __init__(self, **params):
        '''
        Constructor
        '''
        self.__metadata_path = '\\main\\resources\\com\\qad\\erp\\financials\\view'
        self.__javacontroller_path = '\\main\\java\\com\\qad\\erp\\financials'
                
    
    def read_dir(self, dirpath):
        try:
            self.__direxisting = False
            classNames = []
            
            os.chdir(dirpath)
            #Go through the inner files
            for fullname in self.iterbrowse(dirpath):
                if (fullname.startswith(dirpath + self.__metadata_path)):
                    #print fullname 
                    filename=os.path.basename(fullname)
                    #filename
                    print(filename)
                    classNames.insert(0, filename)
                    
                                
            return True, classNames, None
        
        except OSError as e:
            print('expect:', e)
            return False, None, e
        except FileNotFoundError as e:
            print('expect:', e)
            return False, None, e
        finally:
            pass
        
                
    def iterbrowse(self, path):
        for home, dirs, files in os.walk(path):
            for filename in files:
                yield os.path.join(home, filename)
                
                
    