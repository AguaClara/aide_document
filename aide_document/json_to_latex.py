
import json
from utils import read_json

in_file = open('json/data.json','r')

json_string = in_file.read()

in_file.close()

parsed_json = json.loads(json_string)

out_file = open('latex/header_file.tex', 'w')

prefix = "\\newcommand{\\"
infix = '}{'
suffix = '}\n'

for key in parsed_json:
    value = read_json(key, json_string)
    out_file.write(prefix + key + infix + value + suffix)

out_file.close()
