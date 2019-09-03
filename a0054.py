# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:58:14 2019

@author: socce
"""

# あたらしいpythonによるデータ分析の教科書　ｐ１４５
#########################################################################################################
# ウェブサイトの中の表のデータ取り込み
url = "https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%83%E3%83%97%E3%83%AC%E3%83%99%E3%83%AB%E3%83%89%E3%83%A1%E3%82%A4%E3%83%B3%E4%B8%80%E8%A6%A7"
tables = pd.read_html(url)
"""
len(tables)
type(tables)
tables[1]
tables[2]
tables[3]
tables[42]
len(tables[41])
"""

 
#########################################################################################################
# csvファイルの読み込みとあたらしいcsvファイルの作成

import pandas as pd
df = pd.read_csv("C:/Users/socce/Desktop/python code/201704health.csv",encoding="utf-8")
df.to_csv("C:/Users/socce/Desktop/python code/write_data.csv")
"""
type(df)
tables.to_csv("C:/Users/socce/Desktop/python code/write_data.csv") # 無理なコード
import os 
os.getcwd()
os.chdir("C:\\Users\\socce\\Desktop\\python code")
"""

#########################################################################################################
# xlsxファイルの読み込みとあたらしいxlsxファイルの作成
import pandas as pd
df = pd.read_excel("C:/Users/socce/Desktop/python code/201704health.xlsx")
df.to_excel("C:/Users/socce/Desktop/python code/write_data.xlsx")



#########################################################################################################
# pandsのデータフレームをそのままの形で保存しておく方法（pickleファイルとして保存する。）
import pandas as pd
df.to_pickle("C:/Users/socce/Desktop/python code/write_data.pickle")

#########################################################################################################
# pickleファイルを読み込む方法
import pandas as pd
df = pd.read_pickle("C:/Users/socce/Desktop/python code/write_data.pickle")

#########################################################################################################
# pandasのデータフレームのデータの整形 # あたらしいpythonによるデータ分析の教科書　ｐ149
import pandas as pd
df = pd.read_pickle("C:/Users/socce/Desktop/python code/write_data.pickle")
# 条件で抽出する。
df["歩数"]>=10000 # bool型で返す方法
df_selected = df[df["歩数"]>=10000]
"""
print(df_selected)
df_selected.shape
"""
df.query("歩数 >= 10000 and 摂取カロリー <= 1800")
df.query("歩数 >= 10000")

#########################################################################################################
# データの型変換
import pandas as pd
df = pd.read_pickle("C:/Users/socce/Desktop/python code/write_data.pickle")
df.dtypes
"""
df.loc[:,"日付"]
type(df.loc[:,"日付"])
"""
df.loc[:,"date"] = df.loc[:,"日付"].apply(pd.to_datetime) # 新しいdateというカラムを生成して、datetime64型で格納する。
"""
print(df)
df.head() # データフレームの先頭の5行を出力する。
"""
#########################################################################################################
# インデックスの設定
import pandas as pd
import numpy as np
df = pd.read_pickle("C:/Users/socce/Desktop/python code/write_data.pickle")
df.loc[:,"date"] = df.loc[:,"日付"].apply(pd.to_datetime) # 新しいdateというカラムを生成して、datetime64型で格納する。
df.loc[:,"摂取カロリー"] = df.loc[:,"摂取カロリー"].astype(np.float32)
"""
df.head() # データフレームの先頭の5行を出力する。
"""
df = df.set_index("date")
"""
df.head() # データフレームの先頭の5行を出力する。
"""


#########################################################################################################
# データの並べ替え
import pandas as pd
df = pd.read_pickle("C:/Users/socce/Desktop/python code/write_data.pickle")
df.sort_values(by="歩数") # 昇順で並べ替えが行われる。
"""
df.sort_values(by="歩数").head()
"""

df.sort_values(by="歩数",ascending=False) # 降順で並べ替えが行われる。
"""
df.sort_values(by="歩数",ascending=False).head()
"""

#########################################################################################################
# 不要なカラムの削除
import pandas as pd
df = pd.read_pickle("C:/Users/socce/Desktop/python code/write_data.pickle")
df = df.drop("日付",axis=1)
"""
df.tail() # データの末尾の5行を出力する。
"""

#########################################################################################################
# 組み合わせデータの挿入
import pandas as pd
df = pd.read_pickle("C:/Users/socce/Desktop/python code/write_data.pickle")
df.loc[:,"歩数/カロリー"] = df.loc[:,"歩数"]/df.loc[:,"摂取カロリー"]

#########################################################################################################
# 時系列データを扱う # あたらしいpythonによるデータ分析の教科書　ｐ158
import pandas as pd
import numpy as np
dates = pd.date_range(start = "2017-04-01", end = "2017-04-30")
np.random.seed(123) # 同じシーズを持ってくる。乱数を扱って計算させるときの常とう手段。（実際の計算ではちゃんとランダムにする必要がある。）
df = pd.DataFrame(np.random.randint(1,31,30),index=dates, columns = ["乱数"])

# 時系列データを扱う # 一年分　365日のデータを作る。 # あたらしいpythonによるデータ分析の教科書　ｐ159
dates = pd.date_range(start = "2017-01-01", periods=365)
"""
dates
dates.shape
"""

np.random.seed(123)
df = pd.DataFrame(np.random.randint(1,31,365),index=dates,columns=["乱数"])

# 月平均のデータにする
df.groupby(pd.Grouper(freq="M")).mean() # freq="M"として、月ごとのデータにグルーピングするようにした。詳しくは公式ドキュメントGrouperを参照
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Grouper.html

df.loc[:,"乱数"].resample("M").mean()

pd.date_range(start = "2019-01-01", end = "2019-12-31",freq = "W-SAT")








## /と\のちがいについて



"""
# 読み込み不可能バージョン
df = pd.read_csv("C:\Users\socce\Desktop\python code\201704health.csv")
"""

df = pd.read_excel("C:/Users/socce/Downloads/notebooks.zip/notebooks/data/201704health")

"""
翔泳社　サンプルデータ
https://www.shoeisha.co.jp/book/download/9784798158341
https://www.shoeisha.co.jp/book/download/9784798158341/detail

"""



