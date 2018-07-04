'''
Created on Jun 21, 2018

@author: ftd
'''
import os
import xml.dom.minidom
from src.main.pydev.com.ftd.generalutilities.metadata.service.File_constant import File_constant

class File_reader(object):
    '''
    classdocs
    '''
    
    @staticmethod
    def read_dir(dirpath):
        try:
            dir_existing = False
            fileconstant = File_constant()
            #view metadata file list
            viewMetadataNames = {}
            
            #change the work path
            os.chdir(dirpath)
            #go through the inner files
            for fullname in File_reader.iterbrowse(dirpath):
                #get the view metadata files
                if (fullname.startswith(dirpath + fileconstant.view_metadata_path)):
                    #trim the file name
                    filename=os.path.basename(fullname)
                    #remove the suffix
                    filename = filename[:-4]
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
    @staticmethod
    def iterbrowse(path):
        for home, dirs, files in os.walk(path):
            for filename in files:
                #generator
                yield os.path.join(home, filename)
                
    
    @staticmethod
    def read_resourcemetadata(path):
        dom = xml.dom.minidom.parse(path)
        root = dom.documentElement
        print(root.nodeName)
        print(root.nodeName)
        print(root.nodeName)
        print(root.nodeName)
        print(root.nodeName)
        print(root.nodeName)
        print(root.nodeName)
        
    
    @staticmethod
    def verify_file(path):
        return os.path.exists(path)
            
    