# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2025 Leland Stanford Junior University
# Copyright (c) 2016-2025 The Regents of the University of California
#
# This file is part of SimCenterDocumentation.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# You should have received a copy of the BSD 3-Clause License along with
# pelicun. If not, see <http://www.opensource.org/licenses/>.
#
# Contributors:
# Adam Zsarnóczay

import os, sys, json
import shutil
import subprocess
from pathlib import Path
from textwrap import dedent
from zipfile import ZipFile
from copy import deepcopy

import numpy as np
import pandas as pd

import time

start_time = time.time()

def create_cmp_grp_dir(cmp_groups, root, db):

    member_ids = []

    if isinstance(cmp_groups, dict):

        for grp_name, grp_members in cmp_groups.items():

            grp_id = f"{grp_name.split('-')[0].strip()}"

            # create the first-level dirs
            grp_dir = Path(root)/grp_id
            grp_dir.mkdir(parents=True, exist_ok=True)

            # call this function again to add subdirs
            subgrp_ids = create_cmp_grp_dir(grp_members, grp_dir, db=db)

            grp_index_contents = dedent(f'''
            .. _lbl-dldb_damage_{db}_{grp_id.replace(".","_")}

            {"*"*len(grp_name)}
            {grp_name}
            {"*"*len(grp_name)}

            The following models are available:

            .. toctree::
               :maxdepth: 1

            ''')

            for member_id in subgrp_ids:

                grp_index_contents+=f'   {member_id}/index\n'

            grp_index_path = grp_dir/"index.rst"
            with grp_index_path.open("w", encoding="utf-8") as f:
                f.write(grp_index_contents)

            member_ids.append(grp_id)

    else:

        for grp_name in cmp_groups:

            grp_id = f"{grp_name.split('-')[0].strip()}"

            grp_dir = Path(root)/grp_id

            # create group dirs
            grp_dir.mkdir(parents=True, exist_ok=True)

            grp_index_contents = dedent(f'''
            .. _lbl-dldb_damage_{db}_{grp_id.replace(".","_")}

            {"*"*len(grp_name)}
            {grp_name}
            {"*"*len(grp_name)}

            The following models are available:

            ''')

            grp_index_path = grp_dir/"index.rst"
            with grp_index_path.open("w", encoding="utf-8") as f:
                f.write(grp_index_contents)

            member_ids.append(grp_id)

    return member_ids

