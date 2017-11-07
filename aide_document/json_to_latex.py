import json
#Must import the read_json function from utils.py
#in order to get the output to be displayed on the 
#latex file
from utils import read_json

in_file = open('json/data.json','r') #add try catch, raise file not found
json_string = in_file.read()
in_file.close()

parsed_json = json.loads(json_string)

#header_file.tex is the latex file that will be written to
out_file = open('latex/header_file.tex', 'w')

#prefix,infix, and suffix, along with the value determined from
#read_json will help write each latex command to out_file
prefix = "\\newcommand{\\"
infix = '}{'
suffix = '}\n'

#move error handling to utils.py
for key in parsed_json:
    try:
        #Calls read_json function from utils.py
        value = read_json(key, json_string)
    except:
    	#Error message
        print('un-handled json structure, not adding to latex header file')
        print("\"" + key + "\"" + ": " + json.dumps(parsed_json[key], sort_keys=False, 
                        indent=4, separators=(',', ': ')))
    else:
    	#Writes the line to the latex file. 
        out_file.write(prefix + key + infix + value + suffix)
out_file.close()
