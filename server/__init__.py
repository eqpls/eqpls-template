# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
import os
import sys
import uvicorn
import configparser

#===============================================================================
# Implement
#===============================================================================
def run():
    os.chdir(os.path.dirname(__file__))
    config = configparser.ConfigParser()
    config.read('../module.conf', encoding='utf-8')
    stage = config['service']['stage']
    environment = config['service']['environment']
    environment = [environment] if environment else []
    schema = config['service']['schema']
    schema = [schema] if schema else []
    paths = config['service']['paths']
    paths = environment + schema + [path.strip() for path in filter(None, paths.split(','))]
    for path in paths: sys.path.append(path)
    paths.append('.')
    uvicorn.run(
        'service.routes:api',
        host=config['default']['host'],
        port=int(config['default']['port']),
        workers=int(config['service']['workers']) if 'dev' not in stage else None,
        reload=True if 'dev' in stage else False,
        reload_dirs=paths if 'dev' in stage else None,
        log_level='debug' if 'dev' in stage else 'info'
    )
