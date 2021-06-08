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
from ..modelcontroller import document, dfnoperolehan, kontraktor, project, userprofile
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
            
    
    wb.save("render2.xlsx")
   

    return render(request, 'pages/someexcel.html')

def testexcel2(request):

    wb = load_workbook('static_in_env/assets/excel/laporan.xlsx')
    for ws in wb.worksheets:
        print(ws.title)

    row_num = 6
    ws = wb.worksheets[0]
    thin_border = Border(left=Side(style='thin'), 
                     right=Side(style='thin'), 
                     top=Side(style='thin'), 
                     bottom=Side(style='thin'))

    data = document.MRKSatu.objects.all()


    for datas in data:

        r1 = project.Projek.objects.filter(nosebuthargaid=datas.mrksatunosebutharga).first()

        columns = ["num"]
        columns1 = [datas.mrksatunoinden]
        columns2 = [r1.tajukkerja]
        columns3 = ["empty"]


        for col_num in range(len(columns)):   
            
            print(col_num)
            row_num +=1
            ws.cell(row_num, col_num+1, columns[col_num]).border = thin_border
            ws.cell(row_num, col_num+2, columns1[col_num]).border = thin_border
            ws.cell(row_num, col_num+3, columns2[col_num]).border = thin_border
            ws.cell(row_num, col_num+4, columns3[col_num]).border = thin_border
            wb.save("render2.xlsx")
        

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


