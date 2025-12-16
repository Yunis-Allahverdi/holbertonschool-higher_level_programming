#!/usr/bin/python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    elem = ET.Element('data')
    for key, val in dictionary.items():
        child  = ET.Element(key)
        child.text = str(val)
        elem.append(child)
        
    tree = ET.ElementTree(elem)
    
    with open(filename, 'wb') as w_file:
        tree.write(w_file)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    data_dict = {}
    for elem in root:
        data_dict[elem.tag] = elem.text

    return data_dict
