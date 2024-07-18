# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from typing import Annotated, Literal
from fastapi import Query

from common import AUTH_HEADER, ORG_HEADER, ID, ModelStatus

from .controls import Control

from schema.sample.model import Blog

#===============================================================================
# SingleTone
#===============================================================================
ctrl = Control('../module.ini')
api = ctrl.api


#===============================================================================
# API Interfaces
#===============================================================================
@api.get(f'{ctrl.uri}/blog/{{id}}', tags=['Sample'])
async def read_blog(
    id: ID,
    token: AUTH_HEADER,
    org: ORG_HEADER=None
) -> Blog: return await Blog.readModelByID(
    id=id,
    token=token,
    org=org
)


@api.get(f'{ctrl.uri}/blog', tags=['Sample'])
async def search_blog(
    token: AUTH_HEADER,
    org: ORG_HEADER=None,
    filter:Annotated[str | None, Query(alias='$filter', description='lucene type filter ex) $filter=fieldName:yourSearchText')]=None,
    orderBy:Annotated[str | None, Query(alias='$orderby', description='ordered by specific field')]=None,
    order:Annotated[Literal['asc', 'desc'], Query(alias='$order', description='ordering type')]=None,
    size:Annotated[int | None, Query(alias='$size', description='retrieving model count')]=None,
    skip:Annotated[int | None, Query(alias='$skip', description='skipping model count')]=None,
    archive:Annotated[Literal['true', 'false', ''], Query(alias='$archive', description='searching from archive aka database')]=None
) -> Blog: return await Blog.searchModels(
    filter=filter,
    orderBy=orderBy,
    order=order,
    size=size,
    skip=skip,
    archive=archive,
    token=token,
    org=org
)


@api.post(f'{ctrl.uri}/blog', tags=['Sample'])
async def create_blog(
    blog: Blog,
    token: AUTH_HEADER,
    org: ORG_HEADER=None
) -> Blog: return await blog.createModel(
    token=token,
    org=org
)


@api.post(f'{ctrl.uri}/blog/{{id}}', tags=['Sample'])
async def update_blog(
    id: ID,
    blog: Blog,
    token: AUTH_HEADER,
    org: ORG_HEADER=None
) -> Blog: return await blog.setID(str(id)).updateModel(
    token=token,
    org=org
)


@api.delete(f'{ctrl.uri}/blog/{{id}}', tags=['Sample'])
async def delete_blog(
    id: ID,
    token: AUTH_HEADER,
    org: ORG_HEADER=None
) -> ModelStatus: return await Blog.deleteModelByID(
    id=id,
    token=token,
    org=org
)
