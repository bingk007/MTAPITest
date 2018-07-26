#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing

import re
import random
import MyException
import time
import execjs
import datetime

nowTime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')

teleNum = random.choice(['150','137','189'])+''.join(random.choice('0123456789') for i in range(8))
email = ''.join(random.choice('123456789') for i in range(9)) + '@qq.com'
EMP_SID = ''
orderid = ''
# aaa12345
LoginPwd = '58091c3ee5fc04633d39bedf82ca43fd6f821d5b493d60e6ba5cc00e190a911952c782e4e905baa97ab' \
           'd2cc4b9896235a8d043b0e63d54505e6cf9b98111b8359f8129cc1ba91670f8c32f1e4d665d753c835ca' \
           '4817bebfd1303bc6923fdde6c2a4c8eebe10c4df33103778fdd0cff657b2d5c587febdb281bfe8dbf296d620b'
# aa123456
LoginPwd_A = '3a81ce2179a0b340e81aec499c1b1eb24c802a2e3574c117c07b45822e8e134321f4329063fad9d1157' \
             'cf970075769a3dd0e4a43fcc1bcab410ab1b4cd823a3a5f3cc87372722d004d82939d0f9df42f790b80' \
             'fb9bc94cd636b5fc8360c3b0acf9ce7f21f114c5af9fd00cb5e3adc29967b603d40f4b6991d400cbbff5bbaba8'

LoginPwd_B = '55e3c299bae0678723238c1ec479293af9efe04490ec10fce46d8fd44f26e35ab269c541d197bd1b1d404da' \
             '3545efe25256711ef6a00145277b8f04f5dd371d9303c668ddb13bc91ebd139f8f14382cd5663e0127931a64' \
             '682d4a258502b552e7d42191f538f309b35466916ee806e30cd86ed19ac7be4f1580a47163ad69ad6'

TrdePwd = 'CN-SBC7E97F371293682FBF99F3525E229AF758C5C11515B75EA4E7F5981C97DBADE84F7F81188B22BFDF987BDA78' \
          'ECE6F6A962E8DF8A8039E2B4A29354D0253EC68F7738EC4B85E2C5F03E2BC3349C3B2DEDA5480AA8959E340953BA0817' \
          '3CE60F2132226D28B726D02C036D10FF34AF8C829DD257B592B33'

LoginPwd_BE = '9ecc627b6a1a2e8c3490893202c3c9a4bdb0b3b00e5ab550152f00c487af72ea41a02910f21dfaee3af256fba64f2' \
              '566707326302d5b2d31991e9fd023c75a03421dcb6aa7c8c022b67f2d20ffb13e82e2db9ea217d0b3f46b0608cfd27e' \
              '66ffcc85b5916a79b9dc9bc63631f8d0b265c0647582a680a847ac1925862cbd6587'


def search_str(response, regex_list):
    try:
        for i in regex_list:
            re_com = re.compile(i)
            search_str = re_com.search(response)
            if search_str is None:
                raise MyException.NotMatchException("未匹配到预期结果！")
    except Exception as e:
        print("Failed, response is : %s,%s" % (response, e))
        raise e


def make_id():
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    t = time.localtime()[0]
    x = '421381' + '%04d%02d%02d%03d' % (
        random.randint(t - 80, t - 18),
        random.randint(1, 12),
        random.randint(1, 28),
        random.randint(1, 999))
    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]

    return '%s%s' % (x, LAST[y % 11])


def make_card(bankName):
    bank = {'招商银行': ('621485', 16),
            '光大银行': ('622666', 16),
            '中信银行': ('621773', 16),
            '建设银行': ('622700', 19),
            '农业银行': ('622848', 19),
            '工商银行': ('622202', 19),
            '兴业银行': ('622908', 16),
            '邮储银行': ('621098', 19),
            '广发银行': ('622556', 16),
            '交通银行': ('622259', 17),
            '民生银行': ('622620', 16),
            '中国银行': ('621790', 19),
            '平安银行': ('621626', 19)
            }
    cardNO1 = ''.join(random.choice('0123456789') for i in range(bank[bankName][1] - 7))
    cardNO2 = bank[bankName][0] + cardNO1
    c = tuple(cardNO2)
    s1 = 0
    s2 = 0
    for i in range(bank[bankName][1] - 1):
        if i % 2 == 0:
            a = int(c[(bank[bankName][1] - 2) - i]) * 2
            b = tuple(str(a))
            if len(b) == 2:
                s1 = s1 + int(b[0]) + int(b[1])
            else:
                s1 = s1 + a
        else:
            d = int(c[(bank[bankName][1] - 2) - i])
            s2 = s2 + d
    e = tuple(str(s1 + s2))
    f = int(e[len(e) - 1])
    if f == 0:
        n = 0
    else:
        n = 10 - f
    cardNO = cardNO2 + str(n)
    return cardNO


def encryt_word(message):
    f = open("./rsa.js", 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    ctx = execjs.compile(htmlstr)
    return ctx.call('RSAUtils.pwdEncode', message)
