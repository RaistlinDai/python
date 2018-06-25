'''
Created on Jun 23, 2018

@author: ftd
'''

class IFrameConf(object):
    '''
    classdocs
    '''


    def set_conf(self, **confs):
        
        for child in self.winfo_children():
                        
            #config
            for key in confs.keys():
                if key == 'font':
                    child.config(font=confs[key])
                elif key == 'bg':
                    child.config(bg=confs[key])
                elif key == 'fg':
                    child.config(fg=confs[key])
                elif key == 'relief':
                    child.config(relief=confs[key])