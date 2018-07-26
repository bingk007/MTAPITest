#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing


import requests
import re
import urllib3
import ssl
import config

ssl._create_default_https_context = ssl._create_unverified_context
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Utils:

    # API请求地址
    Host_URL = 'http://{0}:8080'.format(config.HOST)
    Host_URL_BE = 'http://{0}:7080'.format(config.HOST)
    Host_URL_WX = 'http://{0}wx.test.com'.format(config.HOST_WX)
    Host_URL_STATIC = 'http://{0}static.test.com'.format(config.HOST_WX)
    Host_URL_ORANGE = 'https://my-st1.orangebank.com.cn'
    Host_URL_PA = 'http://183.62.97.141:9004'

    headers = {
        'User-Agent': 'APP-Android-2.8.0',
        'phoneuuid': 'ffffffff-8799-acf6-ffff-ffffc9461618',
        'Authorization': '',
        'version': '2.8.0'
    }

    headers_wx = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.62 Mobile Safari/537.36',
        'phoneuuid': 'wx',
        'Authorization': ''
    }

    headers_call = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.62 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    headers_be = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.62 Safari/537.36'
    }

    headers_orange = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.62 Mobile Safari/537.36'
    }

    cookies = {
        'SESSIONID': '',
        'tokenName': '',
        'tokenValue': ''
    }

    cookies_be = {
        'SESSIONID': ''
    }

    cookies_or = {
        'JSESSIONID': ''
    }

    def http_get_request(self, params, url):
        response = requests.get(self.Host_URL+url, params, headers=self.headers, cookies=self.cookies, timeout=5)
        try:
            if 'SESSIONID' in response.headers['Set-Cookie']:
                SESSIONID = re.compile('SESSIONID=(.+?);path=/;HttpOnly').search(response.headers['Set-Cookie']).group(1)
                self.cookies['SESSIONID'] = SESSIONID
            if response.status_code == 200:
                return response.json()
            else:
                return
        except Exception as e:
            print("httpGet failed, detail is:%s,%s" % (response.text, e))
            return

    def http_post_request(self, params, url):
        response = requests.post(self.Host_URL+url, params, headers=self.headers, cookies=self.cookies, timeout=10)
        try:
            if 'SESSIONID' in response.headers['Set-Cookie']:
                SESSIONID = re.compile('SESSIONID=(.+?);path=/;HttpOnly').search(response.headers['Set-Cookie']).group(1)
                self.cookies['SESSIONID'] = SESSIONID
            if response.status_code == 200:
                return response.json()
            else:
                return
        except Exception as e:
            print("httpPost failed, detail is:%s,%s" % (response.text, e))
            return

    def request_wx(self, params, url, type):
        try:
            if type == 'get':
                response = requests.get(self.Host_URL_WX + url, params, headers=self.headers_wx, cookies=self.cookies, timeout=5)
            elif type == 'post':
                response = requests.post(self.Host_URL_WX + url, params, headers=self.headers_wx, cookies=self.cookies, timeout=5)
            if 'SESSIONID' in response.headers['Set-Cookie']:
                SESSIONID = re.compile('SESSIONID=(.+?);path=/;HttpOnly').search(response.headers['Set-Cookie']).group(1)
                self.cookies['SESSIONID'] = SESSIONID
            if response.status_code == 200:
                return response.json()
            else:
                return
        except Exception as e:
            print("httpPost failed, detail is:%s,%s" % (response.text, e))
            return

    def request_call(self, params, url):
        response = requests.post(self.Host_URL+url, params, headers=self.headers_call, timeout=10)
        try:
            if response.status_code == 200:
                return response.text
            else:
                return
        except Exception as e:
            print("httpPost failed, detail is:%s,%s" % (response.text, e))
            return

    def request_pa(self, params, url):
        response = requests.get(self.Host_URL_PA+url, params, timeout=5)
        try:
            if response.status_code == 200:
                return response.json()
            else:
                return
        except Exception as e:
            print("httpGet failed, detail is:%s,%s" % (response.text, e))
            return

    def request_be(self, params, url, type):
        try:
            if type == 'get':
                response = requests.get(self.Host_URL_BE+url, params, headers=self.headers_be, cookies=self.cookies_be, timeout=5)
            elif type == 'post':
                response = requests.post(self.Host_URL_BE+url, params, headers=self.headers_be, cookies=self.cookies_be, timeout=5)
            if 'Set-Cookie' in response.headers.keys():
                SESSIONID = re.compile('SESSIONID=(.+?);path=/;HttpOnly').search(response.headers['Set-Cookie']).group(1)
                self.cookies_be['SESSIONID'] = SESSIONID
            if response.status_code == 200:
                return response.text
            else:
                return
        except Exception as e:
            print("httpPost failed, detail is:%s,%s" % (response.text, e))
            return

    def request_orangebank(self, params, url):
        try:
            response = requests.post(self.Host_URL_ORANGE + url, params, verify=False, headers=self.headers_orange, cookies=self.cookies_or, timeout=5)
            if 'Set-Cookie' in response.headers.keys():
                JSESSIONID = re.compile('JSESSIONID=(.+?); Path=/;').search(response.headers['Set-Cookie']).group(1)
                self.cookies_or['JSESSIONID'] = JSESSIONID
            if response.status_code == 200:
                return response.text
            else:
                return
        except Exception as e:
            print("httpPost failed, detail is:%s,%s" % (response.text, e))
            return

    def request_orangebank_photo(self, params, url):
        try:
            response = requests.get(self.Host_URL_ORANGE + url, params, verify=False, headers=self.headers_orange, cookies=self.cookies_or, timeout=5)
            if response.status_code == 200:
                return response.content
            else:
                return
        except Exception as e:
            print("httpPost failed, detail is:%s,%s" % (response.text, e))
            return

    def request_static(self, params, url, type):
        try:
            if type == 'get':
                response = requests.get(self.Host_URL_STATIC + url, params, headers=self.headers, cookies=self.cookies, timeout=5)
            elif type == 'post':
                response = requests.post(self.Host_URL_STATIC + url, params, headers=self.headers, cookies=self.cookies, timeout=5)
            if 'SESSIONID' in response.headers['Set-Cookie']:
                SESSIONID = re.compile('SESSIONID=(.+?);path=/;HttpOnly').search(response.headers['Set-Cookie']).group(1)
                self.cookies['SESSIONID'] = SESSIONID
            if response.status_code == 200:
                return response.json()
            else:
                return
        except Exception as e:
            print("httpPost failed, detail is:%s,%s" % (response.text, e))
            return

    def http_get_request_photo(self, params, url):
        response = requests.get(self.Host_URL+url, params, headers=self.headers, cookies=self.cookies, timeout=5)
        try:
            if response.status_code == 200:
                return response.content
            else:
                return
        except Exception as e:
            print("httpGet failed, detail is:%s,%s" % (response.text, e))
            return

    def get_photo_be(self, params, url):
        response = requests.get(self.Host_URL_BE+url, params, headers=self.headers, cookies=self.cookies_be, timeout=5)
        try:
            if response.status_code == 200:
                return response.content
            else:
                return
        except Exception as e:
            print("httpGet failed, detail is:%s,%s" % (response.text, e))
            return