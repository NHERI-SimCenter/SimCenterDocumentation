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
        for group in specs.values():
            for key,conf in group.items():
                if "config" in conf:
                    try:
                        matches = list(map( lambda m: m.current_value,
                            jsonpath2.path.Path.parse_str(conf["config"]).match(input)
                        ))
                        if matches:
                            results[file].append(key)
                    except Exception as e:
                        print(conf["config"],e,file=sys.stderr)
                elif "config_paths" in conf:
                    matches = list(map(
                        lambda m: m.current_value,
                        jsonpath2.path.Path.parse_str(conf["config_paths"]).match(input)
                    ))
                    if matches:
                        for cval in conf["config_values"]:
                            if cval in matches:
                                results[file].append(key)
                                break;

    return results

def parse_reqs(items:list,parent,level=0,conf_path=None)->dict:
    output = {}
    for j,item in enumerate(items):
        if "config_paths" in item:
            conf_path = item["config_paths"]
        key = f"{parent}.{j+1}"

        if "items" in item and items:
            output.update(parse_reqs(item["items"],key,level+1,conf_path))
        elif conf_path and "config_values" in item:
            print(f"val: {item['config_values']}, {conf_path}")
            output.update({key: {"config_paths": conf_path,"config_values": item["config_values"]}})
        elif "config" in item:
            output.update({key: {"config": item["config"]}})
    return output



if __name__ == "__main__":
    specs = {}
    reqs = json.load(sys.stdin)
    specs = {
        k: parse_reqs(v["items"],k) for k,v in reqs.items()
    }
    print(specs)
    print(json.dumps(apply_filter(specs,*sys.argv[1:]),indent=4))

