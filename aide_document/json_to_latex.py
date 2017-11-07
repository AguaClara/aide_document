
import json
from utils import read_json

in_file = open('json/data.json','r') #add try catch, raise file not found

json_string = in_file.read()

in_file.close()

parsed_json = json.loads(json_string)

out_file = open('latex/header_file.tex', 'w')

prefix = "\\newcommand{\\"
infix = '}{'
suffix = '}\n'

###move error handling to utils.py
for key in parsed_json:
    try:
        value = read_json(key, json_string)
    except:
        print('un-handled json structure, not adding to latex header file')
        print("\"" + key + "\"" + ": " + json.dumps(parsed_json[key], sort_keys=False, 
                        indent=4, separators=(',', ': ')))
    else:
        out_file.write(prefix + key + infix + value + suffix)
out_file.close()
