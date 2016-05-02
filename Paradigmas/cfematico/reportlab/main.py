from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Image
import csv

data_file = 'data.csv'


def import_data(data_file):
    attendee_data = csv.reader(open(data_file, 'rb'))
    for row in attendee_data:
        last_name = row[0]
        first_name = row[1]
        course_name = row[2]
        pdf_file_name = course_name + ' ' + last_name + first_name + '.pdf'
        generate_certificate(first_name, last_name, course_name, pdf_file_name)


def generate_certificate(first_name, last_name, course_name, pdf_file_name):
    attendee_name = first_name + ' ' + last_name
    c = canvas.Canvas(pdf_file_name, pagesize=landscape(letter))

    # Header text
    c.setFont('Helvetica', 48, leading=None)
    c.drawCentredString(415, 500, "Certificate Completion")
    c.setFont('Helvetica', 24, leading=None)
    c.drawCentredString(415, 450, "This certificate is presented to:")

    # Attendee name
    c.setFont('Helvetica-Bold', 34, leading=None)
    c.drawCentredString(415, 395, attendee_name)

    # For completing the ...
    c.setFont('Helvetica', 24, leading=None)
    c.drawCentredString(415, 350, "for completing the following course:")

    # Course name
    c.setFont('Helvetica', 20, leading=None)
    c.drawCentredString(415, 310, course_name)

    # Logo
    seal = 'seal.png'
    c.drawImage(seal, 350, 50, width=None, height=None)

    c.showPage()
    print "Imprimiendo"
    c.save()

if __name__ == '__main__':
    import_data(data_file)
