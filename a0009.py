











# -*- coding: utf-8 -*-
"""
編集中編集中編集中編集中編集中編集中編集中編集中編集中編集中編集中編集中編集中編集中編集中編集中編集中編集中編集中
Created on Wed Jul 31 16:29:35 2019

@author: u00180118
"""
import os
os.getcwd()
os.chdir("C:\\Users\\u00180118\\Desktop\\patent_file") # ディレクトリの変更
import glob
glob.glob("*")
# https://techacademy.jp/magazine/18928

# 以下, ネットワーク上のディレクトリを探すコード
glob.glob("//clsvf1/千葉プロセス/*")
# フォルダ内を下の階層まで下りて探索する場合、ショートカットがあると無限ループしてしまう可能性があるので、
# ショートカットはスキップする。
# .lnkの拡張子をもつファイルを読み込まないようにする。

# だめな例
glob.glob("\\clsvf1\千葉プロセス\グループ統合データベース\080　技術データ\040 合成ゴム エラストマー\000 物性データ\*")

# 良い例
glob.glob("//clsvf1/千葉プロセス/グループ統合データベース/080　技術データ/040 合成ゴム エラストマー/000 物性データ\*")
上記の場合、スラッシュは/でないといけない！！/ではだめ！！

import glob
File_LIST = glob.glob("C:\\Users\\u00180118\\Desktop\\patent_file\\*.pdf") 
File_LIST = glob.glob("//cksvf4/自動車材-T/Gドライブ/*") 

File_LIST = glob.glob("\\clsvf1\\千葉プロセス\\グループ統合データベース\\080　技術データ\\040 合成ゴム エラストマー\\240 S-SBRのCNP試作\\S-SBR技術資料\\*docx") 

\\clsvf1\千葉プロセス\グループ統合データベース\080　技術データ\040 合成ゴム エラストマー\240 S-SBRのCNP試作\S-SBR技術資料


"\\clsvf1\\千葉プロセス\\グループ統合データベース\\080　技術データ\\040 合成ゴム エラストマー"
import a0048
AAA = "全部入り"
BBB = "C:\\Users\\u00180118\\Desktop\\python code" # 検索したいフォルダ（ディレクトリを設定する。）

CCC = "*.docx"
a0048.a0048(AAA,BBB,CCC)



AAA = ["A","B","C"]
k="B"
AAA.remove(k)



import os 
os.getcwd()

BBB = "\\ネットワーク\\clsvf1\\千葉プロセス\\グループ統合データベース"

Dir_name="\\clsvf1\千葉プロセス\グループ統合データベース\080　技術データ\040 合成ゴム エラストマー"
os.chdir(Dir_name)
BBB= "C:\\Users\\u00180118\\Desktop"
os.chdir(Dir_name)

import pathlib

share = pathlib.WindowsPath(r'\\servername\')
share = pathlib.WindowsPath(r'\\ネットワーク\\clsvf1')


path = pathlib.Path('.')
po = path.iterdir()
po
type(po)
po[1]