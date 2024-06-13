# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
import json
import asyncio
from uuid import UUID
from time import time as tstamp
from common import EpException, asleep, runBackground


#===============================================================================
# Implement
#===============================================================================
class Task:

    def __init__(self):
        self.messageMap = {}

    async def startup(self):
        await runBackground(self.background())

    async def shutdown(self): pass

    async def background(self):
        while True:
            LOG.INFO('background')
            await asleep(2)

    #===========================================================================
    # Interface
    #===========================================================================
    async def get_message(self, **query):
        if query: LOG.INFO(f'QUERY {json.dumps(query)}')
        return [message for message in self.messageMap.values()]

    async def create_message(self, message):
        id = message.generateID()
        self.messageMap[str(id)] = message.dict()
        return message

    async def update_message(self, message):
        self.messageMap[str(message.id)] = message.dict()
        return message

    async def delete_message(self, id):
        self.messageMap.pop(str(id))
