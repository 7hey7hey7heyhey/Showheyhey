# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:49:04 2019

@author: u00180118
"""


import pathlib
import os # osモジュールのインポートを行う。

Dir_set = "C:\\Users\\u00180118\\Desktop\\python code" # 検索したいフォルダ（ディレクトリを設定する。） # ディレクトリの変更
os.chdir(Dir_set) # ディレクトリの変更
path = pathlib.Path('.')

def show_recursive(path):
    for po in path.iterdir():
        if po.is_dir(): # ディレクトリだった場合（ファイルではない場合）
            show_recursive(po) # 自分でつくったshow_recursive関数を再帰的に呼び出す！！
        elif po.is_file(): # ディレクトリではない場合（ファイルだった場合）
            print(po)

        


"""
Dir_set = "C:\\Users\\u00180118\\Desktop\\python code" # 検索したいフォルダ（ディレクトリを設定する。） # ディレクトリの変更
os.chdir(Dir_set) # ディレクトリの変更
path = pathlib.Path('.')

import a0014

a0014.show_recursive(path)

"""
