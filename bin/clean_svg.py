#!/usr/bin/env python3

import argparse
import xmltodict


from pprint import pprint
from dumper import dump


parser = argparse.ArgumentParser(description='Cleanup an svg')
parser.add_argument('svgname', type=str, help='svg')


args = parser.parse_args()
svgname = args.svgname


with open(svgname) as fd:
    doc = xmltodict.parse(fd.read())


def clean_element(node):
    if isinstance(node, str):
        return node
    elif isinstance(node, dict):
        clean_node = {}
        for item in node:
            itemname = item
            clean_node[itemname] = clean_element(node[item])
        return clean_node
    elif isinstance(node, list):   
        clean_node = []
        for item in node:
            clean_node.append(clean_element(item))
        return clean_node

svg = clean_element(doc)

doc2 = xmltodict.unparse(svg)
print(doc2)
