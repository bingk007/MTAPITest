#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing

import unittest
import time
import Service
import Common
import Utils
import DB
import ComMeth
import random
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context


class TestCaseUser(unittest.TestCase):

    SUCCESS_RESULT = "'code': '1'"
    SUCCESS_RESULT_A = "'code': 1"
    token = []
    ID = Common.make_id()
    BankCode = Common.make_card('工商银行')

    def setUp(self):
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(time_str)

    def tearDown(self):
        time.sleep(1)

    def test201_reigster_borrower(self):
        '''借款人注册'''
        print('register_borrower')
        try:
            tele = random.choice(['150','137','189'])+''.join(random.choice('0123456789') for i in range(8))
            Service.Service().sendPhoneCode(Common.encryt_word(tele))
            time.sleep(1)
            response = Service.Service().register(Common.encryt_word('aaa12345'), DB.get_code(), 'wx',
                                                  tele, None, 2)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test202_register_invester(self):
        '''投资人注册'''
        print('register_invester')
        try:
            Service.Service().sendPhoneCode(Common.encryt_word(Common.teleNum))
            time.sleep(1)
            response = Service.Service().register(Common.encryt_word('aaa12345'), DB.get_code(), 'wx',
                                                  Common.teleNum, '18911111111', 1)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            tokenName = response['data']['userLoginInfo']['tokenName']
            tokenValue = response['data']['userLoginInfo']['tokenValue']
            authorization = response['data']['authorization']
            Utils.Utils.headers_wx['Authorization'] = authorization
            Utils.Utils.cookies['tokenName'] = tokenName
            Utils.Utils.cookies['tokenValue'] = tokenValue
        except Exception as ex:
            raise ex

    def test203_account_open(self):
        '''开通银行存管流程'''
        print('account_open')
        try:
            response = Service.Service().account_open('民投君', 1, 'Android', Common.encryt_word(self.ID), 1)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            params = {
                'sign': response['data']['sign'],
                'orig': response['data']['data'],
                'returnurl': response['data']['returnUrl'],
                'NOTIFYURL': response['data']['notifyUrl']
            }
            responseN = Service.Service().netLoanIn(
                params['sign'], params['orig'], params['returnurl'],params['NOTIFYURL'], 0)
            Common.EMP_SID = re.compile("EMP_SID=(.+?)';").search(responseN).group(1)
            Common.orderid = re.compile("orderid='\+'(.+?)'\+").search(responseN).group(1)
            for i in range(10):
                responseA = Service.Service().netLoanInSendMobileNotice(
                    Common.teleNum, 'NETLTEMP_NETL01', '执行存管子账户开立操作', ComMeth.corporbank_image(), 'NETL01', '')
                search_str = re.compile('field id="errorCode" required="false"').search(responseA)
                if search_str is None:
                    time.sleep(5)
                    continue
                else:
                    break
            responseB = Service.Service().corporbank_opt(Common.teleNum)
            search_stropt = re.compile('<td>成功</td>\n<td>(.+?)</td>').search(responseB).group(1)
            responseC = Service.Service().netLoanCheckMobile(
                search_stropt, Common.teleNum, Common.orderid, 'NETL01', '民投君', self.ID, self.BankCode, '01102')
            search_md5 = re.compile('id="md5Mobile" value="(.+?)"').search(responseC).group(1)
            responseD = Service.Service().openSubAcctSubmit(
                '01102', Common.teleNum, 2, Common.nowTime, self.BankCode, search_md5, search_stropt, Common.TrdePwd,
                Common.TrdePwd, Common.EMP_SID, params['NOTIFYURL'], params['returnurl'], '中国工商银行', '中国工商银行')
            last_orig = re.compile("orig='\+'(.+?)'\+'").search(responseD).group(1)
            last_sign = re.compile("sign='\+'(.+?)'\+").search(responseD).group(1)
            Service.Service().callback_return(last_orig, last_sign, 'WeChat')
            Service.Service().pa_config()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test204_login(self):
        '''用户登录'''
        print('login')
        try:
            response = Service.Service().login(Common.LoginPwd, 66666, Common.teleNum)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            authorization = response['data']['authorization']
            Utils.Utils.headers['Authorization'] = authorization
            # print(authorization)
        except Exception as ex:
            raise ex

    def test205_autologin(self):
        '''自动登录'''
        print('autologin')
        try:
            response = Service.Service().autologin()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            tokenName = response['data']['userLoginInfo']['tokenName']
            tokenValue = response['data']['userLoginInfo']['tokenValue']
            Utils.Utils.cookies['tokenName'] = tokenName
            Utils.Utils.cookies['tokenValue'] = tokenValue
        except Exception as ex:
            raise ex

    def test206_nickname_update(self):
        '''设置昵称'''
        print('nickname_update')
        try:
            response = Service.Service().nickname_update('辣鸡')
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test207_modifyLoginPwd(self):
        '''修改登录密码'''
        print('modifyLoginPwd')
        try:
            response = Service.Service().modifyLoginPwd(
                Common.LoginPwd_A, Common.LoginPwd, Common.LoginPwd_A)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test208_findPwd_verify(self):
        '''重置密码第一步'''
        print('findPwd_verify')
        try:
            for i in range(5):
                captcha = ComMeth.captcha('./upload/picture.jpg')
                response = Service.Service().findPwd_verify(captcha, Common.teleNum)
                if response['code'] == '1':
                    break
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            self.token.append(response['data']['tokenName'])
            self.token.append(response['data']['tokenValue'])
        except Exception as ex:
            raise ex

    def test209_findPwd_reset(self):
        '''重置密码第二步'''
        print('findPwd_reset')
        try:
            response = Service.Service().findPwd_reset(
                Common.LoginPwd, DB.get_code(), self.token[0], self.token[1])
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test210_validatePassword(self):
        '''修改手势密码时验证登录密码'''
        print('validatePassword')
        try:
            ComMeth.login(Common.teleNum)
            response = Service.Service().validatePassword(Common.LoginPwd)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test211_query_log(self):
        '''用户风险评测等级'''
        print('query_log')
        try:
            response = Service.Service().query_log()
            Common.search_str(str(response), [self.SUCCESS_RESULT_A])
        except Exception as ex:
            raise ex

    def test212_query_all(self):
        '''风险评测试题'''
        print('query_all')
        try:
            response = Service.Service().query_all()
            Common.search_str(str(response), [self.SUCCESS_RESULT_A])
        except Exception as ex:
            raise ex

    def test213_submit(self):
        '''提交评测结果'''
        print('submit')
        try:
            response = Service.Service().submmit('[2,9,15,19,23,28,31,37,41,47,50]')
            Common.search_str(str(response), [self.SUCCESS_RESULT_A])
        except Exception as ex:
            raise ex

    def test214_center_complete(self):
        '''领取积分奖励'''
        print('center_complete')
        try:
            response = Service.Service().center_complete(4)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test215_task_list(self):
        '''任务中心列表'''
        print('task_list')
        try:
            response = Service.Service().tasks_list()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test216_score_sign(self):
        '''每日签到'''
        print('score_sign')
        try:
            response = Service.Service().score_sign()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test217_feedback(self):
        '''提交意见反馈'''
        print('feedback')
        try:
            response = Service.Service().feedback(
                'SM-G9300', 'Android', '7.0', '13756555555', 'ffffffff-8799-acf6-ffff-ffffc9461618', 'MT-好的好的-666', '2.8.0')
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    def test218_auth_apply(self):
        '''存管账户授权'''
        print('auth_apply')
        try:
            response = Service.Service().auth_apply(1, 'Android', 1, 1)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            params = {
                'sign': response['data']['sign'],
                'orig': response['data']['data'],
                'returnurl': response['data']['returnUrl'],
                'NOTIFYURL': response['data']['notifyUrl']
            }
            responseN = Service.Service().netLoanIn(
                params['sign'], params['orig'], params['returnurl'], params['NOTIFYURL'], 0)
            Common.EMP_SID = re.compile("EMP_SID=(.+?)';").search(responseN).group(1)
            Service.Service().sendMobileNotice('NETLTEMP_NETL17_1', '注册电商平台会员管理系统用户1123')
            responseA = Service.Service().corporbank_opt(Common.teleNum)
            search_stropt = re.compile('<td>成功</td>\n<td>(.+?)</td>').search(responseA).group(1)
            responseB = Service.Service().verifyMobileToken(search_stropt, Common.TrdePwd)
            search_md5 = re.compile('id="md5Mobile" value="(.+?)"').search(responseB).group(1)
            responseC = Service.Service().accountAccessMac(
                Common.EMP_SID, Common.nowTime, Common.TrdePwd, params['returnurl'], params['NOTIFYURL'], search_md5, 1)
            last_orig = re.compile("orig='\+'(.+?)'\+'").search(responseC).group(1)
            last_sign = re.compile("sign='\+'(.+?)'\+").search(responseC).group(1)
            Service.Service().callback_return(last_orig, last_sign, 'Android')
        except Exception as ex:
            raise ex


