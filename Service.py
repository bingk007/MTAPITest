#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing


import Utils
import ssl
import Common

ssl._create_default_https_context = ssl._create_unverified_context


class Service:

    def startPage(self, appVersion):
        params = {
            'appVersion': appVersion
        }
        url = '/mobile/cms/startPage.json'
        return Utils.Utils().http_get_request(params, url)

    def config(self):
        params = {
        }
        url = '/mobile/config.json'
        return Utils.Utils().http_get_request(params, url)

    def upgradeConfig(self, currentVersion):
        params = {
            'currentVersion': currentVersion
        }
        url = '/mobile/upgradeConfig.json'
        return Utils.Utils().http_get_request(params, url)

    def index(self):
        params = {
        }
        url = '/mobile/assets/index.json'
        return Utils.Utils().http_get_request(params, url)

    def home(self):
        params = {
        }
        url = '/mobile/v200/home.json'
        return Utils.Utils().http_get_request(params, url)

    def sendPhoneCode(self, mobile):
        params = {
            'mobile': mobile
            }
        url = '/mobile/user/sendPhoneCode.json'
        return Utils.Utils().request_wx(params, url, 'get')

    def register(self, password, mobileCode, origin, mobile, plannerMobile, userRole):
        params = {
            'password': password,
            'mobileCode': mobileCode,
            'origin': origin,
            'mobile': mobile,
            'plannerMobile': plannerMobile,
            'userRole': userRole
            }
        url = '/mobile/user/register.json'
        return Utils.Utils().request_wx(params, url, 'post')

    def login(self, password, captchaCode, loginId):
        params = {
            'password': password,
            'captchaCode': captchaCode,
            'loginId': loginId
            }
        url = '/mobile/user/login.json'
        return Utils.Utils().http_post_request(params, url)

    def autologin(self):
        params = {
        }
        url = '/mobile/user/autologin.json'
        return Utils.Utils().http_get_request(params, url)

    def userInfo(self):
        params = {
        }
        url = '/mobile/my/userInfo.json'
        return Utils.Utils().http_get_request(params, url)

    def home(self):
        params = {
        }
        url = '/mobile/v200/home.json'
        return Utils.Utils().http_get_request(params, url)

    def listing(self, pageSize, pageNum, productType, productArea):
        params = {
            'productArea': productArea,
            'pageSize': pageSize,
            'pageNum': pageNum,
            'productType': productType
        }
        url = '/mobile/v140/product/listing.json'
        return Utils.Utils().http_get_request(params, url)

    def transfer_listing(self, pageSize, pageNum):
        params = {
            'pageSize': pageSize,
            'pageNum': pageNum,
        }
        url = '/mobile/product/transfer/listing.json'
        return Utils.Utils().http_get_request(params, url)

    def planDetail(self, productId):
        params = {
            'productId': productId
        }
        url = '/mobile/product/planDetail.json'
        return Utils.Utils().http_get_request(params, url)

    def transfer_detail(self, productId):
        params = {
            'productId': productId
        }
        url = '/mobile/product/transfer/detail.json'
        return Utils.Utils().http_get_request(params, url)

    def investRecord(self, pageNum, productId, pageSize):
        params = {
            'pageNum': pageNum,
            'productId': productId,
            'pageSize': pageSize
        }
        url = '/mobile/product/invest/investRecord.json'
        return Utils.Utils().http_get_request(params, url)

    def transfer_invest(self, pageNum, productId, pageSize):
        params = {
            'pageNum': pageNum,
            'productId': productId,
            'pageSize': pageSize
        }
        url = '/mobile/product/transfer/detail/transfer/invest.json'
        return Utils.Utils().http_get_request(params, url)

    def original_invest(self, pageNum, productId, pageSize):
        params = {
            'pageNum': pageNum,
            'productId': productId,
            'pageSize': pageSize
        }
        url = '/mobile/product/transfer/detail/original/invest.json'
        return Utils.Utils().http_get_request(params, url)

    def couponRecords(self, pageSize, pageNum, status):
        params = {
            'pageSize': pageSize,
            'pageNum': pageNum,
            'status': status
        }
        url = '/mobile/v150/my/couponRecords.json'
        return Utils.Utils().http_get_request(params, url)

    def getToken(self):
        params = {
        }
        url = '/mobile/user/getToken.json'
        return Utils.Utils().http_get_request(params, url)

    def invest(self, productId, tokenName, tokenValue, investAmount, platform, couponIdentifier=None):
        params = {
            'productId': productId,
            'tokenName': tokenName,
            'investAmount': investAmount,
            'tokenValue': tokenValue,
            'couponIdentifier': couponIdentifier,
            'platform': platform
            }
        url = '/mobile/product/invest.json'
        return Utils.Utils().http_post_request(params, url)

    def reward(self):
        params = {
        }
        url = '/mobile/my/invest/reward.json'
        return Utils.Utils().http_get_request(params, url)

    def journal(self, pageSize, pageNum):
        params = {
            'pageSize': pageSize,
            'pageNum': pageNum,
        }
        url = '/mobile/my/journal.json'
        return Utils.Utils().http_get_request(params, url)

    def bankInfo(self):
        params = {
        }
        url = '/mobile/payment/bankInfo.json'
        return Utils.Utils().http_get_request(params, url)

    def recharge_apply(self, amount, origin):
        params = {
            'amount': amount,
            'origin': origin
        }
        url = '/mobile/custody/recharge/apply.json'
        return Utils.Utils().http_get_request(params, url)

    def calculateCost(self):
        params = {
        }
        url = '/mobile/custody/withdraw/calculateCost.json'
        return Utils.Utils().http_get_request(params, url)

    def withdraw_apply(self, amount, origin):
        params = {
            'amount': amount,
            'origin': origin
        }
        url = '/mobile/custody/withdraw/apply.json'
        return Utils.Utils().http_get_request(params, url)

    def regularInvest_list(self, pageSize, pageNum, investStatus):
        params = {
            'pageSize': pageSize,
            'pageNum': pageNum,
            'investStatus': investStatus
        }
        url = '/mobile/my/regularInvest/list.json'
        return Utils.Utils().http_get_request(params, url)

    def regularInvest_detail(self, id, pageNum=None, pageSize=None):
        params = {
            'id': id,
            'pageNum': pageNum,
            'pageSize': pageSize
        }
        url = '/mobile/my/regularInvest/detail.json'
        return Utils.Utils().http_get_request(params, url)

    def transferindex(self, investId):
        params = {
            'investId': investId
        }
        url = '/mobile/my/transferindex.json'
        return Utils.Utils().http_get_request(params, url)

    def transfer_reasons(self):
        params = {
        }
        url = '/mobile/product/transfer/reasons.json'
        return Utils.Utils().http_get_request(params, url)

    def transferadd(self, investId, transferReward, transferReasonId, platform):
        params = {
            'investId': investId,
            'transferReward': transferReward,
            'transferReasonId': transferReasonId,
            'platform': platform
            }
        url = '/mobile/my/transferadd.json'
        return Utils.Utils().http_post_request(params, url)

    def transfercancel(self, investId):
        params = {
            'investId': investId
        }
        url = '/mobile/my/transfercancel.json'
        return Utils.Utils().http_get_request(params, url)

    def Calendar_list(self, startTime):
        params = {
            'startTime': startTime
        }
        url = '/mobile/my/Calendar/list.json'
        return Utils.Utils().http_get_request(params, url)

    def repayplan_list(self, year, pageSize, pageNum):
        params = {
            'year': year,
            'pageSize': pageSize,
            'pageNum': pageNum
        }
        url = '/mobile/my/repayplan/list.json'
        return Utils.Utils().http_get_request(params, url)

    def autoInvest_set(self):
        params = {
        }
        url = '/mobile/my/autoInvest/set.json'
        return Utils.Utils().http_get_request(params, url)

    def autoInvest_up(self, repayTypes, configId, tokenName, tokenValue, isUseCoupon, surplusAmount, minInvestAmount):
        params = {
            'repayTypes': repayTypes,
            'configId': configId,
            'tokenName': tokenName,
            'tokenValue': tokenValue,
            'isUseCoupon': isUseCoupon,
            'surplusAmount': surplusAmount,
            'minInvestAmount': minInvestAmount
            }
        url = '/mobile/my/autoInvest/up.json'
        return Utils.Utils().http_post_request(params, url)

    def autoInvest_close(self):
        params = {
        }
        url = '/mobile/my/autoInvest/close.json'
        return Utils.Utils().http_get_request(params, url)

    def planner(self, pageSize, pageNum):
        params = {
            'pageSize': pageSize,
            'pageNum': pageNum
        }
        url = '/mobile/my/planner.json'
        return Utils.Utils().http_get_request(params, url)

    def planner_friends(self, pageSize, pageNum):
        params = {
            'pageSize': pageSize,
            'pageNum': pageNum
        }
        url = '/mobile/my/planner/friends.json'
        return Utils.Utils().http_get_request(params, url)

    def findpage_home(self):
        params = {
        }
        url = '/mobile/findpage/home.json'
        return Utils.Utils().http_get_request(params, url)

    def center_index(self):
        params = {
        }
        url = '/mobile/member/center/index.json'
        return Utils.Utils().http_get_request(params, url)

    def nickname_update(self, nickname):
        params = {
            'nickname': nickname
        }
        url = '/mobile/my/nickname/update.json'
        return Utils.Utils().http_get_request(params, url)

    def notice_listing(self, pageSize, pageNum):
        params = {
            'pageSize': pageSize,
            'pageNum': pageNum
        }
        url = '/mobile/cms/notice/listing.json'
        return Utils.Utils().http_get_request(params, url)

    def report_listing(self, pageSize, pageNum):
        params = {
            'pageSize': pageSize,
            'pageNum': pageNum
        }
        url = '/mobile/cms/report/listing.json'
        return Utils.Utils().http_get_request(params, url)

    def custode_account(self):
        params = {
        }
        url = '/mobile/custody/account.json'
        return Utils.Utils().http_get_request(params, url)

    def account_open(self, realName, idType, origin, idCardNo, roleType):
        params = {
            'realName': realName,
            'idType': idType,
            # 'bankCardNo': bankCardNo,
            'origin': origin,
            'idCardNo': idCardNo,
            'roleType': roleType,
            }
        url = '/mobile/custody/account/open.json'
        return Utils.Utils().request_wx(params, url, 'post')

    def validatePassword(self, password):
        params = {
            'password': password
            }
        url = '/mobile/user/validatePassword.json'
        return Utils.Utils().http_post_request(params, url)

    def modifyLoginPwd(self, password, oldPassword, confirmPassword):
        params = {
            'password': password,
            'oldPassword': oldPassword,
            'confirmPassword': confirmPassword
            }
        url = '/mobile/my/modifyLoginPwd.json'
        return Utils.Utils().http_post_request(params, url)

    def findPwd_verify(self, captchaCode, mobile):
        params = {
            'captchaCode': captchaCode,
            'mobile': mobile,
            }
        url = '/mobile/user/findPwd/verify.json'
        return Utils.Utils().http_post_request(params, url)

    def findPwd_reset(self, password, mobileCode, tokenName, tokenValue):
        params = {
            'password': password,
            'mobileCode': mobileCode,
            'tokenName': tokenName,
            'tokenValue': tokenValue
            }
        url = '/mobile/user/findPwd/reset.json'
        return Utils.Utils().http_post_request(params, url)

    def query_log(self):
        params = {
        }
        url = '/assess/query/log'
        return Utils.Utils().http_get_request(params, url)

    def unbunding(self):
        params = {
        }
        url = '/mobile/others/user/unbundling.json'
        return Utils.Utils().http_get_request(params, url)

    def netLoanIn(self, sign, orig, returnurl, NOTIFYURL, userType):
        params = {
            'sign': sign,
            'orig': orig,
            'returnurl': returnurl,
            'NOTIFYURL': NOTIFYURL,
            'userType': userType
        }
        url = '/corporbank/netLoanIn.do'
        return Utils.Utils().request_orangebank(params, url)

    def netLoanInSendMobileNotice(self, mobile, smsTempletId, extContent, checkCode, tranCode, _):
        params = {
            'mobile': mobile,
            'smsTempletId': smsTempletId,
            'extContent': extContent,
            'checkCode': checkCode,
            'tranCode': tranCode,
            '_': _
        }
        url = '/corporbank/netLoanSendMobileNotice.do?EMP_SID={0}'.format(Common.EMP_SID)
        return Utils.Utils().request_orangebank(params, url)

    def corporbank_VerifyImage(self):
        params = {
        }
        url = '/corporbank/VerifyImage'
        return Utils.Utils().request_orangebank_photo(params, url)

    def corporbank_opt(self, mobile):
        params = {
            'mobile': mobile,
        }
        url = '/corporbank/otp.jsp'
        return Utils.Utils().request_orangebank(params, url)

    def netLoanCheckMobile(self, checkCode, mobile, orderid, tranCode, name, idNo, accNo, bankId):
        params = {
            'checkCode': checkCode,
            'mobile': mobile,
            'orderid': orderid,
            'tranCode': tranCode,
            'name': name,
            'idNo': idNo,
            'accNo': accNo,
            'bankId': bankId
        }
        url = '/corporbank/netLoanCheckMobile.do?EMP_SID={0}'.format(Common.EMP_SID)
        return Utils.Utils().request_orangebank(params, url)

    def openSubAcctSubmit(self, bankId, mobile, type, submitTimestamp, accNo, cryptograph, checkCode, newPasswordSure,
                          passwordNew, EMP_SID, NOTIFYURL, returnurl, standardBankName, BankName):
        params = {
            'bankId': bankId,
            'mobile': mobile,
            'type': type,
            'submitTimestamp': submitTimestamp,
            'accNo': accNo,
            'cryptograph': cryptograph,
            'checkCode': checkCode,
            'newPasswordSure': newPasswordSure,
            'passwordNew': passwordNew,
            'EMP_SID': EMP_SID,
            'NOTIFYURL': NOTIFYURL,
            'returnurl': returnurl,
            'standardBankName': standardBankName,
            'BankName': BankName
        }
        url = '/corporbank/openSubAcctSubmit.do'
        return Utils.Utils().request_orangebank(params, url)

    def sendMobileNotice(self, smsTempletId, extContent):
        params = {
            'smsTempletId': smsTempletId,
            'extContent': extContent,
        }
        url = '/corporbank/sendMobileNotice.do?EMP_SID={0}'.format(Common.EMP_SID)
        return Utils.Utils().request_orangebank(params, url)

    def verifyMobileToken(self, checkCode, checkPassword):
        params = {
            'checkCode': checkCode,
            'checkPassword': checkPassword,
        }
        url = '/corporbank/verifyMobileToken.do?EMP_SID={0}'.format(Common.EMP_SID)
        return Utils.Utils().request_orangebank(params, url)

    def accountAccessMac(self, EMP_SID, submitTimestamp, newPassword, returnurl, NOTIFYURL, md5Mobile, FuncCode):
        params = {
            'EMP_SID': EMP_SID,
            'submitTimestamp': submitTimestamp,
            'newPassword': newPassword,
            'returnurl': returnurl,
            'NOTIFYURL': NOTIFYURL,
            'md5Mobile': md5Mobile,
            'FuncCode': FuncCode
        }
        url = '/corporbank/accountAccessMac.do'
        return Utils.Utils().request_orangebank(params, url)

    def callback_return(self, orig, sign, origin):
        params = {
            'orig': orig,
            'sign': sign,
            }
        url = '/mobile/custody/account/callback/return?origin={0}&roleType=1'.format(origin)
        return Utils.Utils().request_call(params, url)

    def pa_config(self):
        params = {
        }
        url = '/mobile/config.json'
        return Utils.Utils().request_pa(params, url)

    def cardList(self):
        params = {
        }
        url = '/mobile/card/cardList.json'
        return Utils.Utils().http_get_request(params, url)

    def center_complete(self, kind):
        params = {
            'kind': kind
        }
        url = '/mobile/member/center/complete.json'
        return Utils.Utils().http_get_request(params, url)

    def question(self):
        params = {
        }
        url = '/assess/app/question'
        return Utils.Utils().http_get_request(params, url)

    def query_all(self):
        params = {
        }
        url = '/assess/question/query/all'
        return Utils.Utils().http_get_request(params, url)

    def submmit(self, optionArr):
        params = {
            'optionArr': optionArr
        }
        url = '/assess/option/submit'
        return Utils.Utils().http_post_request(params, url)

    def tasks_list(self):
        params = {
        }
        url = '/mobile/member/tasks/list.json'
        return Utils.Utils().request_static(params, url, 'get')

    def score_sign(self):
        params = {
        }
        url = '/mobile/my/score/sigin.json'
        return Utils.Utils().http_get_request(params, url)

    def play_list(self):
        params = {
        }
        url = '/mobile/activity/play/list.json'
        return Utils.Utils().http_get_request(params, url)

    def feedback(self, browser, origin, systemVersion, userName, identifier, content, version):
        params = {
            'browser': browser,
            'origin': origin,
            'systemVersion': systemVersion,
            'userName': userName,
            'identifier': identifier,
            'content': content,
            'version': version
        }
        url = '/mobile/others/feedback.json'
        return Utils.Utils().http_post_request(params, url)

    def captcha(self):
        params = {
        }
        url = '/mobile/user/captcha.findPwd.json'
        return Utils.Utils().http_get_request_photo(params, url)

    def findPwd_code(self):
        params = {
        }
        url = '/mobile/user/findPwd/code.json'
        return Utils.Utils().http_get_request(params, url)

    def captcha_be(self):
        params = {
        }
        url = '/captcha.login'
        return Utils.Utils().get_photo_be(params, url)

    def login_be_first(self):
        params = {
        }
        url = '/login'
        return Utils.Utils().request_be(params, url, 'get')

    def login_be(self, loginId, password, captchaCode, tokenName, tokenValue):
        params = {
            'loginId': loginId,
            'password':password,
            'captchaCode':captchaCode,
            'tokenName':tokenName,
            'tokenValue':tokenValue
        }
        url = '/login'
        return Utils.Utils().request_be(params, url, 'post')

    def auth_apply(self, invest, origin, repay, transfer):
        params = {
            'invest': invest,
            'origin': origin,
            'repay': repay,
            'transfer': transfer
        }
        url = '/mobile/custody/auth/apply.json'
        return Utils.Utils().request_static(params, url, 'get')

    def recharge_be(self, user, money):
        params = {
            'user': user,
            'money': money
        }
        url = '/custody/add/money/{0}/{1}'.format(user, money)
        return Utils.Utils().request_be(params, url, 'get')

    def add_coupon(self, couponId, mobile):
        params = {
            'couponId': couponId,
            'mobile': mobile
        }
        url = '/coupon/record/add'
        return Utils.Utils().request_be(params, url, 'post')

    def send_coupon(self, id):
        params = {
            'id': id
        }
        url = '/coupon/record/send'
        return Utils.Utils().request_be(params, url, 'post')

    def list_coupon(self, rows, page, sord, mobile):
        params = {
            'rows': rows,
            'page': page,
            'sord': sord,
            'mobile': mobile
        }
        url = '/coupon/record/list.json'
        return Utils.Utils().request_be(params, url, 'get')






