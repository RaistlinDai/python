'''
Created on Jul 5, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.Mainframe_enum import Mainframe_enum

class TransactionDTO(object):
    '''
    classdocs
    '''


    def __init__(self, current_frame=None, process_flow=None, proj_path=None, next_frame_func=None, prev_frame_func=None):
        '''
        Constructor
        '''
        self.__dto = {'CurrentFrame':current_frame,
                      'ProcessFlow':process_flow,
                      'NextFrameFunc':next_frame_func,
                      'PrevFrameFunc':prev_frame_func,
                      'ProjectPath':proj_path
                      }
        
        
    def set_dtos(self, dtos):
        self.__dto = dtos
        
        
    def get_dtos(self):
        return self.__dto
    
    
    def set_currentframe(self, currentframe):
        if self.__dto:
            self.__dto['CurrentFrame'] = currentframe
            
            
    def get_currentframe(self):
        if self.__dto:
            return self.__dto['CurrentFrame']
        else:
            return None
        
    
    def set_processflow(self, processflow):
        if self.__dto:
            self.__dto['ProcessFlow'] = processflow
            
            
    def get_processflow(self):
        if self.__dto:
            return self.__dto['ProcessFlow']
        else:
            return None
    
    
    def set_next_frame_func(self, next_frame_func):
        if self.__dto:
            self.__dto['NextFrameFunc'] = next_frame_func
            
            
    def get_next_frame_func(self):
        if self.__dto:
            return self.__dto['NextFrameFunc']
        else:
            return None
    
     
    def set_prev_frame_func(self, prev_frame_func):
        if self.__dto:
            self.__dto['PrevFrameFunc'] = prev_frame_func
            
            
    def get_prev_frame_func(self):
        if self.__dto:
            return self.__dto['PrevFrameFunc']
        else:
            return None 
     
        
    def set_projectpath(self, projpath):
        if self.__dto:
            self.__dto['ProjectPath'] = projpath
            
            
    def get_projectpath(self):
        if self.__dto:
            return self.__dto['ProjectPath']
        else:
            return None
        
    
#----------------- maintain the process ----------------
    def get_first_process(self):
        '''
        get the first processing step
        @return: return status (True/False)
        @return: the first step
        @return: the error message when the validation failed
        '''
        #verify the input type
        if self.__dto:
            if self.__dto['ProcessFlow'] and len(self.__dto['ProcessFlow']):
                proc = self.__dto['ProcessFlow'] 
                return True, proc[0], None
            else:
                return False, None, 'There is no process info'
        else:
            return False, None, 'There is no transaction info, please re-open the app'
        
        
    def add_next_process(self, next_step):
        '''
        add a new processing step at the end of the process flow list
        @param next_step: the new processing step
        @return: return status (True/False)
        @return: the error message when the validation failed
        '''
        #verify the input type
        if not isinstance(next_step, Mainframe_enum):
            return False, 'The input parameter is incorrect'
        
        if self.__dto:
            if self.__dto['ProcessFlow']:
                proc = self.__dto['ProcessFlow']
                proc.append(next_step)
                return True, None
            else:
                self.__dto['ProcessFlow'] = [next_step]
                return True, None
        else:
            return False, 'There is no transaction info, please re-open the app'
        
        
    def get_next_process(self, curr_step=None):
        '''
        get the next processing step
        @param curr_step: the current processing step
        @return: return status (True/False)
        @return: the next step
        @return: the error message when the validation failed
        '''
        #verify the transaction dto
        if not self.__dto:
            return False, None, 'There is no transaction info, please re-open the app'
        elif not self.__dto['ProcessFlow']:
            return False, None, 'There is no process info'
        
        #verify the input type
        if not curr_step:
            curr_step = self.get_currentframe()
        elif not isinstance(curr_step, Mainframe_enum):
            return False, None, 'The input parameter is incorrect'
        
        try:
            proc = self.__dto['ProcessFlow']
            idx = proc.index(curr_step)
            #verify if current step is the last step
            if idx+1 >= len(proc):
                return True, None, 'This is the last processing.'
            else:
                return True, proc[idx+1], None
        except ValueError as e:
            print('expect:', e)
            return False, None, e
        
    
    def get_prev_process(self, curr_step=None):
        '''
        get the previous processing step
        @param curr_step: the current processing step
        @return: return status (True/False)
        @return: the next step
        @return: the error message when the validation failed
        '''
        #verify the transaction dto
        if not self.__dto:
            return False, None, 'There is no transaction info, please re-open the app'
        elif not self.__dto['ProcessFlow']:
            return False, None, 'There is no process info'
        
        #verify the input type
        if not curr_step:
            curr_step = self.get_currentframe()
        elif not isinstance(curr_step, Mainframe_enum):
            return False, None, 'The input parameter is incorrect'
        
        try:
            proc = self.__dto['ProcessFlow']
            idx = proc.index(curr_step)
            #verify if current step is the last step
            if idx == 0:
                return True, None, 'This is the first processing'
            else:
                return True, proc[idx-1], None
        except ValueError as e:
            print('expect:', e)
            return False, None, e
    
    
    def update_process_flow_by_selection(self, selections):
        '''
        update the process flow according to the selections from 'Generate Selection' frame
        @param selections: the selections from 'Generate Selection' frame
        '''
        for key, value in selections.items():
            if value.get() == 1:
                #matching the short name in frame enums
                for ii in Mainframe_enum:
                    if key == ii.value[1]:
                        self.add_next_process(ii)
            else:
                continue
        
        
    def print_processflow(self):
        '''
        debug function, it will print the process flow in CONSOLE_SCREEN_BUFFER_INFO
        '''
        proc = self.__dto['ProcessFlow']
        idx = 1
        for ii in proc:
            print(str(idx) + ':' + str(ii))
            idx = idx + 1