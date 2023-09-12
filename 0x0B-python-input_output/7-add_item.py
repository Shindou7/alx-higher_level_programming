#!/usr/bin/python3
"""
adds all arguments to a Python list,
and then save them to a file
"""
import sys
import os.path
import json


save_file = __import__('7-save_to_json_file').save_to_json_file
load_file = __import__('8-load_from_json_file').load_from_json_file

my_contenu = []
if os.path.exists("add_item.json"):
    my_contenu = load_file("add_item.json")

for arg in sys.argv[1:]:
    my_contenu.append(arg)

save_file(my_contenu, "add_item.json")
