# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:UmeAI
@Blog: https://www.umeai.top/
@File:map_tagid2label.py
@Time:2022/12/28 1:17
@ReadMe: 映射tag label信息；
"""
import json

# with open('../AliOpenKG_TBox/AliOpenKG_TBox_All_OriginStr.json', 'r', encoding='utf-8') as f:
#     for idx, line in enumerate(f):
#         print(line)
#         if idx == 30:
#             break
#     data = f.read()
#     data = json.loads(data)

# "@id" : "alis:Market_segment/tag_de9dab4a7bbad3754938cd977f371704",
allConcepts = set()
values = []
with open('AliOpenKG_TBox_All_OriginStr.ttl', 'r', encoding='utf-8') as f:
    for line in f:
        if 'lc_724680f3a17a6fb08bc8eb735cc1ec63' in line:
            a = 1
        line = line.strip()
        if line.startswith('@'):
            continue
        if not line.strip():
            tmp = {}
        # if line.startswith('<http://ali.openkg.cn/alischema#'):
        #     t = line.split('#')
        #     t0 = t[0]
        #     t1 = t[1].split('/')[0]
        #     res = t0 + '#' + t1
        #     allConcepts.add(res)

        # todo pass brand / Place_Of_Origin
        if '#Brand/' in line or '#Place_Of_Origin/' in line:  # 暂时不处理品牌和地区信息
            continue
        if 'rdfs:label' in line:
            continue
        if 'rdfs:subClassOf' in line:
            continue

        # concept - Scene
        if line.startswith('<http://ali.openkg.cn/alischema#Scene'):
            concept_and_conceptID = line.split('#')[1].strip()[:-1]  # 概念及概念ID
            tmp['scene-concept-obj'] = concept_and_conceptID.split('/')[1]
        # concept - Crowd
        if line.startswith('<http://ali.openkg.cn/alischema#Crowd'):
            concept_and_conceptID = line.split('#')[1].strip()[:-1]  # 概念及概念ID
            tmp['Crowd-concept-obj'] = concept_and_conceptID.split('/')[1]
        # concept -   Suitable_time
        if line.startswith('<http://ali.openkg.cn/alischema#Suitable_time'):
            concept_and_conceptID = line.split('#')[1].strip()[:-1]  # 概念及概念ID
            tmp['Suitable_time-concept-obj'] = concept_and_conceptID.split('/')[1]
        # concept - Theme
        if line.startswith('<http://ali.openkg.cn/alischema#Theme'):
            concept_and_conceptID = line.split('#')[1].strip()[:-1]  # 概念及概念ID
            tmp['Theme-concept-obj'] = concept_and_conceptID.split('/')[1]
        # concept - Market_segment
        if line.startswith('<http://ali.openkg.cn/alischema#Market_segment'):
            concept_and_conceptID = line.split('#')[1].strip()[:-1]  # 概念及概念ID
            tmp['Market_segment-concept-obj'] = concept_and_conceptID.split('/')[1]

        # other   Category?
        if line.startswith('<http://ali.openkg.cn/alischema#Category'):
            concept_and_conceptID = line.split('#')[1].strip()[:-1]  # 概念及概念ID
            tmp['Category-concept'] = concept_and_conceptID.split('/')[1]
        # other   Property
        if line.startswith('<http://ali.openkg.cn/alischema#Property'):
            pass

        # handler process
        if line.endswith(';'):
            # todo property
            if 'rdfs:label ' in line:
                line = line.strip().split()[1].replace('"', '')
                taglabel = line[:-1].strip()
                tmp['tagLabel'] = taglabel
            elif 'rdfs:subClassOf' in line and 'alischema#Category' in line:
                tmp['subClassOf'] = line.strip().split('#')[1].strip()[:-2]  # concept and its sub cls
            # todo market_segment
            elif 'Market_segment' in line:
                tmp['concept_with_subCls'] = 'Market_segment'
            # todo property
            elif 'Property' in line:
                line = line.strip().split('>')[1].replace('"', '')
                taglabel = line[:-1].strip()
                tmp['tagName'] = taglabel
            else:  # todo 适配：Scene、Suitable_time、Crowd、Theme
                cls_or_subcls_with_concept = line.split('#')[1].strip()[:-1]  # concept and its sub cls
                tmp['concept_with_subCls'] = cls_or_subcls_with_concept
        if line.endswith('.'):
            # todo not category
            if 'alischema#Property' in line:
                r = line.strip().split()[0].split('#')
                t_name = r[0].strip()[:-1].strip()
                t_label = r[0].strip().replace('"', '')[:-1]
                tmp[t_name] = t_label
            else:  # todo category 2 property
                line = line.strip().split()[1].replace('"', '')
                taglabel = line.strip()
                tmp['tagName'] = taglabel
                values.append(tmp)
