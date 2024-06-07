# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

import uvicorn
from common import getConfig

if __name__ == '__main__':

    config = getConfig('server.conf')
    uvicorn.run(
        'service.routes:app',
        host=config['default']['host'],
        port=int(config['default']['port']),
        reload=True if 'dev' in config['default']['stage'] else False,
        reload_dirs=['.'] if 'dev' in config['default']['stage'] else None
    )
