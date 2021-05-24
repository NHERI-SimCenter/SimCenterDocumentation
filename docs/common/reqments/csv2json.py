#!/bin/python3


import sys,os,csv,json


if __name__=="__main__":
    #data = {}
    #with open(sys.argv[1]) as f:
    #    reader = csv.reader(f)
    #    for row in reader:
    #        print(f"  \"{row[0]}\":{{ ")
    #        print(f"    \"target\": {row[1]},")
    #        print("  },")


    data = {}
    working_dict = {}
    working_list = []
    print(sys.argv[1], file=sys.stderr)
    with open(sys.argv[1]) as f:
        reader = csv.reader(f,quotechar='"',skipinitialspace=True)
        for row in reader:
            if row and "." in row[0]:
                key, *nums = row[0].split(".")
                if key not in data:
                    data[key] = {"items": [], "target": row[1].strip().replace("\"","")}

                lev = data[key]
                for level in map(int,nums[:-1]):
                    assert level > 0
                    lev = lev["items"][level-1]

                while len(lev["items"]) < int(nums[-1])-1:
                    lev["items"].append({"target": None})

                if "fields" in lev: del lev["fields"]
                lev["items"].append(
                    {
                        "target": ",".join(row[1:-3]).strip().replace("\"",""),
                        "fields": list(map(lambda x: x.strip().replace("\"",""),row[-3:])),
                        "items": []
                    }
                )
            elif row:
                data[row[0]] = {"items": [], "target": row[1].strip().replace("\"","")}
                
        print(json.dumps(data,indent=4))


