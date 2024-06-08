# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from common import ID, Profile, Metadata, TStamp, Status
from typing import Union, Optional


#===============================================================================
# Implement
#===============================================================================
class Message(Metadata, TStamp, ID):
    text: Optional[str] = ''
