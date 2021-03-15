# Claudio Perez

import json,os
from pathlib import Path

from rendre.__main__ import create_parser
from rendre import rendre
from pyrsync import blockchecksums, rsyncdelta, patchstream

parser = create_parser()

def sync_files(src_dir,dst_dir,config):

    opts = ["--sort", "--no-quotes", "-j" , "<<>>","-s","<<>>"]

    tfname =  "temp.doc.file"
    with open(tfname,"w+") as tf:
        json.dump(config,tf)

    args = parser.parse_args(["-l",tfname,"-vvv","path",*opts,"--",str(src_dir)+"/./%%:doc"])
    files_to_sync:str  = rendre(args,config).strip()
    os.remove(tfname)
    files_to_sync:list = [
        i.strip() for i in files_to_sync.split("<<>>")
    ]
    for src in files_to_sync:
        dst_file = src.split("/./")[1] if "/./" in src else os.path.split(src)[1]
        dst = Path(dst_dir)/dst_file
        srcp = Path(src)
        if srcp.exists() and srcp.stat().st_mtime > dst.stat().st_mtime:
            with open(src,"rb") as s, open(dst,"wb+") as d:
                print("Synching:")
                print(f"  src: {src}")
                print(f"  dst: {dst}")
                hashes = blockchecksums(d)
                patchstream(d,d,rsyncdelta(s,hashes))
        else:
            pass
