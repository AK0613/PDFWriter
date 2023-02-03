import PyPDF2

template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))

output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)

# My solution
# def add_watermark(file, watermark_file):
#     # Specify reader object pointing to PDF file
#     reader = PdfFileReader(file)
#     writer = PdfFileWriter()
#     # Get all the pages
#     page = list(range(0, len(reader.pages)))
#     # Loop through all the pages and add it to content variable
#     for index in page:
#         content = reader.pages[index]
#         mediabox = content.mediaBox
#
#         stamp = PdfFileReader(watermark_file)
#         stamp_page = stamp.pages[0]
#
#         stamp_page.mergePage(content)
#         stamp_page.mediaBox = mediabox
#         writer.addPage(stamp_page)
#     with open('watermarked.pdf', 'wb') as file:
#         writer.write(file)
#
#
# inputs = sys.argv[1:]
#
# watermark_file = sys.argv[1]
#
# for pdf_file in inputs[1:]:
#     add_watermark(pdf_file, watermark_file)

# from PyPDF2 import PdfReader, PdfWriter

# with open('dummy.pdf', 'rb') as file:
#     reader = PdfReader('dummy.pdf')
#     page = reader.pages[0]
#     page.rotate(90)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer = PyPDF2.PdfWriter()
#         writer.add_page(page)
#         writer.write(new_file)

# Combine PDFs
# Creates a list of arguments (one or more)
# inputs = sys.argv[1:]
#
# print(inputs)
#
#
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         merger.append(pdf)
#     merger.write('super.pdf')
#
#
# pdf_combiner(inputs)

# Watermarking
