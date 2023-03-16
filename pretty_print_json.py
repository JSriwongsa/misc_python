#!/usr/bin/env python3
# this will pretty print a json file

import sys
import json

json_filepath = sys.argv[1]

with open(json_filepath, 'r') as f:
    json_object = json.load(f)
    print(json.dumps(json_object, indent=4))
