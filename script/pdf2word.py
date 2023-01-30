from pdf2docx import Converter


class Daily:
    def __init__(self):
        self.pdf_file = 'E:\\test.pdf'
        self.docx_file = 'E:\\test.docx'

    # convert pdf to docx
    def pdf2docx(self):
        cv = Converter(self.pdf_file)
        cv.convert(self.docx_file)  # all pages by default
        cv.close()


if __name__ == '__main__':
    daily = Daily()
    daily.pdf2docx()
