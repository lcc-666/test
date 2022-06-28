import requests
import time
from numpy import transpose, VisibleDeprecationWarning
import view
import numpy as np


def get_num(school_id, j):
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 "
                      "Safari/537.36 Edg/101.0.1210.39 "
    }
    dt = {1: "理科", 2: "文科"}

    date = []
    for i in range(2019, 2022):
        url = "https://static-data.gaokao.cn/www/2.0/schoolprovinceindex/{}/{}/14/{}/1.json".format(i, school_id, j)
        txt = requests.get(url=url, headers=header, ).json()
        item = txt['data']["item"]
        print(item[0]["year"], dt[int(j)])
        item_dict = {
            "本科一批A段": 0,
            "本科一批B段": 0,
            "本科二批A段": 0,
            "本科二批B段": 0,
        }
        for one in item:

            print("{} 最低分{} 最低名次{}".format(one["local_batch_name"], int(one["min"]),one['min_section']))
            item_dict[one["local_batch_name"]] = int(one["min_section"])

        date.append(list(item_dict.values()))
        time.sleep(0.5)
    np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)

    try:
        transposed = transpose(date).tolist()
        view.Histogram(transposed)
    except IndexError:
        pass



if __name__ == '__main__':
    get_num(269, 1)
