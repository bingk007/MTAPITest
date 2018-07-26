#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing

import unittest
import time
import Service
import Common


class TestCaseFind(unittest.TestCase):

    SUCCESS_RESULT = "'code': '1'"

    def setUp(self):
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(time_str)

    def tearDown(self):
        time.sleep(1)

    def test501_findpage_home(self):
        '''发现页面'''
        print('findpage_home')
        try:
            response = Service.Service().findpage_home()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test502_planner_friends(self):
        '''我的好友'''
        print('planner_friends')
        try:
            response = Service.Service().planner_friends(0, 10)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test503_center_index(self):
        '''会员中心'''
        print('center_index')
        try:
            response = Service.Service().center_index()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test504_notice_listing(self):
        '''平台公告'''
        print('notice_listing')
        try:
            response = Service.Service().notice_listing(20, 0)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test505_report_listing(self):
        '''媒体报道'''
        print('report_listing')
        try:
            response = Service.Service().report_listing(10, 0)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex


