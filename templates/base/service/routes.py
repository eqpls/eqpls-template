# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from typing import Annotated, Literal, List, Any
from fastapi import Request, WebSocket, WebSocketDisconnect, BackgroundTasks, Query

from common import MultiTask, AsyncRest, ID, ModelStatus

from .controls import Control

from schema.sample.model import Message

#===============================================================================
# SingleTone
#===============================================================================
ctrl = Control('../module.ini')
api = ctrl.api


#===============================================================================
# API Interfaces
#===============================================================================
@api.get(f'{ctrl.uri}/message', tags=['Sample'])
async def get_message(request:Request) -> list[Message]:
    query = request.query_params._dict
    return [message for message in ctrl.messageMap.values()]


@api.post(f'{ctrl.uri}/message', tags=['Sample'])
async def create_message(message:Message) -> Message:
    message = message.setID(path='', type=type(message)).updateStatus()
    ctrl.messageMap[message.id] = message
    return message


@api.put(f'{ctrl.uri}/message/{{id}}', tags=['Sample'])
async def update_message(id:ID, message:Message) -> Message:
    message = message.setID(path='', type=type(message), id=id).updateStatus()
    ctrl.messageMap[message.id] = message
    return message


@api.delete(f'{ctrl.uri}/message/{{id}}', tags=['Sample'])
async def delete_message(id:ID) -> ModelStatus:
    ctrl.messageMap.pop(id)
    return ModelStatus(id=id, sref=Message.getSchemaInfo().sref, uref='', status='deleted')


@api.get(f'{ctrl.uri}/multitask', tags=['Sample'])
async def run_multitask() -> List[Any]:
    async with AsyncRest('https://google.co.kr') as rest:
        async with MultiTask() as multi:
            for _ in range(0, 10): multi(rest.get('/'))
            return await multi.wait()


async def backgroundTask(text): LOG.INFO(text)


@api.get(f'{ctrl.uri}/background', tags=['Task'])
async def run_background(
        background:BackgroundTasks,
        text:Annotated[Literal['hahaha', 'hohoho', 'huhuhu'] | None, Query(alias='$text', description='laugh')]=None
    ):
    background.add_task(backgroundTask, text)


@api.websocket(f'{ctrl.uri}/websocket', tags=['WebSocket'])
async def websocket(socket:WebSocket):
    await socket.accept()
    while True:
        try:
            payload = await socket.receive_json()
            await socket.send_json(payload)
        except WebSocketDisconnect: break
