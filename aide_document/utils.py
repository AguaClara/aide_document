"""
General purpose utility library..
"""
import json

def read_json(json_key, json_string):
    parsed_json = json.loads(json_string)
    if isinstance(parsed_json[json_key], float) or isinstance(parsed_json[json_key], int):
        return str(parsed_json[json_key])
    elif 'value' in parsed_json[json_key] and 'units' in parsed_json[json_key]:
        return str(parsed_json[json_key]['value']) + ' ' + parsed_json[json_key]['units']
    else:
        raise
