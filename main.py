# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 18:40
# @Author  : Enmo Ren
# @FileName: main.py
# @Software: PyCharm


from fpdf import FPDF
import json

from error_handler import error_exit


class PDF(FPDF):
    def header(self):
        # Logo
        # self.image('logo_pb.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Ruina', 0, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')


def JSONtoPDF(filename: str, json_data: dict):
    # Get the data values from the JSON string json_data.
    try:
        data = json.loads(json_data)
    except Exception as e:
        error_exit("Invalid JSON data: {}".format(e.message))
    try:
        pdf = PDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for i, line in enumerate(data):
            content = f"{line}:{data[line]}"
            pdf.cell(200, 10, txt=content, ln=i, align="l")
        pdf.output(filename)
    except Exception as e:
        error_exit("Error while generating PDF file: {}".format(e.message))


def testJSONtoPDF(filename: str, json_content: str):
    json_data = json.dumps(json_content)
    JSONtoPDF(filename, json_data)


def main():
    json_test = {
        'pdf_filename': 'placeholder',
        'font_name': 'Courier',
        'font_size': 12,
        'header': 'The Man in the Arena',
        'footer': 'Generated by xtopdf - http://google.com/search?q=xtopdf',
        'lines': 'list_placeholder'
    }
    testJSONtoPDF('test.pdf', json_test)


if __name__ == '__main__':
    main()
