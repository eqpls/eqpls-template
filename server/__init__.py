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
    config = configparser.ConfigParser()
    config.read('module.ini', encoding='utf-8')
    environment = os.path.abspath(config['service']['environment'])
    environment = [environment] if environment else []
    schema = os.path.abspath(config['service']['schema'])
    schema = [schema] if schema else []
    paths = config['service']['paths']
    paths = environment + schema + [os.path.abspath(path.strip()) for path in filter(None, paths.split(','))]
    stage = config['service']['stage']
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    for path in paths: sys.path.append(path)
    paths.append('.')
    uvicorn.run(
        'service.routes:api',
        host=config['default']['host'],
        port=int(config['default']['port']),
        loop='uvloop' if 'container' in config['service']['runtime'] else 'auto',
        workers=int(config['service']['workers']) if 'dev' not in stage else None,
        reload=True if 'dev' in stage else False,
        reload_dirs=paths if 'dev' in stage else None,
        log_level='debug' if 'dev' in stage else 'info'
    )
