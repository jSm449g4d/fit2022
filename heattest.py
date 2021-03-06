# ツイッターのファイルからヒートマップを出力するテスト

import folium
from folium import plugins
import glob
import json

pattern_name = './dataset/geo-point/*.tweets'
geo_point=[]
gp_heat=[]
roop_num=1
for name in glob.glob(pattern_name):
    print(name)
    with open(name, 'r',encoding="utf-8") as f:
        geo_point=f.read().split("\n")
        geo_point.remove("")
    try:
        for gp in geo_point:
            gp=json.loads(gp)
            gp=gp['place']['bounding_box']['coordinates'][0][0]
            gp.reverse()
            gp_heat.append(gp)
    except:
        print("err")
    roop_num-=1
    if (roop_num==0):
        break;
print(len(gp_heat))
        
m = folium.Map(location=gp_heat[0], zoom_start=6)
folium.plugins.HeatMap(gp_heat, radius=7, blur=5).add_to(m)
m.save("./output/heattest.html")
