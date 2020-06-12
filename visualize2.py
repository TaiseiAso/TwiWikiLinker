# coding: utf-8

"""
紐づけるWikipediaデータの最小数を増加させることで、
必要なくなるWikipediaデータの数のヒストグラムを画像として保存する
"""
__author__ = "Aso Taisei"
__date__ = "13 Jun 2020"

import os
import sys
import matplotlib.pyplot as plt

def visualize2():
    """
    紐づけるWikipediaデータの最小数を増加させることで、
    必要なくなるWikipediaデータの数のヒストグラムを画像として保存する
    """

    link_path = "./data/link.txt"
    img_path = "./data/visualize2.png"

    if not os.path.isfile(link_path):
        print("{}: cannot find".format(link_path))
        sys.exit(1)
    try:
        f_in = open(link_path, 'r', encoding='utf-8')
    except:
        print("{}: file read error".format(link_path))
        sys.exit(1)

    dist = {}
    ids = f_in.readline()
    while ids:
        id_list = ids.split()
        len_id_list = len(id_list)
        for id in id_list:
            if id in dist:
                dist[id] = max(dist[id], len_id_list)
            else:
                dist[id] = len_id_list
        ids = f_in.readline()

    hist = list(dist.values())

    fig = plt.figure()
    plt.hist(hist, bins=100)
    plt.xlabel("x < link_min")
    plt.ylabel("unuse wikipedia data")
    fig.savefig(img_path)

    f_in.close()

if __name__ == '__main__':
    visualize2()
