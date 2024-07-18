# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from common import UerpControl

from driver.auth_kc_redis import AuthKeyCloakRedis
from driver.redis import RedisModel
from driver.elasticsearch import ElasticSearch
from driver.postgresql import PostgreSql

from schema.sample.model import Blog, Message


#===============================================================================
# Implement
#===============================================================================
class Control(UerpControl):

    def __init__(self, confPath):
        UerpControl.__init__(
            self,
            confPath=confPath,
            authDriver=AuthKeyCloakRedis,
            cacheDriver=RedisModel,
            searchDriver=ElasticSearch,
            databaseDriver=PostgreSql
        )

    async def startup(self):
        await self.registerModel(Blog)
        await self.registerModel(Message)

    async def shutdown(self): pass
