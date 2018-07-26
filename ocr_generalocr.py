#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing


import apiutil
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
app_id = '1106928785'
app_key = 'P91kIX69bqUU01tw'


def ocr(image):
    with open(image, 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)

    # print ('----------------------SEND REQ----------------------')
    rsp = ai_obj.getOcrGeneralocr(image_data)

    if rsp['ret'] == 0:
        for i in rsp['data']['item_list']:
            return i['itemstring']
        # print('----------------------API SUCC----------------------')
    else:
        print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
        print('----------------------API FAIL----------------------')
