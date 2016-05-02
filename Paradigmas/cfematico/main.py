from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Image
import csv

comprobante = 'texto_comprobante.csv'


def importar(comprobante):
    attendee_data = csv.reader(open(comprobante, 'rb'))
    for fila in attendee_data:
        apellido = fila[0]

if __name__ == '__main__':
    print('ola')
