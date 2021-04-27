from django.shortcuts import render, get_list_or_404, redirect, reverse
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse, Http404
from django.conf.urls.static import static
from django.conf import settings
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.humanize.templatetags.humanize import intcomma
import datetime
from PyPDF2 import PdfFileReader, PdfFileWriter, pdf
import io
from io import BytesIO
import os
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pdfjinja import PdfJinja
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
from pdfjinja import PdfJinja
from tempfile import NamedTemporaryFile
from ..modelcontroller import document,dfnoperolehan,kontraktor,project, userprofile
from django.contrib.auth.models import User


def testexcel(request):
    
    wb = load_workbook('static_in_env/assets/excel/laporan.xlsx')
    for ws in wb.worksheets:
        print(ws.title)

    row_num = 7
    ws = wb.worksheets[0]
    thin_border = Border(left=Side(style='thin'), 
                     right=Side(style='thin'), 
                     top=Side(style='thin'), 
                     bottom=Side(style='thin'))
    
    columns = [
      '1', 
     'B13-28209',
     'PENYELENGGARAAN TERUSAN, TALIAIR TANAH/KONKRIT SERTA PARIT DIKAWASAN RANTAU PANJANG, SKIM PENGAIRAN KOTA II, DAERAH KUALA MUDA, KEDAH DARUL AMAN.',
     '61,775.11',
     '(1) FEBAH ENTERPRISE\n(2)JPSKMSB(KU/KM)S/B/OM/101/2020\n(3)22-09-2020 / 12-11-2020\n(4) 26-08-2020 / 21-10-2020 ',
     '20,000.00',
     '61,775.11',
     '80,000.00',
     '-16,680.00',
     '80,000.00',
     '100%',
    ]
    columns2 = [
      '1', 
     'B13-28209',
     'PENYELENGGARAAN TERUSAN, TALIAIR TANAH/KONKRIT SERTA PARIT DIKAWASAN RANTAU PANJANG, SKIM PENGAIRAN KOTA II, DAERAH KUALA MUDA, KEDAH DARUL AMAN.',
     '61,775.11',
     '(1) FEBAH ENTERPRISE\n(2)JPSKMSB(KU/KM)S/B/OM/101/2020\n(3)22-09-2020 / 12-11-2020\n(4) 26-08-2020 / 21-10-2020 ',
     '20,000.00',
     '61,775.11',
     '80,000.00',
     '-16,680.00',
     '80,000.00',
     '100%',
    ]
 
 
   
    for col_num in range(len(columns)):
        ws.cell(row_num, col_num+1, columns[col_num]).border = thin_border
        ws.cell(row_num+1, col_num+1, columns2[col_num]).border = thin_border
            
    
    wb.save("render.xlsx")
   

    return render(request, 'pages/someexcel.html')


def exceltest(request):
     
    wb = load_workbook('static_in_env/assets/excel/bookpython.xlsx')
    for ws in wb.worksheets:
        print(ws.title)
    
    row_num = 4
    ws = wb.worksheets[0]
    columns = ['Username', 'Line 1\nLine 2\nLine 3', 'Last name', 'Email address', ]
    columns1 = ['Username', 'Line 1\nLine 2\nLine 3', 'Last name', 'Email address', ]
   
    for col_num in range(len(columns)):
        ws.cell(row_num, col_num+2, columns[col_num])
        ws['C'+ str(row_num+range)].alignment = Alignment(wrapText=True)
        ws.cell(row_num+1, col_num+2, columns1[col_num])
    
    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.cell(row_num, col_num+2, row[col_num])
    
    wb.save("chart.xlsx")



def report_by_year(request):
    return render(request, 'pages/laporan_filter.html')

