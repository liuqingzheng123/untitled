# -*- coding:utf-8 -*-
# Author : liuqingzheng
# Data : 2018/11/13 21:17
from mysetting import globalsetting
import importlib
class Setting:
    def __init__(self,settings_module):
        for setting in dir(globalsetting):
            if setting.isupper():
                setattr(self, setting, getattr(globalsetting, setting))

        mod = importlib.import_module(settings_module)
        # mod=settings_module
        for setting in dir(mod):
            if setting.isupper():
                setting_value = getattr(mod, setting)
                setattr(self, setting, setting_value)



setting=Setting('setting')