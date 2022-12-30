# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:UmeAI
@Blog: https://www.umeai.top/
@File:read_nt.py
@Time:2022/12/28 14:27
@ReadMe: 
"""
import rdflib

# others = set()
key_stand = set()  # with # split
keys_stand_value = ['Suitable_time', 'Market_segment', 'Category', 'Theme', 'Scene', 'Crowd', 'Property', 'Brand',
                    'Place_Of_Origin']  # important: standard Concept - meta property data - instance(obj)
# standard_concept_dict = {}
# for i in keys_stand_value:
#     if i == 'Category' or i == 'Theme' or i == 'Suitable_time' or i == 'Crowd' or i == 'Property' or i == 'Scene' or i == 'Place_Of_Origin':
#         continue
#     standard_concept_dict[i] = []
brands = set()
category_structure = {}
themeID_structure = {}
suitTime_structure = {}
scene_structure = {}
crowd_structure = {}
market_segment_structure = {}
ontology_structure = {}
# ==============================================================================================
# keys = set()  # not # split
# keys_value = [
#     'eligibleRegion', 'Course', 'byArtist', 'Menu', 'GenderType', 'isVariantOf', 'height', 'instrument', 'fatContent',
#     'copyrightYear', 'Brand', 'currency', 'mainContentOfPage', 'Photograph', 'contentSize', 'option', 'givenName',
#     'nutrition', 'containsPlace', 'width', 'category', 'Time', 'Service', 'Person', 'Festival', 'ControlAction',
#     'Quantity', 'driveWheelConfiguration', 'Place', 'Event', 'additionalType', 'ActivateAction', 'material',
#     'accessMode', 'naics', 'Series', 'areaServed', 'CreativeWork', 'Product', 'model', 'itemListElement',
#     'AutoPartsStore', 'amenityFeature', 'device', 'SpreadsheetDigitalDocument', 'broadcastServiceTier', 'cargoVolume',
#     'operatingSystem', 'aircraft', 'description', 'depth', 'featureList', 'MapCategoryType', 'numberOfPages',
#     'Duration', 'Electrician', 'Mass', 'numberOfPlayers', 'value', 'valueMaxLength', 'starRating', 'videoFrameSize',
#     'Action', 'Distance', 'datasetTimeInterval', 'SeaBodyOfWater', 'VideoGame', 'numberOfForwardGears', 'duration',
#     'location', 'course', 'serviceType', 'applicationCategory', 'language', 'sport', 'genre', 'itemCondition', 'query',
#     'produces', 'image', 'audio', 'recordedAs', 'Role', 'Country', 'recipeCuisine', 'position', 'video',
#     'proteinContent', 'HousePainter', 'version', 'StructuredValue', 'color', 'Mountain', 'educationalUse', 'Game',
#     'Season', 'accessibilityFeature', 'Article', 'Energy', 'Car', 'Ticket', 'carrierRequirements', 'GeoShape'
# ]
# other_concept_dict = {}
# for i in keys_value:
#     other_concept_dict[i] = []

with open('AliOpenKG_TBox_All_OriginStr.nt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()[:-1]
        tmp_res_Li = line.split()
        s_seq = tmp_res_Li[0]
        label_seq = tmp_res_Li[1]
        concept_instance_seq = tmp_res_Li[2]
        # each ontology structure - Market_segment
        if 'Market_segment' in s_seq and 'prefLabel' in label_seq:
            concept_Instance_id = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[-1]
            concept_instance_name = concept_instance_seq.strip().replace('"', '')
            market_segment_structure[concept_Instance_id] = concept_instance_name
            continue

        # each ontology structure - Suitable_time
        if 'Suitable_time/tag_' in s_seq and 'prefLabel' in label_seq:
            # < http: // ali.openkg.cn / alischema  # Suitable_time/tag_91013838c31e296c3d0ac4bac8b8bbfa> <http://www.w3.org/2004/02/skos/core#prefLabel> "国庆节" .
            concept_Instance_id = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            concept_instance_name = concept_instance_seq.strip().replace('"', '')
            if concept_Instance_id in suitTime_structure:
                suitTime_structure[concept_Instance_id].append({'concept_instance_name': concept_instance_name})
            else:
                suitTime_structure[concept_Instance_id] = [{'concept_instance_name': concept_instance_name}]
            continue
        if 'Suitable_time/tag_' in s_seq and 'broader' in label_seq and 'Concept' not in concept_instance_seq:
            # < http: // ali.openkg.cn / alischema  # Suitable_time/tag_91013838c31e296c3d0ac4bac8b8bbfa> <http://www.w3.org/2004/02/skos/core#broader> <http://ali.openkg.cn/alischema#Suitable_time/c1_shiling---节日> .
            if concept_instance_seq.endswith(
                    'Suitable_time>') or concept_instance_seq == '"Suitable_time"' or concept_instance_seq == '"适用时间"':
                # < http: // ali.openkg.cn / alischema  # Suitable_time/c1_shiling---节气> <http://www.w3.org/2004/02/skos/core#broader> <http://ali.openkg.cn/alischema#Suitable_time> .
                # < http: // ali.openkg.cn / alischema  # Suitable_time> <http://www.w3.org/2004/02/skos/core#broader> <http://www.w3.org/2004/02/skos/core#Concept> .
                # < http: // ali.openkg.cn / alischema  # Suitable_time> <http://www.w3.org/2004/02/skos/core#prefLabel> "适用时间" .
                # < http: // ali.openkg.cn / alischema  # Suitable_time> <http://www.w3.org/2004/02/skos/core#altLabel> "Suitable_time" .
                continue
            concept_Instance_id = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            concept_subCategory = concept_instance_seq.strip().replace('<', '').replace('>', '').split('/')[-1]
            if concept_Instance_id in suitTime_structure:
                suitTime_structure[concept_Instance_id].append({'broader_to': concept_subCategory})
            else:
                suitTime_structure[concept_Instance_id] = [{'broader_to': concept_subCategory}]
            continue

        # each ontology structure - Theme
        if 'Theme/tag_' in s_seq and 'prefLabel' in label_seq:
            # < http: // ali.openkg.cn / alischema  # Theme/tag_b131ac7c53429b91f7bac744ff02a855> <http://www.w3.org/2004/02/skos/core#prefLabel> "陈婷" .
            concept_Instance_id = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            concept_instance_name = concept_instance_seq.strip().replace('"', '')
            if concept_Instance_id in themeID_structure:
                themeID_structure[concept_Instance_id].append({'concept_Instance_name': concept_instance_name})
            else:
                themeID_structure[concept_Instance_id] = [{'concept_Instance_name': concept_instance_name}]
            continue
        if 'Theme/tag_' in s_seq and 'broader' in label_seq:
            # todo theme 只有一级和 theme 有多级的情况：如果是多级theme：结构信息存储在：ontology_structure结构中
            # < http: // ali.openkg.cn / alischema  # Theme/tag_b131ac7c53429b91f7bac744ff02a855> <http://www.w3.org/2004/02/skos/core#broader> <http://ali.openkg.cn/alischema#Theme/c1_主题---明星> .
            concept_Instance_id = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            concept_subCategory = concept_instance_seq.strip().replace('<', '').replace('>', '').split('/')[-1]
            if concept_Instance_id in themeID_structure:
                themeID_structure[concept_Instance_id].append({'broader_from': concept_subCategory})
            else:
                themeID_structure[concept_Instance_id] = [{'broader_from': concept_subCategory}]
            continue
        if 'Theme' in s_seq and '---' in s_seq and 'broader' in label_seq and '---' in concept_instance_seq:
            # < http: // ali.openkg.cn / alischema  # Theme/c3_主题---吸湿发热> <http://www.w3.org/2004/02/skos/core#broader> <http://ali.openkg.cn/alischema#Theme/c2_主题---新科技> .
            concept_Instance_theme_instance_from = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            concept_Instance_theme_instance = \
                concept_instance_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            ontology_structure[concept_Instance_theme_instance_from] = concept_Instance_theme_instance
            continue
        if 'Theme' in s_seq and '---' in s_seq and 'prefLabel' in label_seq:
            # < http: // ali.openkg.cn / alischema  # Theme/c3_主题---吸湿发热> <http://www.w3.org/2004/02/skos/core#prefLabel> "吸湿发热" .
            # concept_Instance_id = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            # concept_instance_name = concept_instance_seq.strip().replace('"', '')
            continue

        # Scene
        if 'Scene/tag_' in s_seq and 'prefLabel' in label_seq:
            # < http: // ali.openkg.cn / alischema  # Scene/tag_ce287156b202f56882110c00c832d9b6> <http://www.w3.org/2004/02/skos/core#prefLabel> "演奏铜管乐器" .
            concept_Instance_id = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            concept_instance_name = concept_instance_seq.strip().replace('"', '')
            if concept_Instance_id in scene_structure:
                scene_structure[concept_Instance_id].append({'concept_Instance_name': concept_instance_name})
            else:
                scene_structure[concept_Instance_id] = [{'concept_Instance_name': concept_instance_name}]
            continue
        if 'Scene/tag_' in s_seq and 'broader' in label_seq and '---' in concept_instance_seq:
            # < http: // ali.openkg.cn / alischema  # Scene/tag_ce287156b202f56882110c00c832d9b6> <http://www.w3.org/2004/02/skos/core#broader> <http://ali.openkg.cn/alischema#Scene/c1_scene---其他> .
            concept_Instance_id = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            concept_subCategory = concept_instance_seq.strip().replace('<', '').replace('>', '').split('/')[-1]
            if concept_Instance_id in scene_structure:
                scene_structure[concept_Instance_id].append({'broader_from': concept_subCategory})
            else:
                scene_structure[concept_Instance_id] = [{'broader_from': concept_subCategory}]
            continue
        if 'Scene' in s_seq and '---' in s_seq and 'broader' in label_seq and '---' in concept_instance_seq:
            # <http://ali.openkg.cn/alischema#Scene/c3_scene---极限运动> <http://www.w3.org/2004/02/skos/core#broader> <http://ali.openkg.cn/alischema#Scene/c2_scene---做运动> .
            concept_Instance_theme_instance_from = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            concept_Instance_theme_instance = \
                concept_instance_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            ontology_structure[concept_Instance_theme_instance_from] = concept_Instance_theme_instance
            continue

        # Crowd
        if 'Crowd/tag_' in s_seq and 'prefLabel' in label_seq:
            # < http: // ali.openkg.cn / alischema  # Crowd/tag_1b0d89a10b594e342d5f227bf6f5c28c> <http://www.w3.org/2004/02/skos/core#prefLabel> "宝马#-#X5(进口)#-#2018款#-#xDrive35i 3.0T 手自一体 典雅型车主" .
            concept_Instance_id = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            concept_instance_name = concept_instance_seq.strip().replace('"', '')
            if concept_Instance_id in crowd_structure:
                crowd_structure[concept_Instance_id].append({'concept_Instance_name': concept_instance_name})
            else:
                crowd_structure[concept_Instance_id] = [{'concept_Instance_name': concept_instance_name}]
            continue
        if 'Crowd/tag_' in s_seq and 'broader' in label_seq and 'Concept' not in concept_instance_seq:
            # < http: // ali.openkg.cn / alischema  # Crowd/tag_1b0d89a10b594e342d5f227bf6f5c28c> <http://www.w3.org/2004/02/skos/core#broader> <http://ali.openkg.cn/alischema#Crowd/c2_crowd---适配车型> .
            # if 'Suitable_time' in concept_instance_seq:
            #     continue
            concept_Instance_id = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            concept_subCategory = concept_instance_seq.strip().replace('<', '').replace('>', '').split('/')[-1]
            if concept_Instance_id in crowd_structure:
                crowd_structure[concept_Instance_id].append({'broader_to': concept_subCategory})
            else:
                crowd_structure[concept_Instance_id] = [{'broader_to': concept_subCategory}]
            continue
        if 'Crowd' in s_seq and 'broader' in label_seq and '---' in concept_instance_seq:
            # < http: // ali.openkg.cn / alischema  # Crowd/c2_crowd---性别> <http://www.w3.org/2004/02/skos/core#broader> <http://ali.openkg.cn/alischema#Crowd/c1_crowd---基本画像> .
            concept_Instance_theme_instance_from = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            concept_Instance_theme_instance = \
                concept_instance_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            ontology_structure[concept_Instance_theme_instance_from] = concept_Instance_theme_instance
            continue

        # Category
        if 'Category' in s_seq and 'label' in label_seq and 'MapCategoryType' not in s_seq and 'applicationCategory' not in s_seq:
            if concept_instance_seq == '"产品类目"':
                continue
            concept_Instance_id = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            concept_instance_name = concept_instance_seq.strip().replace('"', '')
            # (concept_Instance_id, concept_instance_name)
            pass
            if concept_Instance_id in category_structure:
                category_structure[concept_Instance_id].append({'category_label_name': concept_instance_name})
            else:
                category_structure[concept_Instance_id] = [{'category_label_name': concept_instance_name}]
            continue
        if 'Category' in s_seq and 'subClassOf' in label_seq:
            if concept_instance_seq == '<http://www.w3.org/2002/07/owl#Thing>':
                continue
            concept_Instance_id = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            concept_instance_name = \
                concept_instance_seq.strip().replace('<', '').replace('>', '').split('#')[1].split('/')[-1]
            pass
            if concept_Instance_id in category_structure:
                category_structure[concept_Instance_id].append({'subClassOf': concept_instance_name})
            else:
                category_structure[concept_Instance_id] = [{'subClassOf': concept_instance_name}]
            continue
        if 'Category' in s_seq and 'Property' in label_seq and 'subPropertyOf' not in label_seq:
            concept_Instance_id = s_seq.replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            concept_category_meta_property_name = \
                label_seq.strip().replace('<', '').replace('>', '').split('#')[1].split('/')[1]
            concept_instance_name = concept_instance_seq.strip().replace('"', '')
            if concept_category_meta_property_name == 'Color' or concept_category_meta_property_name == 'Publisher_Name':
                continue
            pass
            if concept_Instance_id in category_structure:
                category_structure[concept_Instance_id].append(
                    {concept_category_meta_property_name: concept_instance_name})
            else:
                category_structure[concept_Instance_id] = [
                    {concept_category_meta_property_name: concept_instance_name}]
            continue

        if '#Brand/' in s_seq and 'label' in label_seq:
            concept_instance_name = concept_instance_seq.strip().replace('"', '')
            brands.add(concept_instance_name)
            continue

a = 1
# import pandas as pd
#
# dataframe = pd.DataFrame({'concept_tag:ID': concept_tagIDs, 'concept_tag:NAME': concept_tagLabels, 'label': labels})
# dataframe.to_csv("concept_tags_entity.csv", index=False, sep=',')
