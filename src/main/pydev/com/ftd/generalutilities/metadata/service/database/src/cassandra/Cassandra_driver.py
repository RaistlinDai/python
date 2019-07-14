'''
Created on Jul 10, 2018

@author: ftd
'''

from cassandra.cluster import Cluster

class Cassandra_driver(object):
    '''
    classdocs
    '''

    def __init__(self, **params):
        '''
        Constructor
        '''
        self.__cluster = Cluster()
    
    