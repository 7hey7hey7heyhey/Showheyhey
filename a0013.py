# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:59:19 2019

@author: u00180118
"""

import pathlib
import os # osモジュールのインポートを行う。

Dir_set = "C:\\Users\\u00180118\\Desktop\\python code" # 検索したいフォルダ（ディレクトリを設定する。） # ディレクトリの変更
os.chdir(Dir_set) # ディレクトリの変更
path = pathlib.Path('.')

for po in path.iterdir():
    if not po.is_dir(): # ディレクトリではない場合（ファイルだった場合）
        print(po)
        