def generate_damage_docs():

    resource_folder = Path("../../../../DB_DamageAndLoss/DB").resolve()
    backend_pelicun_folder = Path("../../../../SimCenterBackendApplications/modules/performDL/pelicun3").resolve()
    file_prefix = 'damage_DB_'

    # initialize the damage doc folder
    doc_folder = "./damage"

    if os.path.exists(doc_folder):
        shutil.rmtree(doc_folder)

    doc_folder = Path(doc_folder)

    doc_folder.mkdir(parents=True, exist_ok=True)

    # get all the available damage dbs
    damage_dbs = []
    for file in os.listdir(resource_folder):

        filename = Path(file).stem

        if filename.startswith(file_prefix):

            filename = filename[len(file_prefix):]

            if filename not in damage_dbs:

                damage_dbs.append(filename)

    damage_dbs = sorted(damage_dbs)

    # create the main index file
    damage_index_contents = dedent('''\
    .. _lbl-dldb_damage:

    *************
    Damage Models
    *************
    
    The following collections are available in our Damage and Loss DataBase:

    .. toctree::
       :maxdepth: 1

    ''')

    # for each database
    for db in damage_dbs:

        print('Working on ', db)

        # add db to main damage index file
        damage_index_contents += f'   {db}/index\n'

        # create a folder
        (doc_folder/db).mkdir(parents=True, exist_ok=True)

        # check if figures are available
        # create figures in zip files
        # We could recognize if the zip is already there and skip this,
        # but that could lead to issues with the zip not being updated.
        # So, we are just creating a new zip every time to be safe.
        db_zip = Path(f"./temp/{file_prefix}{db}.zip").resolve()
        viz_script = backend_pelicun_folder/'DL_visuals.py'
        db_path = resource_folder/f'{file_prefix}{db}.csv'

        viz_command = ' '.join([
            "python3", str(viz_script), "fragility", str(db_path), 
            "-o",str(db_zip), "-z", "1"])
        print(viz_command)

        try:
            result = subprocess.check_output(viz_command, shell=True, text=True)
            returncode = 0

        except subprocess.CalledProcessError as e:
            result = e.output
            returncode = e.returncode

        print(result)

        if returncode != 0:
            continue

        # check if there is metadata available
        db_json = resource_folder/f"{file_prefix}{db}.json"
        if db_json.is_file():
            with open(db_json, 'r') as f:
                db_meta = json.load(f)
        else:
            db_meta = None

        if db_meta is not None:

            db_general = db_meta.get('_GeneralInformation',{})

            # create the top of the db index file
            db_short_name = db_general.get('ShortName', db)

            db_description = db_general.get('Description',
                f"The following models are available in {db}:"
                )

            db_index_contents = dedent(f'''
            .. _lbl-dldb_damage_{db}

            {"*"*len(db_short_name)}
            {db_short_name}
            {"*"*len(db_short_name)}

            {db_description}

            ''')

            # check if there are component groups defined
            db_cmp_groups = db_general.get('ComponentGroups', None)

            # if yes, create the corresponding directory structure and index files
            if db_cmp_groups is not None:

                db_index_contents += dedent(f'''
                .. toctree::
                   :maxdepth: 1

                ''')

                # create the directory structure and index files
                grp_ids = create_cmp_grp_dir(db_cmp_groups, root=(doc_folder/db), db=db)

                for member_id in grp_ids:
                    db_index_contents+=f'   {member_id}/index\n'               

        else:

            print(f"No metadata available for {db}")

            # create the top of the db index file
            db_index_contents = dedent(f'''\
            .. _lbl-dldb_damage_{db}

            {"*"*len(db)}
            {db}
            {"*"*len(db)}

            The following models are available in {db}:

            ''')

        db_index_path = doc_folder/f"{db}/index.rst"
        with db_index_path.open("w", encoding="utf-8") as f:
            f.write(db_index_contents) 

        # now open the zip file
        with ZipFile(db_zip, 'r') as zipObj:

            # for each component
            for comp in sorted(zipObj.namelist()):

                comp = Path(comp).stem.removesuffix('.html')

                # check where the component belongs
                comp_labels = comp.split('.')
                comp_path = doc_folder/db
                new_path = deepcopy(comp_path)

                c_i = 0
                while new_path.is_dir():

                    comp_path = new_path

                    if c_i>len(comp_labels):
                        break

                    new_path = comp_path/f"{'.'.join(comp_labels[:c_i])}"                    

                    c_i += 1

                grp_index_path = comp_path/"index.rst"

                comp_meta = None
                if db_meta is not None:

                    comp_meta = db_meta.get(comp, None)
                
                with grp_index_path.open("a", encoding="utf-8") as f:

                    # add the component info to the docs

                    if comp_meta is None:
                        comp_contents = dedent(f'''
                        {comp}
                        {"*"*len(comp)}

                        .. raw:: html
                           :file: {comp}.html


                        .. raw:: html

                           <hr>

                        ''')

                    else:

                        comp_contents = dedent(f'''
                        .. raw:: html

                           <p class="dl_comp_name"><b>{comp}</b> | {comp_meta.get("Description", "")}</p> 
                           <div>

                        ''')

                        comp_comments = comp_meta.get("Comments", "").split("\n")

                        for comment_line in comp_comments:

                            if comment_line != "":

                                comp_contents += (
                                    f'| {comment_line}\n'
                                )

                        if 'SuggestedComponentBlockSize' in comp_meta:

                            roundup = comp_meta.get('RoundUpToIntegerQuantity', "False")
                            if roundup == "True":
                                roundup_text = "(round up to integer quantity)"
                            else:
                                roundup_text = ""

                            comp_contents += dedent(f'''
                            
                            Suggested Block Size: {comp_meta['SuggestedComponentBlockSize']} {roundup_text}
                            
                            ''')

                        comp_contents += dedent(f'''

                        .. raw:: html
                           :file: {comp}.html

                        .. raw:: html

                           <hr>
                        ''') 

                        

                    f.write(comp_contents)

                # copy the file from the zip to the db folder
                zipObj.extract(f'{comp}.html', 
                               path=comp_path)

    damage_index_path = doc_folder/"index.rst"
    with damage_index_path.open("w", encoding="utf-8") as f:
        f.write(damage_index_contents)



