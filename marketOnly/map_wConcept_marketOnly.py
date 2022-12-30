# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author: UmeAI
@Blog(个人博客地址): https://www.umeai.top
@File:map_wConcept_marketOnly.py
@Time:2022/12/28 22:28
@todo:
@fixme:
@important:
"""
page = 12
tmp_Concept_Product = set()
tmp_Concept_Product_property_meta = set()
tmp_value_id = set()

s = []
p = []
o = []
all_spos = []
with open("./AliOpenKG_ABox_Part4/AliOpenKG_ABox_Product_OriginStr_wConcept_marketOnly_part{}.ttl".format(page),
          # all line 28361069
          'r', encoding='utf-8') as fp:
    for line in fp:
        if line.startswith('@'):
            continue
        if line == '\n':
            spos_each_S = []
            continue
        if line[0] == '<':
            # '<http://ali.openkg.cn/alischema#Market_segment/tag_df0be6ab6e90ab9b88cb400cbaa205d6_instance8918>'
            a = line
            if 'Market_segment' in line:
                continue
            line = line.strip().replace('<', '').replace('>', '')
            tmp = line.split('#')[1].split('/')

            tmp_Concept_Product.add(tmp[0])  # Concept Product with many meta property

            concept_product_ins_pid = tmp[1]  # one instance of concept Product
            s.append(concept_product_ins_pid)
        if line[8] == 'a':
            continue
        if line[8] == '<':
            a = line
            line = line.strip().replace('<', '').replace('>', '')
            tmp = line.split('#')[1].split('/')

            tmp_Concept_Product_property_meta.add(tmp[0])

            concept_product_ins_property_name = tmp[1]
            p.append(concept_product_ins_property_name)

        if line[16] == '<':
            a = line
            line = line.strip()[:-1]
            if ',' in line:
                value_ids = line.split(',')
                for _ in value_ids:
                    _ = _.replace('<', '').replace('>', '')
                    meta_property_value_id = _.split('/')[-1].strip()

                    tmp_value_id.add(meta_property_value_id[:4])

                    o.append(meta_property_value_id)
                    all_spos.append(
                        (concept_product_ins_pid, concept_product_ins_property_name, meta_property_value_id))
            else:
                line = line.strip()[:-1]
                meta_property_value_id = line.split('/')[-1].strip()

                tmp_value_id.add(meta_property_value_id[:4])

                all_spos.append(
                    (concept_product_ins_pid, concept_product_ins_property_name, meta_property_value_id))

# todo save pick
# with open(r'F:\KgData\AliOpenKG_ABox_Part2\marketOnly_part2-spo.pick', 'wb') as f:
#     pickle.dump(all_spos, f)

# todo save csv
import pandas as pd

s = []
p = []
o = []
for spo in all_spos:
    s.append(spo[0])
    p.append(spo[1])
    o.append(spo[2])

dataframe = pd.DataFrame(
    {'concept_product:ID': s, 'concept_product_property_name': p, 'concept_product_property_value:ID': o})
dataframe.to_csv("./AliOpenKG_ABox_Part4/marketOnly_part{}-spo.csv".format(page), index=False, sep=',')
