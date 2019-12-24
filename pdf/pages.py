import os
from PyPDF2 import PdfFileReader, PdfFileWriter

#PDF分页功能
#参数pdf文件位置 页数大小
def pdfPageingAndSize(filePath,pageSize=1):
    fileDir,fileName=os.path.split(filePath)
    fileNameExceptSuffix=fileName.split('.')[0]
    
    #创建输出文件夹
    fileDir = 'F:/mc_learn/pdf/test/all_page_file/'
    outputDir=str(fileNameExceptSuffix)+"_pdf_output_dir"
    os.mkdir(os.path.join(fileDir,outputDir))
    
    #输出文件夹的路径
    OutputDirFile=os.path.join(fileDir,outputDir)
    
    inputPdf = PdfFileReader(filePath, "rb")
    # 获得源PDF文件中页面总数
    pageNumber = inputPdf.getNumPages()
    print("页数：%d"%pageNumber)
    count=0
    output = PdfFileWriter()
    for index in range(pageNumber):
        count+=1
        output.addPage(inputPdf.getPage(index))
        outPdfName='1-'+str(count)+'.pdf'
        #每隔pageSize个页做一个pdf
        if(count%pageSize==0):
            outPdfName="pages-"+str(count-pageSize+1)+"-"+str(count)+'.pdf'
            outputStream = open(os.path.join(OutputDirFile, outPdfName), "wb")
            output.write(outputStream)
            outputStream.close()
            output = PdfFileWriter()
    #如果有些pdf不是pageSize的倍数，则需要单独保存
    if(pageNumber%pageSize):
        number=pageNumber%pageSize
        start=pageNumber-number+1
        end=pageNumber
        outPdfName="pages-"+str(start)
        if(start!=end):
            outPdfName=outPdfName+"-"+str(end)
        outPdfName=outPdfName+'.pdf'
        outputStream = open(os.path.join(OutputDirFile, outPdfName), "wb")
        output.write(outputStream)
        outputStream.close()

filenames = os.listdir('F:/mc_learn/pdf/test/pdf_file/')
for filename in filenames:
    filePath = 'F:/mc_learn/pdf/test/pdf_file/{}'.format(filename)
    pdfPageingAndSize(filePath, pageSize=1)