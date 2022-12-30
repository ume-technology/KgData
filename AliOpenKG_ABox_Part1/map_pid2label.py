# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:UmeAI
@Blog: https://www.umeai.top/
@File:map_pid2label.py
@Time:2022/12/27 22:37
@ReadMe: 
"""
import pandas as pd

entity_Id = []
names = []
labels = []
with open('Prt_Attributes-spo-stan.csv', 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx == 0:
            continue
        if line.split(',')[1] == 'label' and line.split(',')[0].startswith('tag'):
            pid = line.split(',')[0]
            name = line.split(',')[2]
            entity_Id.append(pid)
            names.append(name)
            labels.append('ENTITY')
        # if idx == 1000:
        #     break

# dataframe = pd.DataFrame({'entity:ID': entity_Id, 'name': names, 'o': labels})
# dataframe.to_csv("prt_entity.csv", index=False, sep=',')
