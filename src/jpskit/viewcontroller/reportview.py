from django.shortcuts import render, get_list_or_404, redirect, reverse
from django.core.files.storage import FileSystemStorage
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from PyPDF2 import PdfFileReader, PdfFileWriter, pdf
import io
from io import BytesIO
import os
from django.http import FileResponse, Http404
from django.conf.urls.static import static
from django.conf import settings
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pdfjinja import PdfJinja



def some_pdf(request, idperolehan):

    from pdfjinja import PdfJinja

    pdfjinja = PdfJinja('static_in_env/assets/pdf/form.pdf')
    pdfout = pdfjinja(dict(firstName='salah nama', lastName='Valentine'))
    pdfout.write(open('static_in_env/assets/pdf/filled.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/filled.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()



    return render(request, 'pages/printtest.html' )

