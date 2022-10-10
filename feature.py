import os
import sys
import json

with open("feature.json", "r") as f:
    feature_data = json.load(f)

with open("docs/test.md", "r") as f:
    dat = f.readlines()
    #print(dat)
    for x in dat:
        if x.startswith("<!--start"):
            tag = str(x.split(" ")[1])[0:-4]
            # Remove - if any and make every first letter capital
            heading = tag.replace("-", " ").title()
            index_of_tag = dat.index(x)
            to_be_replaced = dat[index_of_tag+1]
            content = feature_data[tag]
            if content["preview"] == 1:
                to_be_added = f"""=== "About {heading}"\n    {content["about"]}\n=== "Project Details"\n    {content["details"]}\n=== "Preview"\n    ![{heading}]({content["preview"]})\n""".encode("utf-8")
            else:
                to_be_added = f"""=== "About {heading}"\n    {content["about"]}\n=== "Project Details"\n    {content["details"]}\n""".encode("utf-8")
            dat = [_.encode("utf-8") for _ in dat]
            dat[index_of_tag+1] = to_be_added
            #print(to_be_added)
            
            with open("docs/test.md", "bw+") as f:
                f.writelines(dat)
