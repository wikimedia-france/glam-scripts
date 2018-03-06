#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

csv_input = "resources/Datathon-AN-10mars2018/persons.csv"
csv_output = "resources/Datathon-AN-10mars2018/persons_output.csv"

with open(csv_output, 'w') as csv_output_file:
    fieldnames = [
        'id',
        'label',
        'description']
    writer = csv.DictWriter(csv_output_file, fieldnames=fieldnames)
    writer.writeheader()

    with open(csv_input, 'r') as csv_input_file:
        reader = csv.DictReader(csv_input_file, delimiter='\t')
        for line in reader:
            newline = {}
            newline['id'] = line['recordId']
            newline['description'] = line['description_or_functions']
            name_parts = line['standardizedNameForm'].split('(')[0].split(', ')
            if len(name_parts) > 1:
                newline['label'] = "{} {}".format(
                    name_parts[1].strip(),
                    name_parts[0].strip()
                )
            else:
                newline['label'] = name_parts[0]

            writer.writerow(newline)
