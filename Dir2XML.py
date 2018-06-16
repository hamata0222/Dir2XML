# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os
import sys
import re

# Define constants
tag_group='group'
tag_name='name'
tag_file='file'

# Main function
def main():
    if len(sys.argv) < 2:
        print('Please input the directory path which is as root: ')
        root_path = sys.stdin.readline().rstrip()
    else:
        root_path = sys.argv[1]

    root = ET.Element('root')

    print('Converting Directories to XML...')
    
    ele_curr = root
    for path, directories, files in os.walk(root_path):
        group_path = re.sub('^\\' + os.path.sep, '', path.replace(root_path, ''))
        if group_path != '':
            # the root path has no name, so skipped.
            ele_curr = find_named_element(root, group_path)
        for dir in directories:
            ele_curr.append(create_new_group(dir))
        for file in files:
            # This statement is specified for my tool.
            # $PROJ_DIR$ is context root for my tool.
            ele_curr.append(create_new_file(os.path.join('$PROJ_DIR$', group_path, file)))
    
    print('Convertion Completed!')
    
    output_file_name = os.path.join(root_path, 'result.xml')
    print('Output File : %s' %(output_file_name))
    output_to_file(root, output_file_name)

# Define functions
def find_named_element(ele, name):
    name_list = name.split(os.path.sep)
    ele_curr = ele
    for target in name_list:
        ele_pre = ele_curr
        for group in ele_curr.findall(tag_group):
            ele_name = group.find(tag_name)
            if ele_name.text == target:
                ele_curr = group
                break
        if ele_curr is ele_pre:
            ele_new = create_new_group(target)
            ele_curr.append(ele_new)
            ele_curr = ele_new

    return ele_curr

def create_new_element(name, tag):
    ele = ET.Element(tag)
    ele_name = ET.SubElement(ele, tag_name)
    ele_name.text = name
    
    return ele

def create_new_group(name):
    return create_new_element(name, tag_group)

def create_new_file(name):
    return create_new_element(name, tag_file)

def output_to_file(element, file_name):
    fp = open(file_name, 'w')
    fp.write(ET.tostring(element, 'unicode'))

main()
