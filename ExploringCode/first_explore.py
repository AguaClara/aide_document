import json

json_string={"width": 5}

file = open(“testfile.tx”,”w”) 
parsed_json = json.loads(json_string)
width=parsed_json["width"]

file.write(“\\newcommand{\\width}{The width of the plant is"  + width +"}")
 
file.close() 