def generate_repair_docs():

    resource_folder = Path("../../../../DB_DamageAndLoss/DB").resolve()
    backend_pelicun_folder = Path(
        "../../../../SimCenterBackendApplications/modules/performDL/pelicun3").resolve()
    file_prefix = 'loss_repair_DB_'

    # initialize the repair doc folder
    doc_folder = "./repair"

    if os.path.exists(doc_folder):
        shutil.rmtree(doc_folder)

    doc_folder = Path(doc_folder)

    doc_folder.mkdir(parents=True, exist_ok=True)

    # get all the available repair dbs
    repair_dbs = []
    for file in os.listdir(resource_folder):

        filename = Path(file).stem

        if filename.startswith(file_prefix):

            filename = filename[len(file_prefix):]

            if filename not in repair_dbs:

                repair_dbs.append(filename)

    repair_dbs = sorted(repair_dbs)

    # create the main index file
    repair_index_contents = dedent('''\
    .. _lbl-dldb_repair:

    *************************
    Repair Consequence Models
    *************************
    
    The following collections are available in our Damage and Loss DataBase:

    .. toctree::
       :maxdepth: 1

    ''')

    # for each database
    for db in repair_dbs:

        print('Working on ', db)

        # add db to main repair index file
        repair_index_contents += f'   {db}/index\n'

        # create a folder
        (doc_folder/db).mkdir(parents=True, exist_ok=True)

        # check if figures are available
        # create figures in zip files
        # We could recognize if the zip is already there and skip this,
        # but that could lead to issues with the zip not being updated.
        # So, we are just creating a new zip every time to be safe.
        db_zip = Path(f"./temp/{file_prefix}{db}.zip").resolve()
        viz_script = backend_pelicun_folder/'DL_visuals.py'
        db_path = resource_folder/f'{file_prefix}{db}.csv'

        viz_command = ' '.join([
            "python3", str(viz_script), "repair", str(db_path), 
            "-o",str(db_zip), "-z", "1"])
        print(viz_command)

        try:
            result = subprocess.check_output(viz_command, shell=True, text=True)            
            returncode = 0

        except subprocess.CalledProcessError as e:
            result = e.output
            returncode = e.returncode

        print(result)

        if returncode != 0:
            continue

        # check if there is metadata available
        db_json = resource_folder/f"{file_prefix}{db}.json"
        if db_json.is_file():
            with open(db_json, 'r') as f:
                db_meta = json.load(f)
        else:
            db_meta = None

        if db_meta is not None:

            db_general = db_meta.get('_GeneralInformation',{})

            # create the top of the db index file
            db_short_name = db_general.get('ShortName', db)

            db_description = db_general.get('Description',
                f"The following models are available in {db}:"
                )

            db_index_contents = dedent(f'''
            .. _lbl-dldb_repair_{db}

            {"*"*len(db_short_name)}
            {db_short_name}
            {"*"*len(db_short_name)}

            {db_description}

            ''')

            # check if there are component groups defined
            db_cmp_groups = db_general.get('ComponentGroups', None)

            # if yes, create the corresponding directory structure and index files
            if db_cmp_groups is not None:

                db_index_contents += dedent(f'''
                .. toctree::
                   :maxdepth: 1

                ''')

                # create the directory structure and index files
                grp_ids = create_cmp_grp_dir(db_cmp_groups, root=(doc_folder/db), db=db)

                for member_id in grp_ids:
                    db_index_contents+=f'   {member_id}/index\n'               

        else:

            print(f"No metadata available for {db}")

            # create the top of the db index file
            db_index_contents = dedent(f'''\
            .. _lbl-dldb_repair_{db}

            {"*"*len(db)}
            {db}
            {"*"*len(db)}

            The following models are available in {db}:

            ''')

        db_index_path = doc_folder/f"{db}/index.rst"
        with db_index_path.open("w", encoding="utf-8") as f:
            f.write(db_index_contents)

        # now open the zip file
        with ZipFile(db_zip, 'r') as zipObj:

            html_files = [Path(filepath).stem for filepath 
                          in sorted(zipObj.namelist())]

            comp_ids = np.unique(
                [c_id.split('-')[0] for c_id in html_files])

            dv_types = np.unique(
                [c_id.split('-')[1] for c_id in html_files])

            # for each component
            for comp in comp_ids:

                comp_files = []
                for dv_i in dv_types:
                    filename = f"{comp}-{dv_i}"
                    if filename in html_files:
                        comp_files.append(filename)

                # check where the component belongs
                comp_labels = comp.split('.')
                comp_path = doc_folder/db
                new_path = deepcopy(comp_path)

                c_i = 0
                while new_path.is_dir():

                    comp_path = new_path

                    if c_i>len(comp_labels):
                        break

                    new_path = comp_path/f"{'.'.join(comp_labels[:c_i])}"                    

                    c_i += 1

                grp_index_path = comp_path/"index.rst"

                comp_meta = None
                if db_meta is not None:

                    comp_meta = db_meta.get(comp, None)
                
                with grp_index_path.open("a", encoding="utf-8") as f:

                    # add the component info to the docs

                    if comp_meta is None:
                        comp_contents = dedent(f'''
                        {comp}
                        {"*"*len(comp)}

                        ''')

                    else:

                        comp_contents = dedent(f'''

                        .. raw:: html

                           <p class="dl_comp_name"><b>{comp}</b> | {comp_meta.get("Description", "")}</p> 
                           <div>

                        ''')

                        comp_comments = comp_meta.get("Comments", "").split("\n")

                        for comment_line in comp_comments:

                            if comment_line != "":

                                comp_contents += (
                                    f'| {comment_line}\n'
                                )

                        if 'SuggestedComponentBlockSize' in comp_meta:

                            roundup = comp_meta.get('RoundUpToIntegerQuantity', "False")
                            if roundup == "True":
                                roundup_text = "(round up to integer quantity)"
                            else:
                                roundup_text = ""

                            comp_contents += dedent(f'''
                            
                            Suggested Block Size: {comp_meta['SuggestedComponentBlockSize']} {roundup_text}
                            
                            ''')

                    comp_contents += dedent(f'''

                    The following repair consequences are available for this model:

                    ''')

                    for comp_file in comp_files:

                        dv_type = comp_file.split('-')[1]

                        comp_contents += dedent(f'''

                        **{dv_type}**

                        .. raw:: html
                           :file: {comp_file}.html

                        ''')

                        # copy the file from the zip to the db folder
                        zipObj.extract(f'{comp_file}.html', 
                                       path=comp_path)

                    comp_contents += dedent(f'''

                    .. raw:: html

                       <hr>

                    ''')

                    f.write(comp_contents)

    repair_index_path = doc_folder/"index.rst"
    with repair_index_path.open("w", encoding="utf-8") as f:
        f.write(repair_index_contents)

def main(args):

    temp_dir = Path("./temp").resolve()

    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

    temp_dir.mkdir(parents=True, exist_ok=True);

    generate_damage_docs()

    generate_repair_docs()

    shutil.rmtree(temp_dir) 

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':

    main(sys.argv[1:])