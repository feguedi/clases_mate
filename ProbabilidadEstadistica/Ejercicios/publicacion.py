# -*- coding: utf-8 -*-
__author__ = 'nger'
from fpdf import FPDF as pcdmx
import os


class PDF(pcdmx):
    def header(self):
        # Logo
        self.image(os.access('~/Imágenes/Escudo_Informatica.png', os.R_OK), 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '\{nb}', 0, 0, 'C')

pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)
for i in range(1, 41):
    pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
pdf.output('tuto1.pdf', 'F')
