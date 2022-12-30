# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:UmeAI
@Blog: https://www.umeai.top/
@File:read_p1.py
@Time:2022/12/27 17:39
@ReadMe: 
"""

all_spos = []

with open('AliOpenKG_ABox_Product_OriginStr_Attributes.nt', 'r', encoding='utf-8') as f:
    for line in f:
        s = line.split()[0]
        s = s.split('#')[1].split('/')[1][:-1]

        p = line.split()[1]
        p = p.split('/')[-1][:-1]

        o = line.split()[2]
        all_spos.append((s, p, o))

import pandas as pd

s = []
p = []
o = []
for spo in all_spos:
    s.append(spo[0])
    p.append(spo[1])
    o.append(spo[2])

dataframe = pd.DataFrame({'s': s, 'p': p, 'o': o})
dataframe.to_csv("Prt_Attributes-spo.csv", index=False, sep=',')
