from django.shortcuts import render, get_list_or_404, redirect, reverse
from django.core.files.storage import FileSystemStorage
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from PyPDF2 import PdfFileReader, PdfFileWriter, pdf
import io
from io import BytesIO
import os
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from django.http import FileResponse, Http404
from django.conf.urls.static import static
from django.conf import settings
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pdfjinja import PdfJinja
from ..modelcontroller import document,dfnoperolehan,kontraktor,project

def some_pdf(request, idperolehan):

    dataobject = document.MRKSatu.objects.filter(mrksatunosebutharga=idperolehan).first()
    from pdfjinja import PdfJinja
    pdfjinja = PdfJinja('static_in_env/assets/pdf/form.pdf')
    pdfout = pdfjinja(
        dict(
            firstName=dataobject.mrksatukontraktor.konNama, 
            lastName='Valentine'
        ))
    pdfout.write(open('static_in_env/assets/pdf/filled.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/filled.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )

def some_excel(request, idperolehan):

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("static_in_env/assets/json/cred.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("jptest").sheet1  # Open the spreadhseet

    data = sheet.get_all_records()  # Get a list of all records
    print(data)

    return render(request, 'pages/printtest.html')

