#!/home/claudio/miniconda3/envs/simdoc/bin/python

import os, sys, re, json
import jsonpath2

EXENAME = "filter"
def print_help():
    print(f"usage: {EXENAME} [OPTIONS]... SPEC[:ID..] FILES...")

def apply_filter(specs:dict, *files):
    results = {}
    for file in files:
        results[file] = []
        with open(file,"r") as f:
            input = json.load(f)
        for key,pointer in specs.items():
            print(key,pointer)
            matches = list(map(
                lambda m: m.current_value,
                jsonpath2.path.Path.parse_str(pointer).match(input)
            ))
            if matches:
                results[file].append(key)
    return results



if __name__ == "__main__":
    specs = {}
    for line in sys.stdin:
        key, val = line.strip().split(",",1)
        val = None if val == "(null)" or not val else val
        if val:
            specs.update({key.strip(): val.strip()})

    print(apply_filter(specs,*sys.argv[1:]))

