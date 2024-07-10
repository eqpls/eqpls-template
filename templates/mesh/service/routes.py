# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from stringcase import snakecase
from typing import Annotated, Literal, List, Any
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, BackgroundTasks, Query

from common import getConfig, Logger, MultiTask, AsyncRest, ID, ModelStatus

from .controls import Control

from schema.sample.model import Blog, Message

#===============================================================================
# SingleTone
#===============================================================================
config = getConfig('../module.ini')
Logger.register(config)
rootPath = f"/{snakecase(config['default']['title'])}"
api = FastAPI(
    title=config['default']['title'],
    separate_input_output_schemas=False,
    docs_url=f'{rootPath}/docs',
    openapi_url=f'{rootPath}/openapi.json'
)
ctrl = Control(api, config)


#===============================================================================
# API Interfaces
#===============================================================================
@api.get('/blog')
async def blog():
    return await Blog.searchModels()
