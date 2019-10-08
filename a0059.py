# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:51:06 2019

@author: socce
# PDFから全テキストを抽出する方法
https://tech.bita.jp/article/18

画像だけのPDFにコンピュータで文字を扱うための文字情報が含まれないと、文字コードによる検索ができません。
https://teratail.com/questions/153930

# PDFからテキストデータをうまく抜けるかの検証結果のご報告（pdfminer.six)／Python 
https://arakan-pgm-ai.hatenablog.com/entry/2018/01/07/080000

# PDFMiner のインストール
https://a244.hateblo.jp/entry/2017/08/26/001050

# 詳細PDF入門 ー 実装して学ぼう！PDFファイルの構造とその書き方読み方 
https://itchyny.hatenablog.com/entry/2015/09/16/100000

pdfminer.sixのインストールが必要だが、社内のネットワークの規制の関係からか、エラーが出る。

# (Windows) Python3でのUnicodeEncodeErrorの原因と回避方法
https://qiita.com/butada/items/33db39ced989c2ebf644

# Python エラー'cp932' codec can't encode character
https://ja.stackoverflow.com/questions/34431/python-%E3%82%A8%E3%83%A9%E3%83%BCcp932-codec-cant-encode-character

# PDFで文字が検索できない
https://www.antenna.co.jp/pdf/reference/searchable-pdf.html
"""

###############################################################################
import os
os.getcwd()
# os.chdir("C:\\Users\\socce\\Desktop")
os.chdir("C:\\Users\\u00180118\\Desktop\\python code") # ディレクトリの変更 # PDFの読み込み結果をtxtファイルに出力する際に、カレントディレクトリ下に作られるため。

###############################################################################
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import glob

# PATH = "//clsvf1/千葉プロセス/グループ統合データベース/080　技術データ/040 合成ゴム エラストマー/000 技術資料/**/[!~]*.pdf"
# PATH_1 = "//clsvf1/千葉プロセス/グループ統合データベース/050　報告書・諸会議資料/010 各種報告書/084 ワークアサインメント/201905ワークアサインメント【福原】/009 発明整理票 関連/検索の範囲/IPCについて/kosin_ipc_ver2019/**/[!~]*.pdf"
# PATH_2 = "//clsvf1/千葉プロセス/グループ統合データベース/050　報告書・諸会議資料/010 各種報告書/084 ワークアサインメント/201905ワークアサインメント【福原】/009 発明整理票 関連/**/[!~]*.pdf"
PATH_3 = "//clsvf1/千葉プロセス/グループ統合データベース/050　報告書・諸会議資料/010 各種報告書/084 ワークアサインメント/201905ワークアサインメント【福原】/009 発明整理票 関連/P2007-238586_A.pdf"
file_list = glob.glob(PATH_3, recursive=True) # PDFファイル取り込み

###############################################################################
# 関数の定義　PDFの読み込み関数。引数としてPDFのパスを渡す。
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    laparams.detect_vertical = True # Trueにすることで綺麗にテキストを抽出できる
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    maxpages = 0
    caching = True
    pagenos=set()
    fstr = ''
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,caching=caching, check_extractable=True):
        interpreter.process_page(page)

        str = retstr.getvalue()
        fstr += str

    fp.close()
    device.close()
    retstr.close()
    return fstr
###############################################################################

result_list = []
for item in file_list:
    result_txt = convert_pdf_to_txt(item)
    result_list.append(result_txt)


allText = ','.join(result_list) # PDFごとのテキストが配列に格納されているので連結する

file = open('pdf.txt', 'w',encoding='UTF-8') #書き込みモードでオープン#########################################################################
file.write(allText)
file.close()

"""""""""""""""""""""""""""
cp932　と　utf-8　に関して勉強せよ
"""""""""""""""""""""""""""
