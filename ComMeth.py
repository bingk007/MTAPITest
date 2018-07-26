#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing

import Service
import time
import Common
import Utils
import ocr_generalocr
import re


def getToken():
    try:
        time.sleep(1)
        response = Service.Service().getToken()
        token = [response['data']['tokenName'], response['data']['tokenValue']]
        return token
    except Exception as ex:
        raise ex


def getCalendar():
    try:
        # time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        time_str = time.strftime('%Y-%m-01', time.localtime(time.time()))
        return time_str
    except Exception as ex:
        raise ex


def login(mobile):
    try:
        response = Service.Service().login(Common.LoginPwd, 66666, mobile)
        tokenName = response['data']['userLoginInfo']['tokenName']
        tokenValue = response['data']['userLoginInfo']['tokenValue']
        authorization = response['data']['authorization']
        Utils.Utils.headers['Authorization'] = authorization
        Utils.Utils.cookies['tokenName'] = tokenName
        Utils.Utils.cookies['tokenValue'] = tokenValue
    except Exception as ex:
        raise ex


def captcha(image):
    try:
        response = Service.Service().captcha()
        with open(image, 'wb') as file:
            file.write(response)
        return ''.join(list(filter(str.isalnum, ocr_generalocr.ocr(image))))
    except Exception as ex:
        raise ex


def corporbank_image():
    try:
        response = Service.Service().corporbank_VerifyImage()
        time.sleep(1)
        with open('./upload/picturePA.jpg', 'wb') as file:
            file.write(response)
        return ''.join(list(filter(str.isalnum, ocr_generalocr.ocr('./upload/picturePA.jpg'))))
    except Exception as ex:
        raise ex


def captcha_be(image):
    try:
        response = Service.Service().captcha_be()
        with open(image, 'wb') as file:
            file.write(response)
        return ''.join(list(filter(str.isalnum, ocr_generalocr.ocr(image))))
    except Exception as ex:
        raise ex


def login_be():
    try:
        for i in range(5):
            responseA = Service.Service().login_be_first()
            tokenName = re.compile('name="tokenName" value="(.+?)"').search(responseA).group(1)
            tokenValue = re.compile('name="tokenValue" value="(.+?)"').search(responseA).group(1)
            responseB = Service.Service().login_be(
                'admin', Common.LoginPwd_BE, captcha_be('./upload/pictureBE.jpg'), tokenName, tokenValue)
            if responseB.find('"status":1,') != -1:
                break
            time.sleep(5)
    except Exception as ex:
        raise ex
