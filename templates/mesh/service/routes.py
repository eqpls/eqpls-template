# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from typing import Annotated, Literal, List, Any
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, BackgroundTasks, Query
from common import getConfig, Logger, MultiTask, AsyncRest
from .controls import Control
from common import ID, ModelStatus

from schema.sample.model import Message

#===============================================================================
# SingleTone
#===============================================================================
config = getConfig('../module.conf')
Logger.register(config)
api = FastAPI(title=config['default']['title'], separate_input_output_schemas=False)
ctrl = Control(api, config)

#===============================================================================
# API Interfaces
#===============================================================================
