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


pprint(doc)