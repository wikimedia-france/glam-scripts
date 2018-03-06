#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import re
csv_input = "resources/Datathon-AN-10mars2018/persons.csv"
csv_query = "resources/Datathon-AN-10mars2018/query.csv"

pattern = re.compile("http:\/\/catalogue\.bnf\.fr\/ark:\/12148\/cb(?P<BNFid>\d{7,8}[0-9bcdfghjkmnpqrstvwxz])")

bnfids = {}
with open(csv_query, 'r') as csv_query_file:
    reader = csv.DictReader(csv_query_file, delimiter=',')
    for line in reader:
        print(line)
        bnfid = line['bnf']
        bnfids[bnfid] = {
            'qid': line['human'].split('/')[-1],
            'name': line['humanLabel']
        }


with open(csv_input, 'r') as csv_input_file:
    reader = csv.DictReader(csv_input_file, delimiter='\t')
    for line in reader:
        if line['BnFRecord']:
            if 'http://catalogue.bnf.fr/ark:/12148/cb' in line['BnFRecord']:
                m = re.search(pattern, line['BnFRecord'])
                source_bnf_id = m.group('BNFid')
                if source_bnf_id in bnfids:
                    print('{}\tP3599\t"{}"'.format(
                        bnfids[source_bnf_id]['qid'],
                        line['recordId']
                    ))
