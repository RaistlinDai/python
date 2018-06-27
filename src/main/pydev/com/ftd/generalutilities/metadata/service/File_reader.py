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
            #view metadata file list
            viewMetadataNames = {}
            
            #change the work path
            os.chdir(dirpath)
            #go through the inner files
            for fullname in self.iterbrowse(dirpath):
                #get the view metadata files
                if (fullname.startswith(dirpath + fileconstant.viewmetadata_path)):
                    #trim the file name
                    filename=os.path.basename(fullname)
                    #insert into file list
                    viewMetadataNames[filename] = fullname
            
            #no files
            if len(viewMetadataNames) == 0:
                return False, None, 'There is no correct view metadata.'
            
            return True, viewMetadataNames, None
        
        except OSError as e:
            print('expect:', e)
            return False, None, e
        except FileNotFoundError as e:
            print('expect:', e)
            return False, None, e
        finally:
            pass
        
    
    #get the inner files (full path)
    def iterbrowse(self, path):
        for home, dirs, files in os.walk(path):
            for filename in files:
                yield os.path.join(home, filename)
                
                
    