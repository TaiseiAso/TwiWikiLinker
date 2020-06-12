# coding: utf-8

"""文書群から単語をキーとするハッシュを形成する"""
__author__ = "Aso Taisei"
__date__ = "11 Jun 2020"

import yaml
import os
import sys

class WikiHash:
    """文書群から単語をキーとするハッシュを形成するクラス"""

    def __init__(self):
        """コンストラクタ"""
        # ファイルパス
        self.config_path = "./config.yml"
        self.wiki_clean_path = "./data/cleaned.txt"
        self.wiki_clean_part_path = "./data/cleaned-part.txt"
        self.wiki_hash_yaml_path = "./data/hash.yml"

        # 設定
        if not os.path.isfile(self.config_path):
            print("{}: cannot find".format(self.config_path))
            sys.exit(1)

        try:
            config = yaml.load(stream=open(self.config_path, 'r', encoding='utf-8'), Loader=yaml.SafeLoader)
        except:
            print("{}: file read error".format(self.config_path))
            sys.exit(1)

        self.use_parts = config['use_parts']

    def filter(self, words, parts):
        """
        ハッシュのキーに用いる品詞のみを残す
        @param:str words 空白区切りの単語列
        @param:str parts 空白区切りの品詞列
        @return:list[str] ハッシュのキーに用いる単語リスト
        """
        filtered_words = []
        for word, part in zip(words.split(), parts.split()):
            if self.use_parts.get(part):
                filtered_words.append(word)
        return filtered_words

    def create(self):
        """文書群から単語をキーとするハッシュを形成する"""
        # 例外処理
        error_flag = False
        if not os.path.isfile(self.wiki_clean_path):
            print("{}: cannot find".format(self.wiki_clean_path))
            error_flag = True

        if not os.path.isfile(self.wiki_clean_part_path):
            print("{}: cannot find".format(self.wiki_clean_part_path))
            error_flag = True

        try:
            f_out = open(self.wiki_hash_yaml_path, 'w', encoding='utf-8')
        except:
            print("{}: file write error".format(self.wiki_hash_yaml_path))
            error_flag = True

        if error_flag:
            sys.exit(1)

        hash = {}

        with open(self.wiki_clean_path, 'r', encoding='utf-8') as f_in,\
        open(self.wiki_clean_part_path, 'r', encoding='utf-8') as f_in_part:
            words = f_in.readline()
            parts = f_in_part.readline()
            line_count = 0

            while words and parts:
                words = self.filter(words, parts)
                for word in words:
                    if word in hash:
                        hash[word].add(line_count)
                    else:
                        hash[word] = set([line_count])

                words = f_in.readline()
                parts = f_in_part.readline()
                line_count += 1

            print("sum of all wikipedia data: {}".format(line_count))

        yaml.dump(hash, f_out, encoding='utf-8', allow_unicode=True)
        f_out.close()

def create_hash():
    """文書群から単語をキーとするハッシュを形成する"""
    wiki_hash = WikiHash()
    wiki_hash.create()

if __name__ == '__main__':
    create_hash()
