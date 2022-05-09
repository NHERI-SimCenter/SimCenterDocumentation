import sys
import tempfile
import yaml
import xml.etree.ElementTree as et

if __name__=="__main__":
    app_name = sys.argv[-1]

    with open("examples.yaml","r") as f:
        data = yaml.load(f, Loader=yaml.Loader)

    collection = et.Element("collection")
    try:
        for example in data[app_name]["include-item"]:
            et.SubElement(collection,"item").attrib.update(dict(
                id=example,
                type="BasicExample"
            ))
        et.dump(collection)
    except: print("<collection/>")


