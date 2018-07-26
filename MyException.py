#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing


class NotMatchException(Exception):

    def __init__(self,ErrorInfo):
        super().__init__(self)
        self.errorinfo=ErrorInfo

    def __str__(self):
        return self.errorinfo
