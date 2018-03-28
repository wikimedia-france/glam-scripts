#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.dom import minidom
from pprint import pprint
import csv


def getNodeText(node):

    nodelist = node.childNodes
    result = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)


file = "resources/ACMComputingClassificationSystemSKOSTaxonomy.xml"
output_file = "resources/ACM2012.csv"

all_concepts = []

with open(file, 'r') as source:
    pprint("Parsing concepts")
    xmldoc = minidom.parse(source)
    concepts = xmldoc.getElementsByTagName("skos:Concept")

    for c in concepts:
        new_concept = {}
        new_concept['id'] = c.getAttribute("rdf:about")[1:]
        children = c.childNodes

        altLabels = []
        for child in children:
            if child.nodeName == "skos:prefLabel":
                new_concept['label'] = getNodeText(child)
            if child.nodeName == "skos:altLabel":
                altLabels.append(getNodeText(child))

        new_concept['description'] = ', '.join(altLabels)

        pprint(new_concept)
        all_concepts.append(new_concept)

pprint("Writing output file")
fieldnames = ['id', 'label', 'description']
with open(output_file, 'w') as csv_output:
    writer = csv.DictWriter(csv_output,
                            fieldnames=fieldnames,
                            delimiter='\t')
    writer.writeheader()

    for row in all_concepts:
        writer.writerow(row)
