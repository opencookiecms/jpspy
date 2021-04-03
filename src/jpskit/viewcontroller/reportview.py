from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from PyPDF2 import PdfFileReader
import io
import os
from django.http import FileResponse
from reportlab.pdfgen import canvas


def some_pdf(request):

 

    
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(500,500, "Hello world")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


