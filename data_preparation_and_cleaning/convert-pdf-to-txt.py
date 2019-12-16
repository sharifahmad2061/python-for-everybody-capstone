from sys import argv
import PyPDF2 as pdfr

filename = str(argv[1])
print(str(argv))
print('1: ', filename)
output_file = filename.split('.')[0]+'_self.txt'


def pdf_to_txt(file_name):
    pdf = pdfr.PdfFileReader(file_name, 'rb')
    with open(output_file, 'w') as txtfile:
        for page in range(pdf.getNumPages()):
            data = pdf.getPage(page).extractText()
            txtfile.write(data)


pdf_to_txt(filename)
