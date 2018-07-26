#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing

import unittest
import time
import Service
import Common
import ComMeth
import json
import Utils
import config


class TestCaseProduct(unittest.TestCase):

    SUCCESS_RESULT = "'code': '1'"
    productInfo = []

    def setUp(self):
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(time_str)

    def tearDown(self):
        time.sleep(1)

    def list(self, pageSize, pageNum, productType, productArea):
        try:
            response = Service.Service().listing(pageSize, pageNum, productType, productArea)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            productList = response['data']['productList']
            for i in range(len(productList)):
                if productList[i]['surplusAmount'] > 200:
                    self.productInfo.append(productList[i]['id'])
                    break
        except Exception as ex:
            raise ex

    def test301_home(self):
        '''项目列表一级页面（新手，散标，转让）'''
        print('home')
        try:
            ComMeth.login(config.Test_Mobile)
            response = Service.Service().home()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test302_new_listing(self):
        '''项目列表二级页面新手标列表'''
        print('new_listing')
        try:
            self.list(10, 0, 1, 2)
        except Exception as ex:
            raise ex

    def test303_listing(self):
        '''项目列表二级页面散标列表'''
        print('listing')
        try:
            self.list(10, 0, 1, 1)
        except Exception as ex:
            raise ex

    def test304_transfer_listing(self):
        '''项目列表二级页面转让列表'''
        print('transfer_listing')
        try:
            response = Service.Service().transfer_listing(10, 0)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            productList = response['data']['productList']
            for i in range(len(productList)):
                if productList[i]['surplusAmount'] > 200:
                    self.productInfo.append(productList[i]['id'])
                    break
        except Exception as ex:
            raise ex

    def test305_planDetail(self):
        '''散标项目详情'''
        print('planDetail')
        try:
            response = Service.Service().planDetail(self.productInfo[1])
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test306_transfer_detail(self):
        '''转让标项目详情'''
        print('transfer_detail')
        try:
            response = Service.Service().transfer_detail(self.productInfo[2])
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test307_investRecord(self):
        '''投资记录'''
        print('investRecord')
        try:
            for productId in (self.productInfo[1], self.productInfo[2]):
                response = Service.Service().investRecord(0, productId, 20)
                Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test308_transfer_invest(self):
        '''债权信息'''
        print('transfer_invest')
        try:
            response = Service.Service().transfer_invest(0, self.productInfo[2], 15)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test309_original_invest(self):
        '''债权转让记录'''
        print('original_invest')
        try:
            response = Service.Service().original_invest(0, self.productInfo[2], 15)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test310_invest_plan(self):
        '''散标投资并使用优惠券'''
        print('invest_plan')
        try:
            ComMeth.login_be()
            Service.Service().add_coupon(264, config.Test_Mobile)
            Service.Service().add_coupon(265, config.Test_Mobile)
            responseA = Service.Service().list_coupon(10, 0, 'asc', config.Test_Mobile)
            rows = json.loads(responseA)['rows']
            for i in range(len(rows)):
                Service.Service().send_coupon(rows[i]['id'])
            coupon = Service.Service().couponRecords(10, 0, 1)
            couponIdentifier = coupon['data']['couponRecordList'][0]['identifier']
            token = ComMeth.getToken()
            response = Service.Service().invest(self.productInfo[1], token[0], token[1], 100, 2, couponIdentifier)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test311_invest_transfer(self):
        '''转让标投资并使用优惠券'''
        print('invest_transfer')
        try:
            coupon = Service.Service().couponRecords(10, 0, 1)
            couponIdentifier = coupon['data']['couponRecordList'][0]['identifier']
            token = ComMeth.getToken()
            response = Service.Service().invest(self.productInfo[2], token[0], token[1], 100, 2, couponIdentifier)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test312_invest_new(self):
        '''新用户投资新手标'''
        print('invest_new')
        try:
            ComMeth.login(Common.teleNum)
            # ComMeth.login_be()
            Service.Service().recharge_be(Common.teleNum, '500')
            token = ComMeth.getToken()
            response = Service.Service().invest(self.productInfo[0], token[0], token[1], 100, 2)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex
