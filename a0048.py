# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:04:04 2019

@author: u00180118
"""


# wordファイル内のプログラム内の文字列を検索するプログラム。

# 下のkensakuに検索したい文字列を入力して下さい。
# Dir_set2に検索したいディレクトリを設定してください。

def a0048(kensaku,Dir_set2,File_TYPE): # 関数を動かすために必要な変数は3つ（検索したい文字列、検索したいディレクトリ、ファイルの拡張子）
    import os # osモジュールのインポートを行う。
    import win32com.client # windowsでWordを操作するときに使えるモジュール（多分）
    os.chdir(Dir_set2) # ディレクトリの変更


    # フォルダからファイル一覧を取得する。

    import pathlib

    path = pathlib.Path('.') # カレントフォルダ('.')を指定

    file_list1 = []
    for po in path.iterdir(): # ディレクトリ内のファイル・サブディレクトリ一覧を取得
        # print(type(path.iterdir()))
        if not po.is_dir(): # フォルダでない場合に表示する。
            if po.match(File_TYPE): # 指定したファイルの拡張子にマッチしていれば、追加する。
                file_list1.append(po) # 追加する操作。
            # print(type(po.is_dir()))
            # print(po)
    
    file_name_list = [] # 空のリストを作る。
    for ll in file_list1: # ファイルひとつひとつを準場に処理していくために、forループを作る。
        ll = str(ll) # 文字列に変換
        lll = Dir_set2 + "\\" +ll # 文字列を結合
        
        

        Application=win32com.client.Dispatch("Word.Application")
        #Wordを画面表示する : VisibleプロパティをTrueにする・・・[2]
        Application.Visible=True
        #Word文書を読み取り専用で開く : Documents.Open(ReadOnly=True)メソッドを呼ぶ・・・[7]
        doc=Application.Documents.Open( # ワードファイルを読み取り専用で開く
               FileName=lll,
               ConfirmConversions=None,
               ReadOnly=True)
        
        
        Word_Content = doc.Content.Text
        # type(Word_Content)
        
        if Word_Content.find(kensaku) != -1 : # 検索にヒットしなかった場合は-1を返す。（-1出なかった場合は検索にヒットしたということ。）（ヒットした場合は、発見した文字の順番を返す。）
            # print("確認できました。")
            file_name_list.append(ll)
        
        #Word文書を保存せずに閉じる : Document.Close(SaveChanges=0)メソッドを呼ぶ・・・[7]
    doc.Close(SaveChanges=0)
    #Wordを終了する : Quitメソッドを呼ぶ・・・[2]
    Application.Quit()

    
    # 検索したい文字列を含むファイル名を出力する。
    print(file_name_list)
    file_name_list = set(file_name_list) # リスト内の重複を無くす。
    return file_name_list


if __name__ == "__main__":
    A = "全部入り"
    B = "C:\\Users\\u00180118\\Desktop\\python code" # 検索したいフォルダ（ディレクトリを設定する。）
    C = "*.docx"
    a0048(A,B,C)
