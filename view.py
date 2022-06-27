import matplotlib.pyplot as plt
import numpy as np


def Histogram(grade_data):
    plt.rcParams['font.sans-serif'] = ['SimHei']

    labels = ['2019', '2020', '2021']
    a = grade_data[0]
    b = grade_data[1]
    c = grade_data[2]
    d = grade_data[3]

    x = np.arange(len(labels))  # the label locations
    width = 0.15  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width * 1.5, a, width, label='本科一批A段')
    rects2 = ax.bar(x - width * 0.5, b, width, label='本科一批B段')
    rects3 = ax.bar(x + width * 0.5, c, width, label='本科二批A段')
    rects4 = ax.bar(x + width * 1.5, d, width, label='本科二批B段')

    plt.yticks([400, 450, 500, 550, 600, 650, 700])
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom'
                        )

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    autolabel(rects4)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('最低录取分数')
    ax.set_title('2019到2021年最低录取分数线')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.show()


if __name__ == '__main__':
    date = [
        [507, 537, 505],
        [507, 0, 0],
        [447, 473, 446],
        [434, 453, 431],
    ]
    Histogram(date)
