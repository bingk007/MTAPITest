#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing

import unittest
import time
import Service
import Common
import ComMeth
import math
import config


class TestCaseAccount(unittest.TestCase):

    SUCCESS_RESULT = "'code': '1'"
    regularInvestInfo = []
    count = []
    investId = []

    def setUp(self):
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(time_str)

    def tearDown(self):
        time.sleep(1)

    def test401_userInfo(self):
        '''用户信息'''
        print('userInfo')
        try:
            ComMeth.login(config.Test_Mobile)
            response = Service.Service().userInfo()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test402_journal(self):
        '''资金流水'''
        print('journal')
        try:
            for pageNum in (0, 1):
                response = Service.Service().journal(20, pageNum)
                Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test403_regularInvest_list(self):
        '''投资项目'''
        print('regularInvest_list')
        try:
            for investStatus in (2, 3, 4):
                # for pageNum in (0, 1):
                response = Service.Service().regularInvest_list(10, 0, investStatus)
                Common.search_str(str(response), [self.SUCCESS_RESULT])
                record = response['data']['InvestRecords']
                self.count.append(response['data']['count'])
                if len(record):
                    self.regularInvestInfo.append(record[0]['id'])
        except Exception as ex:
            raise ex

    def test404_regularInvest_detail(self):
        '''投资项目详情'''
        print('regularInvest_detail')
        try:
            for id in self.regularInvestInfo:
                response = Service.Service().regularInvest_detail(id)
                Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test405_transferindex(self):
        '''申请债券转让页面'''
        print('transferindex')
        try:
            for m in range(int(math.ceil(self.count[1]/10))):
                responseA = Service.Service().regularInvest_list(10, m, 3)
                record = responseA['data']['InvestRecords']
                for i in range(len(record)):
                    if record[i]['transferStatus'] == 2:
                        self.investId.append(record[i]['id'])
                        break
                if len(self.investId) > 0:
                    break
            responseB = Service.Service().transferindex(self.investId[0])
            Common.search_str(str(responseB), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test406_transfer_reasons(self):
        '''转让原因'''
        print('transfer_reasons')
        try:
            response = Service.Service().transfer_reasons()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test407_transferadd(self):
        '''申请转让'''
        print('transferadd')
        try:
            response = Service.Service().transferadd(self.investId[0], 0, 1, 2)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test408_regularInvest_detail(self):
        '''转让详情'''
        print('regularInvest_detail2')
        try:
            response = Service.Service().regularInvest_detail(self.investId[0], 0, 10)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test409_transfercancel(self):
        '''撤销转让'''
        print('transfercancel')
        try:
            response = Service.Service().transfercancel(self.investId[0])
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test410_Calendar_list(self):
        '''回款日历'''
        print('Calendar_list')
        try:
            response = Service.Service().Calendar_list(ComMeth.getCalendar())
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test411_repayplan_list(self):
        '''回款计划'''
        print('repayplan_list')
        try:
            for year in (2018, 2019):
                response = Service.Service().repayplan_list(year, 15, 0)
                Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test412_autoInvest_set(self):
        '''自动投标配置信息'''
        print('autoInvest_set')
        try:
            response = Service.Service().autoInvest_set()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test413_autoInvest_up(self):
        '''开启自动投标，按多种条件组合设置'''
        print('autoInvest_up')
        try:
            for repayTypes in (1, 2, 3, '1,2,3'):
                for configId in (5, 6, 7, 8, 9):
                    token = ComMeth.getToken()
                    response = Service.Service().autoInvest_up(repayTypes, configId, token[0], token[1], 1, 0, 100)
                    Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test414_autoInvest_close(self):
        '''关闭自动投标'''
        print('autoInvest_close')
        try:
            response = Service.Service().autoInvest_close()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test415_couponRecords(self):
        '''优惠券信息'''
        print('couponRecords')
        try:
            for pageNum in (0, 1):
                response = Service.Service().couponRecords(10, pageNum, 3)
                Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test416_planner(self):
        '''推荐奖励'''
        print('planner')
        try:
            for pageNum in (0, 1):
                response = Service.Service().planner(15, pageNum)
                Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test417_bankInfo(self):
        '''充值限额'''
        print('payment_bankInfo')
        try:
            response = Service.Service().bankInfo()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test418_recharge_apply(self):
        '''充值申请'''
        print('recharge_apply')
        try:
            response = Service.Service().recharge_apply(100, 'Android')
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test419_calculateCost(self):
        '''提现手续费计算'''
        print('calculateCost')
        try:
            response = Service.Service().calculateCost()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test420_withdraw_apply(self):
        '''提现申请'''
        print('withdraw_apply')
        try:
            response = Service.Service().withdraw_apply(10, 'Android')
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex


