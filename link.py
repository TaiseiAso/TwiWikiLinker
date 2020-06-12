# coding: utf-8

"""TwitterデータとWikipediaデータを紐づける"""
__author__ = "Aso Taisei"
__date__ = "13 Jun 2020"

import os
import sys
import yaml

class TwiWikiLinker:
    """TwitterデータとWikipediaデータを紐づけるクラス"""

    def __init__(self):
        """コンストラクタ"""
        self.config_path = "./config.yml"
        self.tweet_path = "./data/tweet.txt"
        self.tweet_part_path = "./data/tweet-part.txt"
        self.wiki_clean_yaml_path = "./data/cleaned.yml"
        self.wiki_hash_yaml_path = "./data/hash.yml"
        self.link_path = "./data/link.txt"

        if not os.path.isfile(self.config_path):
            print("{}: cannot find".format(self.config_path))
            sys.exit(1)

        try:
            config = yaml.load(stream=open(self.config_path, 'r', encoding='utf-8'), Loader=yaml.SafeLoader)
        except:
            print("{}: file read error".format(self.config_path))
            sys.exit(1)

        self.use_parts = config['use_parts']

    def link(self):
        """TwitterデータとWikipediaデータを紐づける"""
        error_flag = False
        if not os.path.isfile(self.tweet_path):
            print("{}: cannot find".format(self.tweet_path))
            error_flag = True

        if not os.path.isfile(self.tweet_part_path):
            print("{}: cannot find".format(self.tweet_part_path))
            error_flag = True

        if not os.path.isfile(self.wiki_clean_yaml_path):
            print("{}: cannot find".format(self.wiki_clean_yaml_path))
            error_flag = True

        if not os.path.isfile(self.wiki_hash_yaml_path):
            print("{}: cannot find".format(self.wiki_hash_yaml_path))
            error_flag = True

        try:
            f_in_tweet = open(self.tweet_path, 'r', encoding='utf-8')
        except:
            print("{}: file read error".format(self.tweet_path))
            error_flag = True

        try:
            f_in_tweet_part = open(self.tweet_part_path, 'r', encoding='utf-8')
        except:
            print("{}: file read error".format(self.tweet_part_path))
            error_flag = True

        try:
            f_in_wiki_title = open(self.wiki_clean_yaml_path, 'r', encoding='utf-8')
        except:
            print("{}: file read error".format(self.wiki_clean_yaml_path))
            error_flag = True

        try:
            f_in_wiki_hash = open(self.wiki_hash_yaml_path, 'r', encoding='utf-8')
        except:
            print("{}: file read error".format(self.wiki_hash_yaml_path))
            error_flag = True

        try:
            f_out = open(self.link_path, 'w', encoding='utf-8')
        except:
            print("{}: file write error".format(self.link_path))
            error_flag = True

        if error_flag:
            sys.exit(1)

        wiki_title_dict = yaml.load(f_in_wiki_title)
        wiki_hash_dict = yaml.load(f_in_wiki_hash)

        all_ids = set()

        tweet = f_in_tweet.readline()
        tweet_part = f_in_tweet_part.readline()
        while tweet and tweet_part:
            ids = set()
            for word, part in zip(tweet.split(), tweet_part.split()):
                if self.use_parts.get(part):
                    ids_ = wiki_title_dict.get(word)
                    if ids_:
                        ids = ids | ids_
                    ids_ = wiki_hash_dict.get(word)
                    if ids_:
                        ids = ids | ids_
            f_out.write(' '.join(map(str, ids)) + "\n")
            all_ids = all_ids | ids

            tweet = f_in_tweet.readline()
            tweet_part = f_in_tweet_part.readline()

        print("sum of use wikipedia data: {}".format(len(all_ids)))

        f_out.close()
        f_in_wiki_hash.close()
        f_in_wiki_title.close()
        f_in_tweet_part.close()
        f_in_tweet.close()

def link():
    """TwitterデータとWikipediaデータを紐づける"""
    twi_wiki_linker = TwiWikiLinker()
    twi_wiki_linker.link()

if __name__ == '__main__':
    link()
