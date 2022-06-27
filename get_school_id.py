import requests
import time
"""
https://api.eol.cn/web/api/&page=2&request_type=1&size=20&uri=apidata/api/gk/school/lists
https://api.eol.cn/web/api/?page=3&request_type=1&size=20&uri=apidata/api/gk/school/lists
"""

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 "
                  "Safari/537.36 Edg/101.0.1210.39 "
}

for i in range(1,143):
    url="https://api.eol.cn/web/api/?page=%d&request_type=1&size=20&uri=apidata/api/gk/school/lists"%i
    txt = requests.get(url=url, headers=header, ).json()
    item=txt["data"]["item"]

    f=open(file="./data.txt",mode="a")
    for one in item:
        f.write(one["name"]+":"+str(one["school_id"])+"\n")
    time.sleep(1)
    print(i)
