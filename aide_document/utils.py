"""
General purpose utility library..
"""
import json

def read_json(json_key, json_string)
    parsed_json = json.loads(json_string)
    if parsed_json[json_key].hasOwnProperty('value') and parsed_json[json_key].hasOwnProperty('units')
        print 'hello world'
