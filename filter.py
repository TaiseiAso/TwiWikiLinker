# coding: utf-8

"""使用しないTwitter/Wikipediaデータをフィルタリングする"""
__author__ = "Aso Taisei"
__date__ = "13 Jun 2020"

import os
import sys
import yaml

class DataFilter:
    """使用しないTwitter/Wikipediaデータをフィルタリングするクラス"""

    def __init__(self):
        """コンストラクタ"""
        self.config_path = "./config.yml"

        self.tweet_path = "./data/tweet.txt"
        self.tweet_part_path = "./data/tweet-part.txt"
        self.reply_path = "./data/reply.txt"
        self.wiki_clean_path = "./data/cleaned.txt"
        self.wiki_clean_part_path = "./data/cleaned-part.txt"
        self.link_path = "./data/link.txt"

        self.filtered_tweet_path = "./data/filtered-tweet.txt"
        self.filtered_tweet_part_path = "./data/filtered-tweet-part.txt"
        self.filtered_reply_path = "./data/filtered-reply.txt"
        self.filtered_wiki_path = "./data/filtered-wiki.txt"
        self.filtered_wiki_part_path = "./data/filtered-wiki-part.txt"
        self.filtered_link_path = "./data/filtered-link.txt"

        if not os.path.isfile(self.config_path):
            print("{}: cannot find".format(self.config_path))
            sys.exit(1)

        try:
            config = yaml.load(stream=open(self.config_path, 'r', encoding='utf-8'), Loader=yaml.SafeLoader)
        except:
            print("{}: file read error".format(self.config_path))
            sys.exit(1)

        self.link_min = config['link_min']

    def filtering(self):
        """使用しないTwitter/Wikipediaデータをフィルタリングする"""
        error_flag = False
        for path in [self.tweet_path, self.tweet_part_path, self.wiki_clean_path, self.wiki_clean_part_path, self.link_path, self.reply_path]:
            if not os.path.isfile(path):
                print("{}: cannot find".format(path))
                error_flag = True

        f_in = []
        for path in [self.tweet_path, self.tweet_part_path, self.wiki_clean_path, self.wiki_clean_part_path, self.link_path, self.reply_path]:
            try:
                f_in.append(open(path, 'r', encoding='utf-8'))
            except:
                print("{}: file read error".format(path))
                error_flag = True

        f_out = []
        for path in [self.filtered_tweet_path, self.filtered_tweet_part_path, self.filtered_wiki_path, self.filtered_wiki_part_path, self.filtered_link_path, self.filtered_reply_path]:
            try:
                f_out.append(open(path, 'w', encoding='utf-8'))
            except:
                print("{}: file write error".format(path))
                error_flag = True

        if error_flag:
            sys.exit(1)

        new_link = []
        ids = set()

        tweet = f_in[0].readline()
        tweet_part = f_in[1].readline()
        reply = f_in[5].readline()
        link = f_in[4].readline()

        cnt = cnt_ = 0
        while tweet and tweet_part and reply and link:
            if len(link.split()) >= self.link_min:
                cnt_ += 1
                f_out[0].write(tweet)
                f_out[1].write(tweet_part)
                f_out[5].write(reply)
                id_list = list(map(int, link.split()))
                for id in id_list:
                    ids.add(id)
                new_link.append(id_list)

            tweet = f_in[0].readline()
            tweet_part = f_in[1].readline()
            reply = f_in[5].readline()
            link = f_in[4].readline()
            cnt += 1

        print("tweet: {} -> {}".format(cnt, cnt_))

        wiki = f_in[2].readline()
        wiki_part = f_in[3].readline()

        cnt = cnt_ = 0
        while wiki and wiki_part:
            if cnt in ids:
                cnt_ += 1
                f_out[2].write(wiki)
                f_out[3].write(wiki_part)

            wiki = f_in[2].readline()
            wiki_part = f_in[3].readline()
            cnt += 1

        print("wiki: {} -> {}".format(cnt, cnt_))

        change = {}
        for i, id in enumerate(ids):
            change[id] = str(i)

        for id_list in new_link:
            f_out[4].write(' '.join([change[id] for id in id_list]) + "\n")

        for f in f_in+f_out:
            f.close()

def filtering():
    """使用しないTwitter/Wikipediaデータをフィルタリングする"""
    data_filter = DataFilter()
    data_filter.filtering()

if __name__ == '__main__':
    filtering()
