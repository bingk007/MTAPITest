#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing

import unittest
import time
import Service
import Common


class TestCaseOther(unittest.TestCase):

    SUCCESS_RESULT = "'code': '1'"

    def setUp(self):
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(time_str)

    def tearDown(self):
        time.sleep(1)

    def test101_startPage(self):
        '''启动页面'''
        print('startPage')
        try:
            response = Service.Service().startPage('280')
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test102_config(self):
        '''配置信息'''
        print('config')
        try:
            response = Service.Service().config()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test103_upgradeConfig(self):
        '''版本升级配置信息'''
        print('upgradeConfig')
        try:
            response = Service.Service().upgradeConfig('280')
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test104_index(self):
        '''首页数据'''
        print('index')
        try:
            response = Service.Service().index()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test105_cardList(self):
        '''银行卡列表'''
        print('cardList')
        try:
            response = Service.Service().cardList()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test106_play_list(self):
        '''活动中心列表'''
        print('play_list')
        try:
            response = Service.Service().play_list()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

