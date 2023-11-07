import json
# reading to data.json
with open("./data/cpu-amd.json", encoding="utf-8") as infile:
    parsed_json = json.load(infile)
    for index, item in enumerate(parsed_json["items"]):
        print(index)
        print('-----------------------')