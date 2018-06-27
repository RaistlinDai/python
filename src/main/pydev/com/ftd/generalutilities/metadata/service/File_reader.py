'''
Created on Jun 21, 2018

@author: ftd
'''
import os
from src.main.pydev.com.ftd.generalutilities.metadata.service.FileConstant import FileConstant

class File_reader(object):
    '''
    classdocs
    '''
    
    def read_dir(self, dirpath):
        try:
            self.__direxisting = False
            fileconstant = FileConstant(self)
            
            classNames = []
            
            os.chdir(dirpath)
            #Go through the inner files
            for fullname in self.iterbrowse(dirpath):
                if (fullname.startswith(dirpath + fileconstant.viewmetadata_path)):
                    #print fullname 
                    filename=os.path.basename(fullname)
                    #filename
                    classNames.insert(0, filename)
            
            #No files
            if len(classNames) == 0:
                return False, None, 'There is no correct files.'
            
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
                
                
    