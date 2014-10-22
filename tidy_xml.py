#!/usr/bin/env python
import xml.dom.minidom
import sys
#parse input file
parsed = xml.dom.minidom.parse(sys.argv[1])
lines = parsed.toprettyxml(indent=' '*4).split('\n')
# handle empty lines 
print('\n'.join([line for line in lines if line.strip()]))
