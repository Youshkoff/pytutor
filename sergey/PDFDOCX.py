from pdf2docx import Converter
pdf_file = 'F:\Копия Табель_ИЮНЬ_водители_СКВ1.pdf'
docx_file = 'F:\Копия Табель_ИЮНЬ_водители_СКВ1.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close
