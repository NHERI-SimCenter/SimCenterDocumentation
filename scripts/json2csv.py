import os, sys, re, json
from dataclasses import dataclass
import jsonpath2

EXENAME = "json2csv.py"

EXAMPLE_DIRS = {
    "qfem": "qfem-[0-9]{4}",
    "eeuq": "eeuq-[0-9]{4}",
    "weuq": "weuq-[0-9]{4}",
    "pbdl": "pbdl-[0-9]{4}",
    "r2dt": "E[0-9].*",
    "hdro": "hdro-[0-9]{4}",
}

def print_help():
    print(f"""
usage: {EXENAME} [OPTIONS]... < INPUT

Example:
\t./{EXENAME} \\
    -Eqfem ~/quoFEM/Examples/*/src/input.json
    < Requirements.json > Requirements.csv
""")


def apply_filter(specs:dict, *files)->dict:
    results = {}
    for file in files:
        results[file] = []
        try:
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
        except Exception as e:
            print(file,e,file=sys.stderr)
    return results


def proc_reqs(items:list, parent, level:int=0, conf_path:str=None)->dict:
    output = {}
    for j,item in enumerate(items):
        if "config_paths" in item:
            conf_path = item["config_paths"]
        key = f"{parent}.{j+1}"

        if "items" in item and item["items"]:
            output.update(proc_reqs(item["items"],key,level+1,conf_path))
        elif conf_path and "config_values" in item:
            output.update({
                key: {"config_paths": conf_path,"config_values": item["config_values"]}
            })
        elif "config" in item:
            output.update({key: {"config": item["config"]}})
    return output

def find_first(key:str, dct:dict):
    for k,v in dct.items():
        if key in v:
            return k
    return None

def create_link(v:str,app:str=None)->str:
    if v and app is None:
        if v[:4] == "http":
            return f'`link <{v}>`_'
        else:
            return v
    elif v and EXAMPLE_DIRS[app] is not None:
        match = re.search(f"({EXAMPLE_DIRS[app]})",v)
        return f'":{match.group(0)}:`/`"' if match else '_'
    else:
        return '_'

def find_implementation(key:str,item:dict, examples:dict, options=None)->list:
    if "implementation" in item:
        if isinstance(item["implementation"],str):
            if item["implementation"] == "core" or item["implementation"] == "standard":
                return {
                    #app: "**core**" if v else "NA" for app,v in examples.items()
                    app: "**core**" if examples[app] else '_' for app in EXAMPLE_DIRS.keys()
                }
        else:
            implementations = {
               k: item["implementation"][k] if k in item["implementation"] else  '_'
               for k in EXAMPLE_DIRS.keys()
            }
            return {
                k: f'"{create_link(v)}"'
                    for k,v in implementations.items()
            }
    else:
        return {app: create_link(find_first(key,examples[app]),app) if examples[app] else "_"
                for app in EXAMPLE_DIRS.keys()}


def print_reqs(items:list,parent,level:int,examples:dict,options=None)->dict:
    """Print requirements in CSV format"""
    options = options or Options()
    for j,item in enumerate(items):
        if not item["target"]:
            continue
        if "apps" in item:
            examples = {
                app: v if app in item["apps"] else False
                for app,v in examples.items()
            }

        key = f"{parent}.{j+1}"
        if "items" in item and item["items"]:
            field_template = '"**{}**"'
            print(", ".join(
                map(field_template.format,
                    [key, item["target"], "_", "_", "_"] + ["_"]*len(EXAMPLE_DIRS)
            )), file=options.file)
            print_reqs(item["items"],key,level+1,examples,options)

        else:
            fields = [f'"{f}"' if f else '_' for f in item["fields"]]
            refs = list(find_implementation(key, item, examples,options).values())
            print(f'"{key}", "{item["target"]}",' + ", ".join(fields + refs),
                    file=options.file
            )



@dataclass
class Options:
    field_template:str = '"{}"'
    file = sys.stdout

if __name__ == "__main__":
    argnum = 1
    apps = {}
    argc = len(sys.argv)
    options = Options()
    verbose = False
    while argnum < argc:
        arg = sys.argv[argnum]
        if sys.argv[argnum][:2] == "-E":
            apps.update({arg[2:]: []})
            argnum += 1
            expl_input = sys.argv[argnum]
            while expl_input[0] != "-":
                apps[arg[2:]].append(expl_input)
                argnum += 1
                if argnum == argc: break
                expl_input = sys.argv[argnum]
            if expl_input == "-": argnum += 1
        elif sys.argv[argnum] == "-v":
            verbose=True
            argnum += 1
        else:
            break

    if verbose: print(f"apps: {list(apps.keys())}",file=sys.stderr)
    reqs = json.load(sys.stdin)
    specs = {
        k: proc_reqs(v["items"],k,
            conf_path=v["config_paths"] if "config_paths" in v else None)
        for k,v in reqs.items()
    }
    apps_included = {k: True for k in apps}
    filtered_examples = {
        app: apply_filter(specs,*apps[app]) for app in apps
    }
    for k,item in reqs.items():

        if "apps" in item:
            examples = {
                app: v if app in item["apps"] else False
                    for app,v in filtered_examples.items()
            }
        else:
            examples = filtered_examples

        print_reqs(item["items"],k,0,examples,options)


