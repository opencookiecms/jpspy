# Generated by Django 3.1.2 on 2021-01-28 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='isSungai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sg_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sg_cabang', models.CharField(blank=True, max_length=50, null=True)),
                ('sg_pangjang', models.CharField(blank=True, max_length=50, null=True)),
                ('sg_daerah', models.CharField(blank=True, max_length=50, null=True)),
                ('sg_noshet', models.CharField(blank=True, max_length=50, null=True)),
                ('sg_norujukan', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kontraktor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('konNama', models.CharField(blank=True, max_length=100, null=True)),
                ('konImage', models.FileField(blank=True, null=True, upload_to='')),
                ('konAlamat', models.CharField(blank=True, max_length=200, null=True)),
                ('konAlamatExtS', models.CharField(blank=True, max_length=50, null=True)),
                ('konAlamatExtD', models.CharField(blank=True, max_length=20, null=True)),
                ('konPoskod', models.CharField(blank=True, max_length=10, null=True)),
                ('konBandar', models.CharField(blank=True, max_length=20, null=True)),
                ('konDaerah', models.CharField(blank=True, max_length=20, null=True)),
                ('konNegeri', models.CharField(blank=True, max_length=20, null=True)),
                ('konTel', models.CharField(blank=True, max_length=20, null=True)),
                ('konEmail', models.CharField(blank=True, max_length=150, null=True)),
                ('konFax', models.CharField(blank=True, max_length=20, null=True)),
                ('konBank', models.CharField(blank=True, max_length=50, null=True)),
                ('konNoAkaun', models.CharField(blank=True, max_length=50, null=True)),
                ('konKawOperasi', models.CharField(blank=True, max_length=20, null=True)),
                ('konPrestasi', models.CharField(blank=True, max_length=10, null=True)),
                ('konPengurus', models.CharField(blank=True, max_length=150, null=True)),
                ('konNoKPPengurus', models.CharField(blank=True, max_length=20, null=True)),
                ('konNoTelPengurus', models.CharField(blank=True, max_length=20, null=True)),
                ('konRKsatu', models.CharField(blank=True, max_length=150, null=True)),
                ('konRKsatuNokp', models.CharField(blank=True, max_length=20, null=True)),
                ('konRKsatuNoTel', models.CharField(blank=True, max_length=20, null=True)),
                ('konRKdua', models.CharField(blank=True, max_length=150, null=True)),
                ('konRKduaNokp', models.CharField(blank=True, max_length=20, null=True)),
                ('konRKduaNoTel', models.CharField(blank=True, max_length=20, null=True)),
                ('konRKtiga', models.CharField(blank=True, max_length=150, null=True)),
                ('konRKtigaNokp', models.CharField(blank=True, max_length=20, null=True)),
                ('konRKtigaNoTel', models.CharField(blank=True, max_length=20, null=True)),
                ('konRKempat', models.CharField(blank=True, max_length=150, null=True)),
                ('konRKempatNokp', models.CharField(blank=True, max_length=20, null=True)),
                ('konRKempatNoTel', models.CharField(blank=True, max_length=20, null=True)),
                ('konJPBaru', models.CharField(blank=True, max_length=150, null=True)),
                ('konJPPembaharuan', models.CharField(blank=True, max_length=20, null=True)),
                ('konJPLainLain', models.CharField(blank=True, max_length=20, null=True)),
                ('konJPKategori', models.CharField(blank=True, max_length=20, null=True)),
                ('konMPTarikhMohon', models.CharField(blank=True, max_length=20, null=True)),
                ('konMPCas', models.CharField(blank=True, max_length=200, null=True)),
                ('konMPNoResit', models.CharField(blank=True, max_length=150, null=True)),
                ('konMPNoSijil', models.CharField(blank=True, max_length=50, null=True)),
                ('konMPtarikhkeluar', models.CharField(blank=True, max_length=50, null=True)),
                ('konMPtarikhtamat', models.CharField(blank=True, max_length=50, null=True)),
                ('konMPdisemak', models.CharField(blank=True, max_length=50, null=True)),
                ('konMPjawatansemak', models.CharField(blank=True, max_length=50, null=True)),
                ('konMPdisah', models.CharField(blank=True, max_length=50, null=True)),
                ('konMPjawatansah', models.CharField(blank=True, max_length=50, null=True)),
                ('konMPlulus', models.CharField(blank=True, max_length=50, null=True)),
                ('konMPjawatanlulus', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKNoPendaftaran', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKSahDari', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKTamat', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKGredSatu', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKKatSatu', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKKhuSatu', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKGredDua', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKKatDua', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKKhuDua', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKGredTiga', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKKatTiga', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKKhuTiga', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKNoPendaftaran', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKSahDari', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKTamat', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKGredSatu', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKKatSatu', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKKhuSatu', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKGredDua', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKKatDua', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKKhuDua', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKGredTiga', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKKatTiga', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKKhuTiga', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSTBNoPendaftaran', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSTBSahDari', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSTBTamat', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSTBGred', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSSMNoPendaftaran', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSSMSahDari', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSSMTamat', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSSTNoPendaftaran', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSSTSahDari', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSSTTamat', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilJPSNoPendaftaran', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilJPSSahDari', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilJPSTamat', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilJPSGred', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MRK2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NoPerolehan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noperolehan', models.CharField(blank=True, max_length=100, null=True)),
                ('tarikh', models.CharField(blank=True, max_length=50, null=True)),
                ('kaedahperolehan', models.CharField(blank=True, max_length=50, null=True)),
                ('pegawaiselia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_sebutharga', models.CharField(blank=True, max_length=150, null=True)),
                ('o_tarikh', models.CharField(blank=True, max_length=50, null=True)),
                ('o_permilik', models.CharField(blank=True, max_length=150, null=True)),
                ('o_jenis', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sistem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistemname', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jawatan', models.CharField(blank=True, max_length=50, null=True)),
                ('gredjawatan', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='subsistem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsistemname', models.CharField(blank=True, max_length=50, null=True)),
                ('sistemlink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jpskit.sistem')),
            ],
        ),
        migrations.CreateModel(
            name='Projek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tajukkerja', models.CharField(blank=True, max_length=50, null=True)),
                ('daerah', models.CharField(blank=True, max_length=50, null=True)),
                ('pgred', models.CharField(blank=True, max_length=50, null=True)),
                ('pkategori', models.CharField(blank=True, max_length=50, null=True)),
                ('pkhususan1', models.CharField(blank=True, max_length=50, null=True)),
                ('pkhususan2', models.CharField(blank=True, max_length=50, null=True)),
                ('pkhususan3', models.CharField(blank=True, max_length=50, null=True)),
                ('ptaraf', models.CharField(blank=True, max_length=50, null=True)),
                ('ptempohsiap', models.CharField(blank=True, max_length=50, null=True)),
                ('pweekormonth', models.CharField(blank=True, max_length=50, null=True)),
                ('hargadukumen', models.CharField(blank=True, max_length=50, null=True)),
                ('tarikhnotis', models.CharField(blank=True, max_length=50, null=True)),
                ('tariklawattapak', models.CharField(blank=True, max_length=50, null=True)),
                ('tarikhdukemenjual', models.CharField(blank=True, max_length=50, null=True)),
                ('tarikhakhirdukemenjual', models.CharField(blank=True, max_length=50, null=True)),
                ('tarikhtutupsebutharga', models.CharField(blank=True, max_length=50, null=True)),
                ('pjuruteradearah', models.CharField(blank=True, max_length=50, null=True)),
                ('pjurutera', models.CharField(blank=True, max_length=50, null=True)),
                ('pjuruterakanan36', models.CharField(blank=True, max_length=50, null=True)),
                ('pjurutera29', models.CharField(blank=True, max_length=50, null=True)),
                ('kodvot', models.CharField(blank=True, max_length=50, null=True)),
                ('peruntukan', models.CharField(blank=True, max_length=50, null=True)),
                ('peruntukansemasa', models.CharField(blank=True, max_length=50, null=True)),
                ('latitud1', models.CharField(blank=True, max_length=50, null=True)),
                ('latitud2', models.CharField(blank=True, max_length=50, null=True)),
                ('latitud3', models.CharField(blank=True, max_length=50, null=True)),
                ('longlitud1', models.CharField(blank=True, max_length=50, null=True)),
                ('longlitud2', models.CharField(blank=True, max_length=50, null=True)),
                ('longlitud3', models.CharField(blank=True, max_length=50, null=True)),
                ('lembangansungai', models.CharField(blank=True, max_length=50, null=True)),
                ('sistem', models.CharField(blank=True, max_length=50, null=True)),
                ('subsistem', models.CharField(blank=True, max_length=50, null=True)),
                ('komponen', models.CharField(blank=True, max_length=50, null=True)),
                ('dimensi', models.CharField(blank=True, max_length=50, null=True)),
                ('nosebuthargaid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.noperolehan')),
            ],
        ),
        migrations.CreateModel(
            name='MRK1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noinden', models.CharField(blank=True, max_length=50, null=True)),
                ('gred', models.CharField(blank=True, max_length=20, null=True)),
                ('kategori', models.CharField(blank=True, max_length=20, null=True)),
                ('pengkhususan', models.CharField(blank=True, max_length=100, null=True)),
                ('tarikhmula', models.CharField(blank=True, max_length=50, null=True)),
                ('tarikhjangkasiap', models.CharField(blank=True, max_length=50, null=True)),
                ('pegawai', models.CharField(blank=True, max_length=100, null=True)),
                ('jawatan', models.CharField(blank=True, max_length=50, null=True)),
                ('kosprojek', models.CharField(blank=True, max_length=100, null=True)),
                ('tarikhdaftar', models.CharField(blank=True, max_length=50, null=True)),
                ('nosebutharga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jpskit.noperolehan')),
            ],
        ),
    ]
