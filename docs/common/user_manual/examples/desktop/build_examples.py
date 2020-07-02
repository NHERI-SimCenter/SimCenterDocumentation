# Claudio Perez
# Python 3.8

import json, os, shutil
from ruamel_yaml import YAML

#app_name = 'EE-UQ'
#app_name = 'PBE'
#app_name = 'WE-UQ'
app_name = 'quoFEM'
#app_name = 'pelicun'

newline = os.linesep

yaml=YAML(typ='rt')


FILE_VARS = {
    'fem':
        {'OpenSees': ['mainInput','mainPostprocessScript'],
         'OpenSeesPy':['mainInput','parametersFile','mainPostprocessScript'],
         'FEAPpv': []}
}


def make(app_name):
    with open('idx.yml') as file: index = yaml.load(file)

    for ex in index[app_name]:
        # Change heading in .rst file
        with open(app_name +'/'+ ex['id'] + '.rst') as f: lines = f.readlines()
        lines[0] = ex['name']+'\n'
        with open(app_name +'/'+ ex['id'] + '.rst', "w") as f: f.writelines(lines)

        # Create input.json file
        target_dir = app_name +'/src/'+ ex['id']+'/'
        with open(target_dir+'input.json','w+') as input_json:
            json.dump(ex['input'],input_json, indent=4)

        # Populate quo-xx/ dir
        src_dir = ex['srcDir'] + '/'
        for file_var in FILE_VARS['fem'][ex['input']['fem']['program']]:
            if fname := ex['input']['fem'][file_var]:
                try: shutil.copyfile(src_dir+fname, target_dir+fname)
                except Exception as e: print(e)

if __name__ == "__main__":
    make(app_name)
