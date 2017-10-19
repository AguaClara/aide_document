
from utils import read_json



file = open('json/data.json','r')

json_string = file.read()

file.close()

read_json("max_coag_dose_conc",json_string)
