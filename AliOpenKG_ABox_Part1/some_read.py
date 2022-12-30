# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:UmeAI
@Blog: https://www.umeai.top/
@File:some_read.py
@Time:2022/12/27 22:52
@ReadMe: 
"""
# with open('prt_entity.csv', 'r', encoding='utf-8') as f:
#     for idx, _ in enumerate(f):
#         pass

import json

with open('../AliOpenKG_TBox/AliOpenKG_TBox_All_OriginStr.json', 'r', encoding='utf-8') as f:
    a = json.load(f)
