# aide_document

[![Build Status](https://travis-ci.org/AguaClara/aide_document.svg?branch=master)](https://travis-ci.org/AguaClara/aide_document)
[![codecov.io](https://codecov.io/github/hbetts/orbitalpy/coverage.svg?branch=master)](https://codecov.io/github/AguaClara/aide_document?branch=master)

About this project...
## Overview
The important python, json, and latex files of this project can be found in the aide_document folder. Explanations of these files can be found below or in the files themselves, because they are documented. The high-level explanation of this repository is that the python scripts help convert the json file to a latex header file.  


## Explanations of Files
The two main python files used for converting json to latex are found in the aide_document folder. The files are json_to_latex.py and utils.py. The json file that is used is called data.json, and can be found in the aide_document/json directory. 

json_to_latex.py reads the json file, which is found in the json folder in the same directory. The python script then opens the latex header_file, found in the latex folder in the same directory. Finally, the script iterates through the keys in the json file and calls a helper function in utils.py to create the latex line of code to be added to latex/header_file.tex. 

utils.py contains the read_json function, which is called in json_to_latex.py. The read_json function checks the attributes of the inputted key, and returns the latex line of code to be used in the latex header file that is being created. 

## Design Goals
aide_document/json_to_latex.py should be able to process all json files, no matter what their syntax is. The goal is to make it work recursively, so that more complex json files with nested keys can be inputted. Additionally, making the process of downloading the code and running the python script for the json to latex conversion as simple as possible is a predominant goal. 

## Installation

Installation instructions...

## Usage

Usage instructions...

## Contributing

Read [CONTRIBUTING](CONTRIBUTING.md).
