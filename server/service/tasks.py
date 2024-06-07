# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
import json
from uuid import UUID
from time import time as tstamp
from common import EpException


#===============================================================================
# Implements
#===============================================================================
class Task:

    def __init__(self): pass

    async def startup(self): pass

    async def shutdown(self): pass

    #===========================================================================
    # Interface
    #===========================================================================
    async def get_test(self, **query):
        LOG.INFO(f'QUERY {json.dumps(query)}')
        return query
