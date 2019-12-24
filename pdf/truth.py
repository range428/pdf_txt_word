import os
import re

from pdfminer.pdfinterp import  PDFResourceManager,process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

#PDF TO TXT
def readPDF(pdffile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr,retstr,laparams=laparams)

    process_pdf(rsrcmgr,device,pdffile)
    device.close()

    content = retstr.getvalue()
    retstr.close()

    return content

def handleData(filename):
    file = open(outfilename + filename, 'r', encoding='utf-8')

    while True:
        line = file.readline()
        if not line:
            file.close()
            break

        elif line.find("Load bearing anchor") > -1 or line.find("Torsion anchor") > -1 or line.find("Pins") > -1:
            # print(line)
            with open('result/' + filename, 'a', encoding='utf8') as f:
                f.write(line)

outfilename = ''
foldername = 'F:/mc_learn/pdf/test/all_page_file'
folders = os.listdir('F:/mc_learn/pdf/test/all_page_file')
for folder in folders:
    path = 'F:/mc_learn/pdf/test/all_page_file/{}/'.format(folder)
    pdfList = os.listdir(path)
    os.mkdir('F:/mc_learn/pdf/test/txt/{}'.format(folder))
    for li in pdfList:
        pdffile = open(path + '/' + li, "rb")
        content = readPDF(pdffile)

        str = re.sub('.pdf', '.txt', li)
        file1 = 'F:/mc_learn/pdf/test/txt/{}/'.format(folder) + str
        with open( file1, 'w', encoding='utf8') as f:
            f.write(content)
        outfilename = 'F:/mc_learn/pdf/test/txt/{}/'.format(folder)

        handleData(str)