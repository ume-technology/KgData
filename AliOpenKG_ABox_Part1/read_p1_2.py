# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:UmeAI
@Blog: https://www.umeai.top/
@File:read_p1_2.py
@Time:2022/12/27 18:43
@ReadMe: 修正 p1 存储的数据； 得到所有产品的标准label信息
"""
import pandas as pd

s = []
p = []
o = []

with open('Prt_Attributes-spo.csv', 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx == 0:
            continue
        s.append(line.split(',')[0])
        tp = line.split(',')[1]
        if 'rdf-schema#' in tp:
            tp = tp.replace('rdf-schema#', '')
        p.append(tp)
        to = line.split(',')[2].strip()
        if '"' in to:
            to = to.replace('"', '')
        o.append(to)

dataframe = pd.DataFrame({'s': s, 'p': p, 'o': o})
dataframe.to_csv("Prt_Attributes-spo-stan.csv", index=False, sep=',')
