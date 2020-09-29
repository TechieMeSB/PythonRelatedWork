import PyPDF2

inline1=open('Bell.pdf','rb')
pdfreader1=PyPDF2.PdfFileReader(inline1)
outfile=open('LabAssignment.pdf','wb')
pdfwriter=PyPDF2.PdfFileWriter()
for i in range(5):
    pdfwriter.addPage(pdfreader1.getPage(i))

inline2=open('1stprgm.pdf','rb')
pdfreader2=PyPDF2.PdfFileReader(inline2)
pdfwriter.addPage(pdfreader2.getPage(0))

inline3=open('CRC.pdf','rb')
pdfreader3=PyPDF2.PdfFileReader(inline3)
for i in range(5):
    pdfwriter.addPage(pdfreader3.getPage(i))

inline4=open('2ndprgm.pdf','rb')
pdfreader4=PyPDF2.PdfFileReader(inline4)
pdfwriter.addPage(pdfreader4.getPage(0))


pdfwriter.write(outfile)
inline2.close()
inline3.close()
inline4.close()
outfile.close()
inline1.close()
