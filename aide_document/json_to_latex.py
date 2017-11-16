import json
#Must import the read_json function from utils.py
#in order to get the output to be displayed on the 
#latex file

from aide_document.utils import read_json
from aide_document.json_error import JsonError, JsonKeyError

def json_to_latex_header(json_path, header_path):
    try:
        in_file = open(json_path,'r') 
    except IOError:
        print("Could not read file:" + in_file_path)
        raise

    json_string = in_file.read()
    in_file.close()

    parsed_json = json.loads(json_string)

    #write latex commands to header_path file
    
    out_file = open(header_path, 'w')

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
        except JsonKeyError as key_err:
            #Error message
            print('un-handled json structure, not adding to latex header file')
            print(key_err.key + ":")
            print(key_err.value)
            raise
        else:
            #Writes the line to the latex file. 
            out_file.write(prefix + key + infix + value + suffix)
    out_file.close()


if __name__ == '__main__':
    data= 'json/data.json'
    header_file = 'latex/header_file.tex'
    json_to_latex_header(data, header_file)
