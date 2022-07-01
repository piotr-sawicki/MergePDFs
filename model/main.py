from PyPDF2 import PdfFileMerger
from PyQt5.QtWidgets import QPushButton, QFileDialog


def pdf_merge(output, *pdfs):
    merger = PdfFileMerger()
    for pdf in pdfs:
        try:
            merger.append(pdf)
        except FileNotFoundError:
            print('File {} not found and has been not added to the output file'.format(pdf))
    merger.write(output)
    merger.close()


class MergePDFs(QWidget):
    def __init__(self):
        super().__init__()





if __name__ == '__main__':

    print("\n\nTool merges multiple PDFs into a single PDF\n")

    output = input('Type name of output file: ')
    while not output.endswith('.pdf'):
        output = input(
            'Wrong output file name. Did you provided PDF extension for the output file?\nType again:')
    pdfs = []
    pdf = ''
    while pdf != 'X':
        pdf = input('Type name of input file or type X to finish input list: ')
        if pdf.endswith('.pdf'):
            pdfs.append(pdf)
        else:
            if pdf != 'X':
                print('Input file not added. PDF extension not provided')

    print('Output file:')
    print('    {}'.format(output))
    print('Input files:')
    if pdfs:
        for pdf in pdfs:
            print('    {}'.format(pdf))
        pdf_merge(output, *pdfs)
        print('\nMerging succeed!☺')