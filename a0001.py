import PDFMiner
import glob
from PDFMiner.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from glob import glob


PDF_LIST = glob('./patent_file/*.pdf')# PDFファイル取り込み　/現在のディレクトリからひとつ戻る。保存先のファイルが変わる場合はこれを編集する必要あり。patent_fileというのはフォルダの名前。
print(PDF_LIST)

# cmdにpip freezeと入力すると、入っているライブラリを返してくれる。
# pip freeze
# pip install 

# PDFから全テキストを抽出する方法
# https://tech.bita.jp/article/18

for pdf in PDF_LIST
### おまじない ###
print(pdf)
rsrcmgr = PDFResourceManager()
retstr = StringIO()
codec = 'utf-8'
laparams = LAParams()
laparams.detect_vertical = True # Trueにすることできれいにテキストを抽出できる。
device = TextConverter(rsrcmgr, retstr,codec=codec,laparams=laparams)
### おまじない ###

fp = open(pdf,'rb')
interpreter = PDFPageInterpreter(rsrcmgr,device)
maxpage = 0
caching = True
pagenos = set()
fstr = ''
for page in PDFage.get_pages(fp,pagenos,maxpages=maxpages,caching,check_extractable = True):
    interpreter.process_page(page)
    string = retstr.getvalue()
    fstr += string
fp.close


device.close()
retstr.close()
print(fstr)