def some_pdf(request, idperolehan):

    dataobject = document.MRKSatu.objects.filter(mrksatunosebutharga=idperolehan).first()
    print("this is data object",dataobject.mrksatunoinden)

    pdfjinja = PdfJinja('static_in_env/assets/pdf/form.pdf')
    pdfout = pdfjinja(
        dict(
            firstname = dataobject.mrksatukontraktor.sijilPPKNoPendaftaran
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

#real dokument print began here

def pdfmrksatu(request, idperolehan):

    dataobject = document.MRKSatu.objects.filter(mrksatunosebutharga=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.mrksatunosebutharga.pegawaiselia.id).first()
    test = dataobject.mrksatukontraktor.sijilPPKNoPendaftaran
    print(test)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/MRK-01.pdf')
    pdfout = pdfjinja(
        dict(
            sijilpkk=dataobject.mrksatukontraktor.sijilPPKNoPendaftaran,
            kontraktor=dataobject.mrksatukontraktor.konNama,
            nokontrak=dataobject.mrksatunosebutharga.noperolehan,
            noinden=dataobject.mrksatunoinden,
            daereah=dataobject.mrksatukontraktor.konKawOperasi,
            negeri=dataobject.mrksatukontraktor.konNegeri,
            kosprojek=intcomma(dataobject.mrksatukosprojek),
            tarikhmula=dataobject.mrksatutarikhmula,
            tarikhjsiap=dataobject.mrksatutarikhjangkasiap,
            pegawai=userprofileL.user.first_name,
            jawatan=userprofileL.jawatan,
            tarikhlapo=dataobject.mrksatutarikhdaftar,
        ))

 
    pdfout.write(open('static_in_env/assets/pdf/outputpdf/MRK-01-'+test+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/MRK-01-'+test+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )


def pdfmrkdua(request, idperolehan):

    dataobject = document.MRKDua.objects.filter(mrkduanosebutharga=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.mrkduanosebutharga.pegawaiselia.id).first()
    test = dataobject.mrkduanosebutharga.noperolehan
    print(test)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/MRK-02.pdf')
    pdfout = pdfjinja(
        dict(
            nopkk = dataobject.mrksatulink.mrksatukontraktor.sijilPPKNoPendaftaran,
            kontraktor = dataobject.mrksatulink.mrksatukontraktor.konNama,
            nokontrak = dataobject.mrkduanosebutharga.noperolehan,
            noinden = dataobject.mrksatulink.mrksatunoinden,
            kosprojek = intcomma(dataobject.mrksatulink.mrksatukosprojek),
            tarikhmilik = dataobject.mrksatulink.mrksatutarikhmula,
            tarikhjangkasiap = dataobject.mrksatulink.mrksatutarikhjangkasiap,
            kemajuanprojek = dataobject.mrkduakerjajadual,
            kemajuankerjasebenar = dataobject.mrkduakerjasebenartarikh,
            sehingga = dataobject.mrkduakerjasebenar,
            nobayaran = dataobject.mrkduakemajuan,
            jumlahbayaran = intcomma(dataobject.mrkduabayarankemajuan),
            check1=dataobject.mrkduamodal,
            check2=dataobject.mkrduabahan,
            check3=dataobject.mrkduapekerja,
            check4=dataobject.mrkduatapak,
            check5=dataobject.mrkduacuaca,
            disebabkan = dataobject.mrkduadisebabkanoleh,
            lainlain = dataobject.mrkdualainlain,
            lanjutmasa = dataobject.mrkdualanjutmasa,
            lanjutdari = dataobject.mrkdualanjutdari,
            lanjuthingga = dataobject.mrkdualanjutsehingga,
            disebabkanoleh = dataobject.mrkduadisebabkan,
            lad = dataobject.mrkduaLAD,
            laddari = dataobject.mrkduaLADdari,
            ladhingga = dataobject.mrkduaLADSehingga,
            tarikhperakuan = dataobject.mrkduaperakuan,
            tarikhmansuh = dataobject.mrkduamansuh,

        ))

 
    pdfout.write(open('static_in_env/assets/pdf/outputpdf/MRK-02-'+test+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/MRK-02-'+test+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )

def pdflsk(request, idperolehan):

    dataobject = document.Laporansiapkerja.objects.filter(lsknosebutharga=idperolehan).first()
    projek = project.Projek.objects.filter(nosebuthargaid=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.lsknosebutharga.pegawaiselia.id).first()
 
    test = dataobject.lsknosebutharga.noperolehan
    print(test)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/Laporansiapkerja.pdf')
    pdfout = pdfjinja(
        dict(
            kontraktor = dataobject.lskmrksatulink.mrksatukontraktor.konNama,
            alamat1 = dataobject.lskmrksatulink.mrksatukontraktor.konAlamat,
            alamat2 = dataobject.lskmrksatulink.mrksatukontraktor.konAlamatExtS,
            poskod = dataobject.lskmrksatulink.mrksatukontraktor.konPoskod,
            bandar = dataobject.lskmrksatulink.mrksatukontraktor.konBandar,
            negeri = dataobject.lskmrksatulink.mrksatukontraktor.konNegeri,
            kerja = projek.tajukkerja,
            inden = dataobject.lskmrksatulink.mrksatunoinden,
            sebutharga = dataobject.lsknosebutharga.noperolehan,
            workmen = dataobject.lskperkeso,
            ins1 = dataobject.lsknoinsurancesatu,
            ins2 = dataobject.lsknoinsurancedua,
            peruntukan = dataobject.lskperuntukan,
            kosprojek = intcomma(dataobject.lskmrksatulink.mrksatukosprojek),
            hargasebenar = intcomma(dataobject.lskhargasebenar),
            tarikhmula = dataobject.lskmrksatulink.mrksatutarikhmula,
            tarikhtamat = dataobject.lskmrksatulink.mrksatutarikhjangkasiap,
            tarikhlanjutmasa = dataobject.lsklanjutmasa,
            tarikhsiapsem = dataobject.lskkerjasiap,
            laporan = dataobject.lsklaporan,
            tarikhakui = dataobject.lsktarikhperakui,
            penyelia = userprofileL.user.first_name,
            jawatan = userprofileL.jawatan,
            kb = dataobject.lskketuabahagian,
            jawatankb = dataobject.lskjawatanketuabahagian,
            jurutera = dataobject.lskjuruteraj41,
            jawatanjurutera = dataobject.lskjawatanj41,
            jd = dataobject.lskjuruteradaerah,
            jawatanjd = dataobject.lskjawatanjuruteradaerah,
        ))

 
    pdfout.write(open('static_in_env/assets/pdf/outputpdf/Laporansiapkerja-'+test+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/Laporansiapkerja-'+test+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )
    

    
