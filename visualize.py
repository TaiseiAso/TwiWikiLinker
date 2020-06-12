# coding: utf-8

"""Twitterデータと紐づいたWikipediaデータの数のヒストグラムを画像として保存する"""
__author__ = "Aso Taisei"
__date__ = "13 Jun 2020"

import os
import sys
import matplotlib.pyplot as plt

def visualize():
    """Twitterデータと紐づいたWikipediaデータの数のヒストグラムを画像として保存する"""

    link_path = "./data/link.txt"
    img_path = "./data/visualize.png"

    if not os.path.isfile(link_path):
        print("{}: cannot find".format(link_path))
        sys.exit(1)
    try:
        f_in = open(link_path, 'r', encoding='utf-8')
    except:
        print("{}: file read error".format(link_path))
        sys.exit(1)

    hist = []
    ids = f_in.readline()
    while ids:
        hist.append(len(ids.split()))
        ids = f_in.readline()

    fig = plt.figure()
    plt.hist(hist, bins=100)
    plt.xlabel("sum of wikipedia link")
    plt.ylabel("twitter data")
    fig.savefig(img_path)

    f_in.close()

if __name__ == '__main__':
    visualize()
