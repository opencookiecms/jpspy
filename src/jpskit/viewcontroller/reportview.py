from django.shortcuts import render, get_list_or_404, redirect, reverse
from django.core.files.storage import FileSystemStorage
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from PyPDF2 import PdfFileReader, PdfFileWriter, pdf
import io
from io import BytesIO
import os
from django.http import FileResponse
from django.conf.urls.static import static
from django.conf import settings
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter



def some_pdf(request, idperolehan):


    doc = SimpleDocTemplate("/tmp/MRK-02.pdf")
    styles = getSampleStyleSheet()
    Story = [Spacer(1,2*inch)]
    style = styles["Normal"]
    for i in range(100):
       bogustext = ("This is Paragraph number %s.  " % i) * 20
       p = Paragraph(bogustext, style)
       Story.append(p)
       Story.append(Spacer(1,0.2*inch))
    doc.build(Story)

    fs = FileSystemStorage("/tmp")
    with fs.open("MRK-02.pdf") as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
        return response

    return response

