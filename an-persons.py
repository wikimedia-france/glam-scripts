#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import re
csv_input = "resources/Datathon-AN-10mars2018/persons.csv"
csv_query = "resources/Datathon-AN-10mars2018/query.csv"

isni_ids = {}
with open(csv_query, 'r') as csv_query_file:
    reader = csv.DictReader(csv_query_file, delimiter=',')
    for line in reader:
        print(line)
        isni_id = line['isni']
        isni_ids[isni_id] = {
            'qid': line['human'].split('/')[-1],
            'name': line['humanLabel']
        }


with open(csv_input, 'r') as csv_input_file:
    reader = csv.DictReader(csv_input_file, delimiter='\t')
    for line in reader:
        if line['isni']:
            source_isni_id = line['isni'].strip()
            if source_isni_id in isni_ids:
                print('{}\tP3599\t"{}"'.format(
                    isni_ids[source_isni_id]['qid'],
                    line['recordId']
                ))
