#! This code takes one input YAML file and geneartes one output file within the project folder
#! 1. ABC_Input.yaml: File where we give our input YAML properties
#! 2. ABC_SortedOutput.yaml: File where we get the sorted YAML properties in alphabetical order, comments & decorators | or > are removed when loaded into code.

#! yamlSorter\Scripts\activate
#! python yamlSorter.py
#! 1. python -m venv <Environment Name> #--> To create environment with given Name
#! 2. <Environment Name>\Scripts\activate #--> To start the environment
#! 3. deactivate #--> To stop  the environment

#! Eternal libraries needed for this code are below
#!python -m pip install PyYAML

import yaml

# Function to sort the dictionary recursively
def sort_dict(d):
    if isinstance(d, dict):
        return { k: sort_dict(d[k]) for k in sorted(d) }
    elif isinstance(d, list):
        return [ sort_dict(item) for item in d ]
    else:
        return d

# Read and sort the YAML file
input_file = 'ABC_Input.yaml'
output_file = 'ABC_SortedOutput.yaml'

with open(input_file, 'r') as stream:
    try:
        data = yaml.safe_load(stream)  # Load the YAML content
        sorted_data = sort_dict(data)   # Sort the data recursively

        with open(output_file, 'w') as outfile:
            yaml.dump(sorted_data, outfile, default_flow_style=False)  # Write sorted data to a new file

    except yaml.YAMLError as err:
        print(err)

