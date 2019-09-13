# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:02:31 2019

@author: u00180118
a0051.pyの発展形
a0048.pyの発展形
"""


import glob
import win32com.client # windowsでWordを操作するときに使えるモジュール（多分）

KEYWORD = "不純物" # 検索したいキーワードを指定

PATH ="//Clsvf1/千葉プロセス/グループ統合データベース/050　報告書・諸会議資料/010 各種報告書/020 月報/030 月報関係資料/04 エラストマー/S-SBR関係月報/**/[!~]**.docx"

FILE_LIST = glob.glob(PATH,recursive=True) # type(FILE_LIST),len(FILE_LIST)

Wordfile_list = [] # 空のリストを作る。

for i in FILE_LIST:
    Application=win32com.client.Dispatch("Word.Application")
    Application.Visible=True # Wordを画面表示する : VisibleプロパティをTrueにする
    doc=Application.Documents.Open( # ワードファイルを読み取り専用で開く　: Documents.Open(ReadOnly=True)メソッドを呼ぶ
           FileName=i,
           ConfirmConversions=None,
           ReadOnly=True)
    
    Word_Content = doc.Content.Text # type(Word_Content) # ワードのテキストの中身を抽出。
    
    if Word_Content.find(KEYWORD) != -1 : # 検索にヒットしなかった場合は-1を返す。（-1出なかった場合は検索にヒットしたということ。）（ヒットした場合は、発見した文字の順番を返す。）
        Wordfile_list.append(i)
    doc.Close(SaveChanges=0) # Word文書を保存せずに閉じる : Document.Close(SaveChanges=0)メソッドを呼ぶ


Application.Quit() # Wordを終了する : Quitメソッドを呼ぶ

"""
# 検索したい文字列を含むファイル名を出力する。
print(Wordfile_list)
Wordfile_list = set(Wordfile_list) # リスト内の重複を無くす。
return Wordfile_list


"""