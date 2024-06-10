# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

import sys
import uvicorn
import configparser

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('../module.conf', encoding='utf-8')
    paths = [path.strip() for path in config['default']['paths'].split(',')]
    for path in paths: sys.path.append(path)
    paths.append('.')
    uvicorn.run(
        'service.routes:app',
        host=config['default']['host'],
        port=int(config['default']['port']),
        reload=True if 'dev' in config['default']['stage'] else False,
        reload_dirs=paths if 'dev' in config['default']['stage'] else None
    )
