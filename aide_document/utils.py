"""
General purpose utility library..
"""
import json

def read_json(json_key, json_string):
    parsed_json = json.loads(json_string)
    if 'value' in parsed_json[json_key] and 'units' in parsed_json[json_key]:
        print('hello world')
    else:
        print('goodbye world')