def pdfmrktiga(request, idperolehan):

    dataobject = document.MRKTiga.objects.filter(mrktigasebutharga=idperolehan).first()
    projek = project.Projek.objects.filter(nosebuthargaid=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.mrktigasebutharga.pegawaiselia.id).first()
    lskfetch = document.Laporansiapkerja.objects.filter(lsknosebutharga=idperolehan).first()
    mrkduaf = document.MRKDua.objects.filter(mrkduanosebutharga=idperolehan).first()
 
    test = dataobject.mrktigasebutharga.noperolehan
    print(test)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/MRK03.pdf')
    pdfout = pdfjinja(
        dict(
            pkk = dataobject.marktigamrksatu.mrksatukontraktor.sijilPPKNoPendaftaran,
            kontraktor =dataobject.marktigamrksatu.mrksatukontraktor.konNama,
            sebutharga =dataobject.mrktigasebutharga.noperolehan,
            inden = dataobject.marktigamrksatu.mrksatunoinden,
            tajuk = projek.tajukkerja,
            kosprojek = intcomma(dataobject.marktigamrksatu.mrksatukosprojek),
            kossebenar = intcomma(lskfetch.lskhargasebenar),
            tarikhmula = dataobject.marktigamrksatu.mrksatutarikhmula,
            tarikhakhir =lskfetch.lskkerjasiap,
            lanjuthingga = lskfetch.lsklanjutmasa,
            tarikhsiapsebenar =lskfetch.lskkerjasiap,
            lad =mrkduaf.mrkduaLAD,
            laddari =mrkduaf.mrkduaLADdari,
            ladhingga =mrkduaf.mrkduaLADSehingga,
            c1a = dataobject.mrktigabina,
            c1b = dataobject.mrktigabina,
            c1c = dataobject.mrktigabina,
            c1d = dataobject.mrktigabina,
            c2a = dataobject.mrktigatadbir,
            c2b = dataobject.mrktigatadbir,
            c2c = dataobject.mrktigatadbir,
            c2d = dataobject.mrktigatadbir,
            c3a = dataobject.mrktigakemajuan,
            c3b = dataobject.mrktigakemajuan,
            c3c = dataobject.mrktigakemajuan,
            c3d = dataobject.mrktigakemajuan,
            c4a = dataobject.mkrtigamutukerangka,
            c4b = dataobject.mkrtigamutukerangka,
            c4c = dataobject.mkrtigamutukerangka,
            c4d = dataobject.mkrtigamutukerangka,
            c5a = dataobject.mrktigamutukerja,
            c5b = dataobject.mrktigamutukerja,
            c5c = dataobject.mrktigamutukerja,
            c5d = dataobject.mrktigamutukerja,
            c6a = dataobject.mrktigamutukemasan,
            c6b = dataobject.mrktigamutukemasan,
            c6c = dataobject.mrktigamutukemasan,
            c6d = dataobject.mrktigamutukemasan,
            c7a = dataobject.mrktigamutukerjaluar,
            c7b = dataobject.mrktigamutukerjaluar,
            c7c = dataobject.mrktigamutukerjaluar,
            c7d = dataobject.mrktigamutukerjaluar,
            c8a = dataobject.mrktigapegawasan,
            c8b = dataobject.mrktigapegawasan,
            c8c = dataobject.mrktigapegawasan,
            c8d = dataobject.mrktigapegawasan,
            catat1 = dataobject.mrkcatat1,
            catat2 = dataobject.mrkcatat2,
            catat3 = dataobject.mrkcatat3,
            catat4 = dataobject.mrkcatat4,
            catat5 = dataobject.mrkcatat5,
            catat6 = dataobject.mrkcatat6,
            catat7 = dataobject.mrkcatat7,
            catat8 = dataobject.mrkcatat8,
            ulasan =dataobject.mrktigasokongan,
        ))

 
    pdfout.write(open('static_in_env/assets/pdf/outputpdf/MRK03-'+test+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/MRK03-'+test+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )


def pdfpsksatu(request, idperolehan):

    dataobject = document.PSK.objects.filter(psknosebutharga=idperolehan).first()
    projek = project.Projek.objects.filter(nosebuthargaid=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.psknosebutharga.pegawaiselia.id).first()
    lskfetch = document.Laporansiapkerja.objects.filter(lsknosebutharga=idperolehan).first()
    mrkduaf = document.MRKDua.objects.filter(mrkduanosebutharga=idperolehan).first()
 
    test = dataobject.psknosebutharga.noperolehan
    print(test)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/PSK01.pdf')
    pdfout = pdfjinja(
        dict(

            sebutharga = dataobject.psknosebutharga.noperolehan,
            kontraktor = dataobject.pskmrksatulink.mrksatukontraktor.konNama,
            alamat1 = dataobject.pskmrksatulink.mrksatukontraktor.konAlamat,
            alamat2 = dataobject.pskmrksatulink.mrksatukontraktor.konAlamatExtS,
            poskod = dataobject.pskmrksatulink.mrksatukontraktor.konPoskod,
            bandar = dataobject.pskmrksatulink.mrksatukontraktor.konBandar,
            negeri = dataobject.pskmrksatulink.mrksatukontraktor.konNegeri,
            gred = dataobject.pskmrksatulink.mrksatugred,
            tajukkerja = projek.tajukkerja,
            hargasebenar = intcomma(lskfetch.lskhargasebenar),
            tarikhsebenar = lskfetch.lskkerjasiap,
            tarikhambil = dataobject.psktarikhambilmilik,
            mulacacat = dataobject.psktarikhmulatanggug,
            akhircacat = dataobject.psktarikhtamattanggung,
            jurutere = dataobject.pskmrksatulink.mrksatunosebutharga.pegawaiselia.first_name,
  
        ))

 
    pdfout.write(open('static_in_env/assets/pdf/outputpdf/PSK01-'+test+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/PSK01-'+test+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )



def pdfpskdua(request, idperolehan):

    dataobject = document.PSK.objects.filter(psknosebutharga=idperolehan).first()
    projek = project.Projek.objects.filter(nosebuthargaid=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.psknosebutharga.pegawaiselia.id).first()
    lskfetch = document.Laporansiapkerja.objects.filter(lsknosebutharga=idperolehan).first()
    mrkduaf = document.MRKDua.objects.filter(mrkduanosebutharga=idperolehan).first()
 
    test = dataobject.psknosebutharga.noperolehan
    print(test)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/PKS02.pdf')
    pdfout = pdfjinja(
        dict(

            sebutharga = dataobject.psknosebutharga.noperolehan,
            kontraktor = dataobject.pskmrksatulink.mrksatukontraktor.konNama,
            alamat1 = dataobject.pskmrksatulink.mrksatukontraktor.konAlamat,
            alamat2 = dataobject.pskmrksatulink.mrksatukontraktor.konAlamatExtS,
            poskod = dataobject.pskmrksatulink.mrksatukontraktor.konPoskod,
            bandar = dataobject.pskmrksatulink.mrksatukontraktor.konBandar,
            negeri = dataobject.pskmrksatulink.mrksatukontraktor.konNegeri,
            gred = dataobject.pskmrksatulink.mrksatugred,
            tajukkerja = projek.tajukkerja,
            hargasebenar = intcomma(lskfetch.lskhargasebenar),
            tarikhsebenar = lskfetch.lskkerjasiap,
            tarikhambil = dataobject.psktarikhambilmilik,
            mulacacat = dataobject.psktarikhmulatanggug,
            akhircacat = dataobject.psktarikhtamattanggung,
            jurutere = dataobject.pskmrksatulink.mrksatunosebutharga.pegawaiselia.first_name,
  
        ))

 
    pdfout.write(open('static_in_env/assets/pdf/outputpdf/PKS02-'+test+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/PKS02-'+test+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )


def ssemak(request, idperolehan):

    dataobject = document.SenaraiSemakan.objects.filter(ssnosebutharga=idperolehan).first()
    projek = project.Projek.objects.filter(nosebuthargaid=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.ssnosebutharga.pegawaiselia.id).first()
    lskfetch = document.Laporansiapkerja.objects.filter(lsknosebutharga=idperolehan).first()
    mrkduaf = document.MRKDua.objects.filter(mrkduanosebutharga=idperolehan).first()
 
    idsebutharga = dataobject.ssnosebutharga.id
    print(idsebutharga)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/SS.pdf')
    pdfout = pdfjinja(
        dict(
            check1 = dataobject.ssinden,
            check2 = dataobject.sslsk,
            check3 = dataobject.ssti,
            check4 = dataobject.sssebutharga,
            check5 = dataobject.sspt,
            check6 = dataobject.ssjs,
            check7 = dataobject.sskts,
            check8 = dataobject.ssds,
            check9 = dataobject.ssplm,
            check10 = dataobject.ssab,
            check11 = dataobject.sscidb,
            check12 = dataobject.sspkk,
            check13 = dataobject.ssssm,
            check14 = dataobject.sskk,
            check15 = dataobject.ssinsurance,
            check16 = dataobject.ssgambar,
            pegawai = dataobject.ssnosebutharga.pegawaiselia.first_name,
            tarikh = dataobject.sstarikh
        ))

 
    pdfout.write(open('static_in_env/assets/pdf/outputpdf/SS-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/SS-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )


def pdfpsmk(request, idperolehan):

    dataobject = document.PSMK.objects.filter(psmknosebutharga=idperolehan).first()
    projek = project.Projek.objects.filter(nosebuthargaid=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.psmknosebutharga.pegawaiselia.id).first()
    lskfetch = document.Laporansiapkerja.objects.filter(lsknosebutharga=idperolehan).first()
 
    idsebutharga = dataobject.psmknosebutharga.id
    print(idsebutharga)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/PSMK.pdf')
    pdfout = pdfjinja(
        dict(

            kontrator = dataobject.psmkmrksatulink.mrksatukontraktor.konNama,
            alamat1 = dataobject.psmkmrksatulink.mrksatukontraktor.konAlamat,
            alamat2 = dataobject.psmkmrksatulink.mrksatukontraktor.konAlamatExtS,
            poskod = dataobject.psmkmrksatulink.mrksatukontraktor.konPoskod,
            bandar = dataobject.psmkmrksatulink.mrksatukontraktor.konBandar,
            negeri = dataobject.psmkmrksatulink.mrksatukontraktor.konNegeri,
            gred = dataobject.psmkmrksatulink.mrksatugred,
            sebutharga = dataobject.psmknosebutharga.noperolehan,
            tajuk = projek.tajukkerja,
            tarikhgagal = lskfetch.lskkerjasiap,
            g1 = dataobject.psmknojaminanbanka,
            hargaa = intcomma(dataobject.psmkhargajaminana),
            bakia = intcomma(dataobject.psmkbakiwangjaminana),
            g2 = dataobject.psmknojaminanbankab,
            hargab = intcomma(dataobject.psmkhargajaminanb),
            wangb = intcomma(dataobject.psmkbakiwangjaminanb),
            kosbon = intcomma(dataobject.psmkkosbon),
            bakikosbon = intcomma(dataobject.psmkbakikos),
            pegawai = userprofileL.user.first_name,
            jawatan = userprofileL.jawatan,
        ))

 
    pdfout.write(open('static_in_env/assets/pdf/outputpdf/PSMK-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/PSMK-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )


def pdfjb(request, idperolehan):

    dataobject = document.SuratPJaminanbank.objects.filter(jbankknosebutharga=idperolehan).first()
    projek = project.Projek.objects.filter(nosebuthargaid=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.jbankknosebutharga.pegawaiselia.id).first()
    lskfetch = document.Laporansiapkerja.objects.filter(lsknosebutharga=idperolehan).first()
    psk  = document.PSK.objects.filter(psknosebutharga=idperolehan).first()
 
    idsebutharga = dataobject.jbankknosebutharga.id
    print(idsebutharga)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/jb.pdf')
    pdfout = pdfjinja(
        dict(
            namabank = dataobject.namabank,
            alamatbank = dataobject.alamatbank,
            akaunbank = dataobject.rujukanbank,
            kontraktor = dataobject.jbankmrksatulink.mrksatukontraktor.konNama,
            alamat = dataobject.alamatpemborongsurat,
            tarikha = psk.psktarikhmulatanggug,
            tarikhb = psk.psktarikhtamattanggung,
            jurutera = userprofileL.user.first_name,
            jawatan = userprofileL.jawatan,

 
        ))

 
    pdfout.write(open('static_in_env/assets/pdf/outputpdf/jb-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/jb-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )


def pdfppwjp(request, idperolehan):

    dataobject = document.Perakuanpwjp.objects.filter(wjpknosebutharga=idperolehan).first()
    projek = project.Projek.objects.filter(nosebuthargaid=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.wjpknosebutharga.pegawaiselia.id).first()
    lskfetch = document.Laporansiapkerja.objects.filter(lsknosebutharga=idperolehan).first()
    psk  = document.PSK.objects.filter(psknosebutharga=idperolehan).first()
 
    idsebutharga = dataobject.wjpknosebutharga.id
    print(idsebutharga)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/ppwjp.pdf')
    pdfout = pdfjinja(
        dict(
            namarujukan = dataobject.namarujukan,
            alamtrujukan = dataobject.alamatrujukan,
            kontraktor = dataobject.wjpmrksatulink.mrksatukontraktor.konNama,
            projek = projek.tajukkerja,
            rm = dataobject.koswjp,
            jurutera = dataobject.wjppegawai,
            jawatan = dataobject.wjpjawatan,
        ))

 
    pdfout.write(open('static_in_env/assets/pdf/outputpdf/ppwjp-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/ppwjp-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )

def pdfsmrksatu(request, idperolehan):

    dataobject = document.SuratMRK.objects.filter(smrkknosebutharga=idperolehan).first()
    projek = project.Projek.objects.filter(nosebuthargaid=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.smrkknosebutharga.pegawaiselia.id).first()
    lskfetch = document.Laporansiapkerja.objects.filter(lsknosebutharga=idperolehan).first()
    psk  = document.PSK.objects.filter(psknosebutharga=idperolehan).first()
 
    idsebutharga = dataobject.smrkknosebutharga.id
    print(idsebutharga)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/spkk1.pdf')
    pdfout = pdfjinja(
        dict(

            namarujukan = dataobject.smrknamarujukan,
            alamatrujukan =dataobject.smkralamatrujukan,
            jenisborang = dataobject.smrkjenisborang,
            kontraktor = dataobject.smrkmrksatulink.mrksatukontraktor.konNama,
            nopkk = dataobject.smrkmrksatulink.mrksatukontraktor.sijilPPKNoPendaftaran,
            norujukan = dataobject.smrkrujukantuan,
            pegawai = dataobject.smrkpegawai,
            jawatan = dataobject.smrkjawatan,
    
        ))


    pdfout.write(open('static_in_env/assets/pdf/outputpdf/spkk1-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/spkk1-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )



def pdfsmrkdua(request, idperolehan):

    dataobject = document.SuratMRK.objects.filter(smrkknosebutharga=idperolehan).first()
    projek = project.Projek.objects.filter(nosebuthargaid=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.smrkknosebutharga.pegawaiselia.id).first()
    lskfetch = document.Laporansiapkerja.objects.filter(lsknosebutharga=idperolehan).first()
    psk  = document.PSK.objects.filter(psknosebutharga=idperolehan).first()
 
    idsebutharga = dataobject.smrkknosebutharga.id
    print(idsebutharga)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/spkk2.pdf')
    pdfout = pdfjinja(
        dict(
            namarujukan = dataobject.smrknamarujukan,
            alamatrujukan =dataobject.smkralamatrujukan,
            jenisborang = dataobject.smrkjenisborang,
            kontraktor = dataobject.smrkmrksatulink.mrksatukontraktor.konNama,
            nopkk = dataobject.smrkmrksatulink.mrksatukontraktor.sijilPPKNoPendaftaran,
            norujukan = dataobject.smrkrujukantuan,
            pegawai = dataobject.smrkpegawai,
            jawatan = dataobject.smrkjawatan,
            tarikh = dataobject.smrktarikh,
        ))

 
    pdfout.write(open('static_in_env/assets/pdf/outputpdf/spkk2-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/spkk2-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )



def pdfskhas01(request, idperolehan):

    dataobject = document.SuratKhas.objects.filter(khasknosebutharga=idperolehan).first()
    projek = project.Projek.objects.filter(nosebuthargaid=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.khasknosebutharga.pegawaiselia.id).first()
    lskfetch = document.Laporansiapkerja.objects.filter(lsknosebutharga=idperolehan).first()
    psk  = document.PSK.objects.filter(psknosebutharga=idperolehan).first()
 
    idsebutharga = dataobject.khasknosebutharga.id
    print(idsebutharga)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/skhas01.pdf')
    pdfout = pdfjinja(
        dict(
            rujukantuan = dataobject.khasrujukantuan,
            rujukan = dataobject.khasknosebutharga,
            namarujukan = dataobject.khasnamarujukan,
            alamatrujukan =dataobject.khasalamatrujukan,
            gred = dataobject.khasmrksatulink.mrksatugred,
            kategori = dataobject.khasmrksatulink.mrksatukategori,
            khusus  = dataobject.khasmrksatulink.mrksatupengkhususan,
            kontraktor = dataobject.khasmrksatulink.mrksatukontraktor.konNama,
            projek = projek.tajukkerja,
            jurutera = dataobject.khasmrksatulink.mrksatunosebutharga.pegawaiselia.first_name,
            jawatan = userprofileL.jawatan,

        ))

 
    pdfout.write(open('static_in_env/assets/pdf/outputpdf/skhas01-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/skhas01-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )

def pdfskhas02(request, idperolehan):

    dataobject = document.SuratKhas.objects.filter(khasknosebutharga=idperolehan).first()
    projek = project.Projek.objects.filter(nosebuthargaid=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.khasknosebutharga.pegawaiselia.id).first()
    lskfetch = document.Laporansiapkerja.objects.filter(lsknosebutharga=idperolehan).first()
    psk  = document.PSK.objects.filter(psknosebutharga=idperolehan).first()
 
    idsebutharga = dataobject.khasknosebutharga.id
    print(idsebutharga)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/skhas02.pdf')
    pdfout = pdfjinja(
        dict(
            rujukantuan = dataobject.khasrujukantuan,
            rujukan = dataobject.khasknosebutharga,
            namarujukan = dataobject.khasnamarujukan,
            alamatrujukan =dataobject.khasalamatrujukan,
            gred = dataobject.khasmrksatulink.mrksatugred,
            kategori = dataobject.khasmrksatulink.mrksatukategori,
            khusus  = dataobject.khasmrksatulink.mrksatupengkhususan,
            kontraktor = dataobject.khasmrksatulink.mrksatukontraktor.konNama,
            projek = projek.tajukkerja,
            jurutera = dataobject.khasmrksatulink.mrksatunosebutharga.pegawaiselia.first_name,
            jawatan = userprofileL.jawatan,
        ))

 
    pdfout.write(open('static_in_env/assets/pdf/outputpdf/skhas02-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/skhas02-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )

def pdfpwjp01(request, idperolehan):

    dataobject = document.SuratPelepasanBon.objects.filter(bonknosebutharga=idperolehan).first()
    projek = project.Projek.objects.filter(nosebuthargaid=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.bonknosebutharga.pegawaiselia.id).first()
    lskfetch = document.Laporansiapkerja.objects.filter(lsknosebutharga=idperolehan).first()
    psk  = document.PSK.objects.filter(psknosebutharga=idperolehan).first()
 
    idsebutharga = dataobject.bonknosebutharga.id
    print(idsebutharga)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/spwjp.pdf')
    pdfout = pdfjinja(
        dict(
          
            rujukan = dataobject.bonknosebutharga,
            kepada = dataobject.bonkepada,
            alamatkepada =dataobject.bonalamatsatu,
            kontraktor = dataobject.bonmrksatulink.mrksatukontraktor.konNama,
            kepada2 = dataobject.bonmelalui,
            alamatkepada2 = dataobject.bonalamatdua,
            jurutera = dataobject.bonmrksatulink.mrksatunosebutharga.pegawaiselia.first_name,
            jawatan = userprofileL.jawatan,
            kosbon = intcomma(dataobject.bonwangjaminan),
      
        ))

 
    pdfout.write(open('static_in_env/assets/pdf/outputpdf/spwjp-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/spwjp-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )


def pdfpwjp02(request, idperolehan):

    dataobject = document.SuratPelepasanBon.objects.filter(bonknosebutharga=idperolehan).first()
    projek = project.Projek.objects.filter(nosebuthargaid=idperolehan).first()
    userprofileL = userprofile.UserProfile.objects.filter(id=dataobject.bonknosebutharga.pegawaiselia.id).first()
    lskfetch = document.Laporansiapkerja.objects.filter(lsknosebutharga=idperolehan).first()
    psk  = document.PSK.objects.filter(psknosebutharga=idperolehan).first()
 
    idsebutharga = dataobject.bonknosebutharga.id
    print(idsebutharga)
 
    pdfjinja = PdfJinja('static_in_env/assets/pdf/spwjp02.pdf')
    pdfout = pdfjinja(
        dict(
            
            rujukan = dataobject.bonknosebutharga,
            kepada = dataobject.bonkepada,
            alamatkepada =dataobject.bonalamatsatu,
            kontraktor = dataobject.bonmrksatulink.mrksatukontraktor.konNama,
            kepada2 = dataobject.bonmelalui,
            alamatkepada2 = dataobject.bonalamatdua,
            jurutera = dataobject.bonmrksatulink.mrksatunosebutharga.pegawaiselia.first_name,
            jawatan = userprofileL.jawatan,
            kosbon = intcomma(dataobject.bonwangjaminan),
      
        ))

 
    pdfout.write(open('static_in_env/assets/pdf/outputpdf/spwjp02-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'wb'))
    try:
        return FileResponse(open('static_in_env/assets/pdf/outputpdf/spwjp02-'+str(idsebutharga)+'-'+userprofileL.user.first_name+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/printtest.html' )


##filter the report

def report_by_year(request):

    kaedah = request.GET.get('kaedah')

    qs = document.MRKSatu.objects.raw()
    
    context = {
        'test':"TEst"
    }
    
    return render(request, 'pages/laporan_filter.html',context)
    
    
    
    
    
    
    
    
    

    
