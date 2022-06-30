import requests
import time

"""
理科
https://static-data.gaokao.cn/www/2.0/schoolspecialindex/2021/459/14/1/51/1.json（51）
https://static-data.gaokao.cn/www/2.0/schoolspecialindex/2021/459/14/1/52/1.json （52）
（44）（45）
文科
https://static-data.gaokao.cn/www/2.0/schoolspecialindex/2021/269/14/2/51/1.json

"""


def get_one_major(schiil_id, j):
    type_dt = {"1": "理科", "2": "文科"}
    dt = {
        "51": "1A",
        "52": "1B",
        "44": "2A",
        "45": "2B"
    }
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 "
                      "Safari/537.36 Edg/101.0.1210.39 "
    }
    f = open(file=str(schiil_id) + type_dt[j] + ".txt", mode="w", encoding="utf8")
    for i in dt.keys():
        f.write(dt[i] + "\n")
        x = 0
        while x < 10:
            x += 1
            url = "https://static-data.gaokao.cn/www/2.0/schoolspecialindex/2021/{}/14/{}/{}/{}.json".format(schiil_id,
                                                                                                             j, i, x)
            txt = requests.get(url=url, headers=header).json()
            if txt is '':
                break
            item = txt['data']["item"]
            for one in item:
                name = one["spname"]
                rank = one["min_section"]
                info = name + " " + rank + "\n"
                f.write(info)
        time.sleep(0.5)
    f.close()
    print("专业名次已生成")


if __name__ == '__main__':
    get_one_major(269, 1)
