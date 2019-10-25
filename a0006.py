##############################################################################
"""
pythonファイル内のキーワード検索
指定する必要があるもの以下2つ
1. 検索したいディレクトリのパス
2. 検索したいキーワード
（3. 検索したいファイル形式。ここではpyファイルを指定している。）

"""
##########################  設定するもの  ################################
kensaku = 'appropriate' # 検索したい言葉をここに入れる。
KENSAKU_PATH = "C:\\Users\\u00180118\\Desktop\\python code"
File_TYPE = "*.py" # 検索したいファイルの型を指定。ここではpyファイル（pythonのコード）の探索を行いたいから、pyを指定する。
########################################################################

import os # os.getcwd() # 現在のディレクトリを表示
os.chdir(KENSAKU_PATH) # ディレクトリの変更
"""
Dir_set1 = "C:\\Users\\u00180118\\Desktop" # 検索したいフォルダ（ディレクトリを設定する。）
Dir_set2 = "C:\\Users\\u00180118\\Desktop\\python code" # 検索したいフォルダ（ディレクトリを設定する。）
os.chdir(Dir_set2) # ディレクトリの変更
"""
# フォルダからファイル一覧を取得する。
import pathlib
path = pathlib.Path('.') # カレントフォルダ('.')を指定


file_list1 = [] # 空のリストを作る。
for po in path.iterdir(): # •ディレクトリ内のファイル・サブディレクトリ一覧を取得 iterdir
    # print(type(path.iterdir()))
    if not po.is_dir(): # フォルダでない場合(つまり、何らかのファイルの場合（例えば、エクセルファイルとかWordファイルのとき）)に表示する。
        if po.match(File_TYPE): # 指定したファイルの拡張子にマッチしていれば、追加する。
            file_list1.append(po) # 追加する操作。 # po をリストに追加する（poとは何らかのファイル）。
            # print(type(po.is_dir()))
            # print(po)

# print(file_list1) # ディレクトリ内のファイルを確認する。# file_list1[0]　# file_list1[1]
"""
for ll in file_list1:
    print(ll)
"""
file_name_list = [] # 空のリストを作る。
for ll in file_list1: # ディレクトリ内のファイルひとつひとつをループ計算させる。
    
    text = [] # 空のリストを作る。
    with open(ll,encoding='utf-8') as f: # 検索したいファイルを設定    
        for line in f:
            text.append(line)
            # print(line), # print(text), type(text)
        list = text
        for l in list:
            if kensaku in l:
                # type(l)
                file_name_list.append(ll)

file_name_list = set(file_name_list) # リスト内の重複を無くす。

print(file_name_list)
