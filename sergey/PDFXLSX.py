# Import the required Module
import tabula
# Read a PDF File
df = tabula.read_pdf("F:\Копия Табель_ИЮНЬ_водители_СКВ1.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("F:\Копия Табель_ИЮНЬ_водители_СКВ1.pdf", "iplmatch.csv", output_format="csv", pages='all')
print(df)
