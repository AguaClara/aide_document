from sys import version_info
import os

py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2

if py3:
  input_file = input("Please enter the name of the input file, including the extension type \n ")
  output_file = input("Please enter the name of the output file \n ")
else:
  input_file= raw_input("Please enter the name of the input file, including the extension type \n ")
  output_file = raw_input("Please enter the name of the output file \n ")

os.system("pandoc " + input_file + " -o " + output_file + ".pdf" )
