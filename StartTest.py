#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing

import unittest
import time
import HTMLTestRunner
import os

if __name__ == '__main__':
    # suite = unittest.defaultTestLoader.discover('.', pattern='TestCase*.py')
    # time_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    # # filename = "./TestReport/TestReport_" + time_str + ".html"
    # filename = "./upload/TestReport.html"
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #             stream=fp,
    #             title=u'移动端API自动化测试报告',
    #             # description=u'【测试报告详情】：'
    #             )
    # runner.run(suite)
    # fp.close()

    # os.system('ren ./upload/TestReport01.html ./upload/TestReport.html')

    suite = unittest.defaultTestLoader.discover('.', pattern='TestCase*.py')
    unittest.TextTestRunner().run(suite)
