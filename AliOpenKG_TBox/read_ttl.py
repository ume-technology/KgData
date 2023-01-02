# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author: UmeAI
@Blog(个人博客地址): https://www.umeai.top
@File:read_ttl.py
@Time:2023/1/1 00:22
@todo: 
@fixme: 
@important: 
"""
with open('AliOpenKG_TBox_All_OriginStr.ttl', 'r', encoding='utf-8') as f:
    for idx, i in enumerate(f):
        if idx <= 7 or i == '\n':
            continue
        print(i)
        print(1)
        line = i.strip()
        print(line)
        print(2)
        break

import json

with open('AliOpenKG_TBox_All_OriginStr.json', 'r', encoding='utf-8') as f:
    datattl = json.load(f)['@graph']

owlThing = {
    'rdf:': [],
    'owl:': [],
    'xsd:': [],
    'alis:': [],
    'skos:': [],
    'cns:': [],
    'rdfs:': [],
    'ens:': [],
    'Brand': []
}

for index in range(len(datattl) - 1, -1, -1):
    if 'rdf:' in datattl[index]['@id']:
        owlThing['rdf:'].append(datattl.pop(index))

for index in range(len(datattl) - 1, -1, -1):
    if 'owl:' in datattl[index]['@id']:
        owlThing['owl:'].append(datattl.pop(index))

for index in range(len(datattl) - 1, -1, -1):
    if 'xsd:' in datattl[index]['@id']:
        owlThing['xsd:'].append(datattl.pop(index))

for index in range(len(datattl) - 1, -1, -1):
    if 'alis:' in datattl[index]['@id']:
        owlThing['alis:'].append(datattl.pop(index))

for index in range(len(datattl) - 1, -1, -1):
    if 'skos:' in datattl[index]['@id']:
        owlThing['skos:'].append(datattl.pop(index))

for index in range(len(datattl) - 1, -1, -1):
    if 'cns:' in datattl[index]['@id']:
        owlThing['cns:'].append(datattl.pop(index))

for index in range(len(datattl) - 1, -1, -1):
    if 'rdfs:' in datattl[index]['@id']:
        owlThing['rdfs:'].append(datattl.pop(index))

for index in range(len(datattl) - 1, -1, -1):
    if 'ens:' in datattl[index]['@id']:
        owlThing['ens:'].append(datattl.pop(index))

# {'Suitable_time',
# 'Property',
# 'Category',
# 'Place_Of_Origin',
# 'Theme',
# 'Brand',
# 'Market_segment',
# 'Scene',
# 'Crowd'}
# owlstructure = set()

property_structure = []
for i in range(len(owlThing['alis:']) - 1, -1, -1):
    # owlstructure.add(i['@id'].split(':')[1].split('/')[0])
    if 'alis:Property' in owlThing['alis:'][i]['@id']:
        property_structure.append(owlThing['alis:'].pop(i))
kk_property = []
for i in range(len(property_structure) - 1, -1, -1):
    if len(property_structure[i]) == 4:
        kk_property.append(property_structure.pop(i))
kk_kk_property = []
for i in range(len(kk_property) - 1, -1, -1):
    if 'equivalentProperty' in kk_property[i]:
        kk_kk_property.append(kk_property.pop(i))

category_structure = []
for i in range(len(owlThing['alis:']) - 1, -1, -1):
    # owlstructure.add(i['@id'].split(':')[1].split('/')[0])
    if 'alis:Category' in owlThing['alis:'][i]['@id']:
        category_structure.append(owlThing['alis:'].pop(i))
kk_category = []  # c3 -> lc
for i in range(len(category_structure) - 1, -1, -1):
    if 'alis:Category' in category_structure[i]['subClassOf']:
        kk_category.append(category_structure.pop(i))
kk_kk_category = []  # alis:Category -> c1
for i in range(len(kk_category) - 1, -1, -1):
    if kk_category[i]['subClassOf'] == 'alis:Category':
        kk_kk_category.append(kk_category.pop(i))
kk_kk_kk_category = []  # c1 -> c2
for i in range(len(kk_category) - 1, -1, -1):
    if '/c1_' in kk_category[i]['subClassOf']:
        kk_kk_kk_category.append(kk_category.pop(i))
kk_kk_kk_kk_category = []  # c2 -> c3
for i in range(len(kk_category) - 1, -1, -1):
    if '/c2_' in kk_category[i]['subClassOf']:
        kk_kk_kk_kk_category.append(kk_category.pop(i))

place_Of_Origin_structure = []
for i in range(len(owlThing['alis:']) - 1, -1, -1):
    # owlstructure.add(i['@id'].split(':')[1].split('/')[0])
    if 'alis:Place_Of_Origin' in owlThing['alis:'][i]['@id']:
        place_Of_Origin_structure.append(owlThing['alis:'].pop(i))
kk_k_place_Of_Origin = []
for i in range(len(place_Of_Origin_structure) - 1, -1, -1):
    if len(place_Of_Origin_structure[i]) == 4:
        kk_k_place_Of_Origin.append(place_Of_Origin_structure.pop(i))
kk_kk_place_Of_Origin = []
for i in range(len(place_Of_Origin_structure) - 1, -1, -1):
    if len(place_Of_Origin_structure[i]) != 6:
        kk_kk_place_Of_Origin.append(place_Of_Origin_structure.pop(i))
kk_kk_kk_place_Of_Origin = []
for i in range(len(kk_kk_place_Of_Origin) - 1, -1, -1):
    if 'rdf:type' not in kk_kk_place_Of_Origin[i]:
        kk_kk_kk_place_Of_Origin.append(kk_kk_place_Of_Origin.pop(i))
# for i in range(len(kk_kk_place_Of_Origin) - 1, -1, -1):
#     if 'http://ali.openkg.cn/alischema#Place_Of_Origin/China/' not in kk_kk_place_Of_Origin[i]['rdf:type']:
#         kk_kk_place_Of_Origin.append(kk_kk_place_Of_Origin.pop(i))


market_segment_structure = []
for i in range(len(owlThing['alis:']) - 1, -1, -1):
    # owlstructure.add(i['@id'].split(':')[1].split('/')[0])
    if 'alis:Market_segment' in owlThing['alis:'][i]['@id']:
        market_segment_structure.append(owlThing['alis:'].pop(i))
kkmarket_segment = []
for i in range(len(market_segment_structure) - 1, -1, -1):
    if market_segment_structure[i]['broader'] != 'alis:Market_segment':
        kkmarket_segment.append(market_segment_structure.pop(i))

brand_structure = []
kkbrands = []
for i in range(len(owlThing['alis:']) - 1, -1, -1):
    # owlstructure.add(i['@id'].split(':')[1].split('/')[0])
    if 'alis:Brand' in owlThing['alis:'][i]['@id']:
        brand_structure.append(owlThing['alis:'].pop(i))
for i in range(len(brand_structure) - 1, -1, -1):
    if brand_structure[i]['subClassOf'] != 'alis:Brand':
        kkbrands.append(brand_structure.pop(i))

crowd_structure = []  # with domain 2 range
for i in range(len(owlThing['alis:']) - 1, -1, -1):
    # owlstructure.add(i['@id'].split(':')[1].split('/')[0])
    if 'alis:Crowd' in owlThing['alis:'][i]['@id']:
        crowd_structure.append(owlThing['alis:'].pop(i))
kk_crowd = []  # tag_ -> c3_crowd
for index in range(len(crowd_structure) - 1, -1, -1):
    if 'tag_' in crowd_structure[index]['@id']:
        kk_crowd.append(crowd_structure.pop(index))
kk_kk_crowd = []  # tag_ -> c2_crowd
for index in range(len(kk_crowd) - 1, -1, -1):
    if 'c2_' in kk_crowd[index]['broader']:
        kk_kk_crowd.append(kk_crowd.pop(index))
kk_kk_kk_crowd = []  # tag_ -> c1_crowd
for index in range(len(kk_crowd) - 1, -1, -1):
    if 'c1_' in kk_crowd[index]['broader']:
        kk_kk_kk_crowd.append(kk_crowd.pop(index))

theme_structure = []  # with domain 2 range
for i in range(len(owlThing['alis:']) - 1, -1, -1):
    # owlstructure.add(i['@id'].split(':')[1].split('/')[0])
    if 'alis:Theme' in owlThing['alis:'][i]['@id']:
        theme_structure.append(owlThing['alis:'].pop(i))
kk_theme = []  # tag theme ->  c1_主题
for index in range(len(theme_structure) - 1, -1, -1):
    if 'c1_主题' in theme_structure[index]['broader']:
        kk_theme.append(theme_structure.pop(index))
kk_kk_theme = []  # c3 -> c2
for index in range(len(theme_structure) - 1, -1, -1):
    if 'c2_主题' in theme_structure[index]['broader']:
        kk_kk_theme.append(theme_structure.pop(index))
kk_kk_kk_theme = []  # c2 --> c1
for index in range(len(kk_theme) - 1, -1, -1):
    if 'tag_' not in kk_theme[index]['@id']:
        kk_kk_kk_theme.append(kk_theme.pop(index))
kk_kk_kk_kk_theme = []  # tag_ -> c3
for index in range(len(theme_structure) - 1, -1, -1):
    if 'tag_' in theme_structure[index]['@id']:
        kk_kk_kk_kk_theme.append(theme_structure.pop(index))

# ===========
suitable_time_structure = []
for i in range(len(owlThing['alis:']) - 1, -1, -1):
    # owlstructure.add(i['@id'].split(':')[1].split('/')[0])
    if 'alis:Suitable_time' in owlThing['alis:'][i]['@id']:
        suitable_time_structure.append(owlThing['alis:'].pop(i))
stsuitable_time = []
for index in range(len(suitable_time_structure) - 1, -1, -1):
    if 'tag_' not in suitable_time_structure[index]['@id']:
        stsuitable_time.append(suitable_time_structure.pop(index))

scene_structure = []  # with domain 2 range    tag_c3scene
for i in range(len(owlThing['alis:']) - 1, -1, -1):
    # owlstructure.add(i['@id'].split(':')[1].split('/')[0])
    if 'alis:Scene' in owlThing['alis:'][i]['@id']:
        scene_structure.append(owlThing['alis:'].pop(i))
kkscene = []
for index in range(len(scene_structure) - 1, -1, -1):
    if 'tag_' not in scene_structure[index]['@id']:
        kkscene.append(scene_structure.pop(index))
kk_kk_scene = []  # c2 -> c3
for index in range(len(kkscene) - 1, -1, -1):
    if 'c2_scene' in kkscene[index]['broader']:
        kk_kk_scene.append(kkscene.pop(index))
kk_kk_kk_scene = []  # c1 -> c2
for index in range(len(kkscene) - 1, -1, -1):
    if 'c1_scene' in kkscene[index]['broader']:
        kk_kk_kk_scene.append(kkscene.pop(index))
tag_c1scene = []
for index in range(len(scene_structure) - 1, -1, -1):
    if 'c1_scene' in scene_structure[index]['broader']:
        tag_c1scene.append(scene_structure.pop(index))
tag_c2scene = []
for index in range(len(scene_structure) - 1, -1, -1):
    if 'c2_scene' in scene_structure[index]['broader']:
        tag_c2scene.append(scene_structure.pop(index))
