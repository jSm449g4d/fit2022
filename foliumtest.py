# ツイッターの情報からふぉりうむで点をプロットするプログラム

import folium
import glob
import json

pattern_name = './dataset/geo-point/*.tweets'
geo_point=[]
for name in glob.glob(pattern_name):
    with open(name, 'r',encoding="utf-8") as f:
        geo_point=f.read().split("\n")
        geo_point.remove("")
    break

testDcit=json.loads(geo_point[-1])
print(testDcit)
location=testDcit['place']['bounding_box']['coordinates'][0][0]
location.reverse()
print(location)
        
m = folium.Map(location=location)
folium.Marker(location=location).add_to(m)
m.save("./output/foliumtest.html")
