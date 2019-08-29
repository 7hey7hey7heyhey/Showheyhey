


import glob
import os

File_LIST = glob.glob("//cksvf3/00公開/10102500千葉プロセスグループ/700 パイロット各種情報交換用/押出機技術資料/*")
File_TYPE = ".docx"


po = File_LIST[1]

file_list1 = [] # 空のリストを作っておく。
dir_list1 = [] # 空のリストを作っておく。
for po in File_LIST: # ディレクトリ内のファイル・サブディレクトリ一覧をループさせる。
        if os.path.isfile(po)==TRUE: # フォルダでない場合(通常ファイルの場合)
            if po.match(File_TYPE): # 指定したファイルの拡張子にマッチしていれば、追加する。
                file_list1.append(po) # 追加する操作。
        else:  # フォルダの場合(通常ファイルではない場合)
            dir_list1.append(po) # 追加する操作。
            

print(file_list1)
print(dir_list1)



A = "C:\\Users\\u00180118\\Desktop\\python code"
B = "C:\\Users\\u00180118\\Desktop\\python code\\a0006.py"

os.path.isfile(File_LIST[1])
os.path.isfile(B)
os.path.isfile(A)





NEW_File_LIST = []
for k in File_LIST:
    print(k)
    if “.lnk” not in k: # .lnkという文字列を含まない要素だけ抜き出す。（ショートカットでのループを避けるため。）
        NEW_File_LIST.append(k)

"""
len(NEW_File_LIST)
""" 












