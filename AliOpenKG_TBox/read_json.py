# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:UmeAI
@Blog: https://www.umeai.top/
@File:read_json.py
@Time:2022/12/28 13:22
@ReadMe: 
"""
import json
import pandas as pd

# all_rels = set()  # {'subClassOf', 'prefLabel', 'subPropertyOf', 'equivalentProperty', 'range', 'label'}
# ontologys = set()  # {'alis:Brand', 'alis:Scene', 'alis:Place_Of_Origin', 'alis:Market_segment', 'alis:Theme', 'alis:Crowd', 'alis:Category', 'alis:Suitable_time'}

entity_ID = []
names = []
labels = []

tt = set()

with open('../AliOpenKG_TBox/AliOpenKG_TBox_All_OriginStr.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    data = data['@graph']
    for i in data:
        # mkeys = list(i.keys())
        # tt.add(mkeys[1])
        # if 'label' not in mkeys:
        #     a = 1
        for idx, (_, v) in enumerate(i.items()):
            if idx == 0:
                entity_ID.append(v)
            if idx == 1:
                names.append(v)
            if idx == 2:
                break
        labels.append('ENTITY')

a = entity_ID[500000:600000]
b = names[500000:600000]
# dataframe = pd.DataFrame({'entity:ID': entity_ID, 'name': names, 'o': labels})
# dataframe.to_csv("concept_entity.csv", index=False, sep=',')
