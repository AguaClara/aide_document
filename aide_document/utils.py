"""
General purpose utility library..
"""

import json
from aide_document.json_error import JsonError, JsonKeyError 

#read_json(json_key,json_string) is a function that 
#takes in a json_key and the json_string and returns
#the value(s) associated with that key. Assumes
#json_string follows format where each key has a number
#or a values and units attribute associated with it. If 
#not, then failure is raised.
def read_json(json_key, json_string):
    try:
        parsed_json = json.loads(json_string)
    except JSONDecodeError as err:
        print("invalid json:")
        print(json_string)
        raise

    #Checks if there is a float or int associated with the key. This condition
    #is only satisfied if the key has a number associated with it.
    if isinstance(parsed_json[json_key], float) or isinstance(parsed_json[json_key], int):
        return str(parsed_json[json_key])
    #Checks if there is a value attribute and units attribute associated 
    #with the key. 
    elif 'value' in parsed_json[json_key] and 'units' in parsed_json[json_key]:
        return str(parsed_json[json_key]['value']) + ' ' + parsed_json[json_key]['units']
    else:
        raise JsonKeyError(json_key, json.dumps(parsed_json[json_key], sort_keys=False, indent=4, separators=(',', ': ')))


###add error handling here instead of in json_to_latex.py
