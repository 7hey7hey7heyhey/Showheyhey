# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:56:30 2019

@author: u00180118
"""


Kensaku = "全部入り"

# pythonでWord文章を抽出する。
# https://qiita.com/int_main_void/items/16cede139bd64514b810

import win32com.client
Application=win32com.client.Dispatch("Word.Application")
#Wordを画面表示する : VisibleプロパティをTrueにする・・・[2]
Application.Visible=True
#Word文書を読み取り専用で開く : Documents.Open(ReadOnly=True)メソッドを呼ぶ・・・[7]

a1 = "C:\\Users\\u00180118\\Desktop\\python code\\"
a2 = "py基礎.docx" # C:\\Users\\u00180118\\Desktop\\python code\\
aaa = a1 + a2
doc=Application.Documents.Open(
       FileName=aaa,
       ConfirmConversions=None,
       ReadOnly=True)


Word_Content = doc.Content.Text
type(Word_Content)

if Word_Content.find(Kensaku) != -1 : # 検索にヒットしなかった場合は-1を返す。（-1出なかった場合は検索にヒットしたということ。）（ヒットした場合は、発見した文字の順番を返す。）
    print("確認できました。")


#Word文書を保存せずに閉じる : Document.Close(SaveChanges=0)メソッドを呼ぶ・・・[7]
doc.Close(SaveChanges=0)
#Wordを終了する : Quitメソッドを呼ぶ・・・[2]
Application.Quit()
