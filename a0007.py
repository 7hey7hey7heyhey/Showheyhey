# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:13:11 2019

@author: u00180118
"""

# pythonでWord文章を抽出する。
# https://qiita.com/int_main_void/items/16cede139bd64514b810

import win32com.client
Application=win32com.client.Dispatch("Word.Application")
#Wordを画面表示する : VisibleプロパティをTrueにする・・・[2]
Application.Visible=True
#Word文書を読み取り専用で開く : Documents.Open(ReadOnly=True)メソッドを呼ぶ・・・[7]
doc=Application.Documents.Open(
       FileName=r"C:\\Users\\u00180118\\Desktop\\python code\\py基礎.docx",
       ConfirmConversions=None,
       ReadOnly=True)


Word_Content = doc.Content.Text
type(Word_Content)

#Word文書を保存せずに閉じる : Document.Close(SaveChanges=0)メソッドを呼ぶ・・・[7]
doc.Close(SaveChanges=0)
#Wordを終了する : Quitメソッドを呼ぶ・・・[2]
Application.Quit()
