# UNCO
import glob
import json

pattern_name = './geo-point/*.tweets'
geo_point={}
for name in glob.glob(pattern_name):
    print (name)
    with open(name, 'r',encoding="utf-8") as f:
        records=f.read().split("\n")
        records.remove("")
        for record in records:
            record=json.loads(record)
            geo_point.update({int(record["id_str"]):record})
    break

with open('./geo-point.json', 'w',encoding="utf-8") as f:
    json.dump(geo_point,f, ensure_ascii=False)
