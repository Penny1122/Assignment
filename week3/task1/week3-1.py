#要求一：Python 取得網路上的資料並儲存到檔案中
import urllib.request as taipei
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with taipei.urlopen(src) as source:
    data=json.load(source) # 利用 JSON 模組處理 json 資料格式
clist=data["result"]["results"]
#print(clist)
with open("data.csv", "w", encoding="utf-8") as file:
    for information in clist:
        year=information["xpostDate"][0:4]
        #print(year)
        img=information["file"].replace("https", " https").split()
        #print(img)
        if (int(year) >= 2015):
            file.write(information["stitle"]+","
            +information["address"][5:8]+","
            +information["longitude"]+","
            +information["latitude"]+","
            +img[0]+"\n")
