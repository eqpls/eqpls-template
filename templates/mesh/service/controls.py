# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from common import MeshControl

from schema.sample.model import Blog


#===============================================================================
# Implement
#===============================================================================
class Control(MeshControl):

    def __init__(self, api, config): MeshControl.__init__(self, api, config)

    async def startup(self):
        await self.registerModel(Blog, 'uerp')

    #===========================================================================
    # Interface
    #===========================================================================
