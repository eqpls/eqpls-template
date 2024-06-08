# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from common import setEnvironment, getConfig, Logger, MultiTask, AsyncRest
from service.tasks import Task

from uuid import UUID
from schema.sample import Message, Status

#===============================================================================
# SingleTone
#===============================================================================
setEnvironment('CONFIG', getConfig('server.conf'))
Logger.register(CONFIG)
app = FastAPI(title=CONFIG['default']['title'])
task = Task()


@app.on_event('startup')
async def runStartUp(): await task.startup()


@app.on_event('shutdown')
async def runShutDown(): await task.shutdown()


#===============================================================================
# API Interfaces
#===============================================================================
@app.get('/message', tags=['Message'])
async def get_message(request:Request) -> list[Message]:
    query = request.query_params._dict
    return await task.get_message(**query)


@app.post('/message', tags=['Message'])
async def create_message(message:Message) -> Message:
    return await task.create_message(message)


@app.put('/message/{id}', tags=['Message'])
async def update_message(id:UUID, message:Message) -> Message:
    message.id = id
    return await task.update_message(message)


@app.delete('/message/{id}', tags=['Message'])
async def delete_message(id:UUID) -> Status:
    await task.delete_message(id)
    return Status(status='deleted')


@app.get('/multitask', tags=['Test'])
async def get_multitask() -> list:
    async with AsyncRest('https://google.co.kr') as rest:
        async with MultiTask() as multi:
            for _ in range(0, 10): multi(rest.get('/'))
            return await multi.wait()


@app.websocket('/websocket')
async def get_websocket(socket:WebSocket):
    await socket.accept()
    while True:
        try:
            payload = await socket.receive_json()
            await socket.send_json(payload)
        except WebSocketDisconnect: break

