'''
Created on Jul 10, 2018

@author: ftd
'''

from cassandra.cluster import Cluster

class Cassandra_service_impl(object):
    '''
    classdocs
    '''

    def __init__(self, **params):
        '''
        Constructor
        '''
        self.__cluster = Cluster()
    
    