# Generated by Django 3.2 on 2021-07-05 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attandance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
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
            options={
                'verbose_name_plural': 'Sungai',
            },
        ),
        migrations.CreateModel(
            name='KDvot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(blank=True, max_length=50, null=True)),
                ('budjet', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('tahun', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kontraktor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('konNama', models.CharField(blank=True, max_length=200, null=True)),
                ('konImage', models.FileField(blank=True, null=True, upload_to='')),
                ('konAlamat', models.CharField(blank=True, max_length=300, null=True)),
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
                ('konMPdisemak', models.CharField(blank=True, max_length=100, null=True)),
                ('konMPjawatansemak', models.CharField(blank=True, max_length=50, null=True)),
                ('konMPdisah', models.CharField(blank=True, max_length=100, null=True)),
                ('konMPjawatansah', models.CharField(blank=True, max_length=50, null=True)),
                ('konMPlulus', models.CharField(blank=True, max_length=100, null=True)),
                ('konMPjawatanlulus', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKNoPendaftaran', models.CharField(blank=True, max_length=100, null=True)),
                ('sijilPPKSahDari', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKTamat', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKGredSatu', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKKatSatu', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKKhuSatu', models.CharField(blank=True, max_length=200, null=True)),
                ('sijilPPKGredDua', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKKatDua', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKKhuDua', models.CharField(blank=True, max_length=200, null=True)),
                ('sijilPPKGredTiga', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKKatTiga', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilPPKKhuTiga', models.CharField(blank=True, max_length=200, null=True)),
                ('sijilSPKKNoPendaftaran', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKSahDari', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKTamat', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKGredSatu', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKKatSatu', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKKhuSatu', models.CharField(blank=True, max_length=200, null=True)),
                ('sijilSPKKGredDua', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKKatDua', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKKhuDua', models.CharField(blank=True, max_length=200, null=True)),
                ('sijilSPKKGredTiga', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKKatTiga', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSPKKKhuTiga', models.CharField(blank=True, max_length=200, null=True)),
                ('sijilSTBNoPendaftaran', models.CharField(blank=True, max_length=100, null=True)),
                ('sijilSTBSahDari', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSTBTamat', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSTBGred', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSSMNoPendaftaran', models.CharField(blank=True, max_length=100, null=True)),
                ('sijilSSMSahDari', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSSMTamat', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSSTNoPendaftaran', models.CharField(blank=True, max_length=100, null=True)),
                ('sijilSSTSahDari', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilSSTTamat', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilJPSNoPendaftaran', models.CharField(blank=True, max_length=100, null=True)),
                ('sijilJPSSahDari', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilJPSTamat', models.CharField(blank=True, max_length=50, null=True)),
                ('sijilJPSGred', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MRKKursus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kscode', models.CharField(blank=True, max_length=50, null=True)),
                ('ksname', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MRKSatu',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mrksatunoinden', models.CharField(blank=True, max_length=50, null=True)),
                ('mrksatugred', models.CharField(blank=True, max_length=20, null=True)),
                ('mrksatukategori', models.CharField(blank=True, max_length=20, null=True)),
                ('mrksatupengkhususan', models.CharField(blank=True, max_length=100, null=True)),
                ('mrksatutarikhmula', models.DateField(blank=True, null=True)),
                ('mrksatutarikhjangkasiap', models.DateField(blank=True, null=True)),
                ('mrksatukosprojek', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('mrksatutarikhdaftar', models.DateField(blank=True, null=True)),
                ('mrksatukontraktor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.kontraktor')),
            ],
            options={
                'verbose_name_plural': 'MRK 1',
            },
        ),
        migrations.CreateModel(
            name='NoPerolehan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('noperolehan', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('tarikh', models.DateField(blank=True, null=True)),
                ('kaedahperolehan', models.CharField(blank=True, max_length=50, null=True)),
                ('pegawaiselia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
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
            name='Projek',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tajukkerja', models.CharField(blank=True, max_length=500, null=True)),
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
                ('kodvot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.kdvot')),
                ('nosebuthargaid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.noperolehan')),
            ],
        ),
        migrations.CreateModel(
            name='sistem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistemname', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sokongan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UnitGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('jawatan', models.CharField(blank=True, max_length=50, null=True)),
                ('gredjawatan', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SuratPJaminanbank',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rujukanbank', models.CharField(blank=True, max_length=50, null=True)),
                ('namabank', models.CharField(blank=True, max_length=50, null=True)),
                ('alamatbank', models.CharField(blank=True, max_length=200, null=True)),
                ('alamatpemborongsurat', models.CharField(blank=True, max_length=200, null=True)),
                ('jbankmrksatulink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.mrksatu')),
                ('projekbind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.projek')),
            ],
            options={
                'verbose_name_plural': 'Surat Pelepasan Jaminan Bank',
            },
        ),
        migrations.CreateModel(
            name='SuratPelepasanBon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bonkepada', models.CharField(blank=True, max_length=150, null=True)),
                ('bonalamatsatu', models.CharField(blank=True, max_length=200, null=True)),
                ('bonmelalui', models.CharField(blank=True, max_length=150, null=True)),
                ('bonalamatdua', models.CharField(blank=True, max_length=200, null=True)),
                ('bonwangjaminan', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('bonpegawai', models.CharField(blank=True, max_length=50, null=True)),
                ('bonjawatan', models.CharField(blank=True, max_length=50, null=True)),
                ('bonmrksatulink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.mrksatu')),
                ('projekbind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.projek')),
            ],
            options={
                'verbose_name_plural': 'Surat Bon',
            },
        ),
        migrations.CreateModel(
            name='SuratMRK',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('smrkrujukantuan', models.CharField(blank=True, max_length=50, null=True)),
                ('smrktarikh', models.DateField(blank=True, null=True)),
                ('smrkjenisborang', models.CharField(blank=True, max_length=50, null=True)),
                ('smrknamarujukan', models.CharField(blank=True, max_length=50, null=True)),
                ('smkralamatrujukan', models.CharField(blank=True, max_length=200, null=True)),
                ('smrkpegawai', models.CharField(blank=True, max_length=50, null=True)),
                ('smrkjawatan', models.CharField(blank=True, max_length=50, null=True)),
                ('projekbind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.projek')),
                ('smrkmrksatulink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.mrksatu')),
            ],
            options={
                'verbose_name_plural': 'Surat MRK',
            },
        ),
        migrations.CreateModel(
            name='SuratKhas',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('khasrujukantuan', models.CharField(blank=True, max_length=50, null=True)),
                ('khasnamarujukan', models.CharField(blank=True, max_length=50, null=True)),
                ('khasalamatrujukan', models.CharField(blank=True, max_length=200, null=True)),
                ('khaspegawai', models.CharField(blank=True, max_length=50, null=True)),
                ('khasjawatan', models.CharField(blank=True, max_length=50, null=True)),
                ('khasmrksatulink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.mrksatu')),
                ('projekbind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.projek')),
            ],
            options={
                'verbose_name_plural': 'Surat Khas',
            },
        ),
        migrations.CreateModel(
            name='subsistem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsistemname', models.CharField(blank=True, max_length=100, null=True)),
                ('sistemlink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.sistem')),
            ],
        ),
        migrations.CreateModel(
            name='SenaraiSemakan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ssinden', models.CharField(blank=True, max_length=10, null=True)),
                ('sslsk', models.CharField(blank=True, max_length=10, null=True)),
                ('ssti', models.CharField(blank=True, max_length=10, null=True)),
                ('sssebutharga', models.CharField(blank=True, max_length=10, null=True)),
                ('sspt', models.CharField(blank=True, max_length=10, null=True)),
                ('ssjs', models.CharField(blank=True, max_length=10, null=True)),
                ('sskts', models.CharField(blank=True, max_length=10, null=True)),
                ('ssds', models.CharField(blank=True, max_length=10, null=True)),
                ('ssplm', models.CharField(blank=True, max_length=10, null=True)),
                ('ssab', models.CharField(blank=True, max_length=10, null=True)),
                ('sscidb', models.CharField(blank=True, max_length=10, null=True)),
                ('sspkk', models.CharField(blank=True, max_length=10, null=True)),
                ('ssssm', models.CharField(blank=True, max_length=10, null=True)),
                ('sskk', models.CharField(blank=True, max_length=10, null=True)),
                ('ssinsurance', models.CharField(blank=True, max_length=10, null=True)),
                ('ssgambar', models.CharField(blank=True, max_length=10, null=True)),
                ('sstarikh', models.DateField(blank=True, null=True)),
                ('projekbind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.projek')),
                ('ssmrksatulink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.mrksatu')),
            ],
            options={
                'verbose_name_plural': 'Senarai Semakan',
            },
        ),
        migrations.CreateModel(
            name='PSMK',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('psmknojaminanbanka', models.CharField(blank=True, max_length=50, null=True)),
                ('psmkhargajaminana', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('psmkbakiwangjaminana', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('psmknojaminanbankab', models.CharField(blank=True, max_length=50, null=True)),
                ('psmkhargajaminanb', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('psmkbakiwangjaminanb', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('psmkkosbon', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('psmkbakikos', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('psmkpegawaipenguasa', models.CharField(blank=True, max_length=50, null=True)),
                ('psmkjawatan', models.CharField(blank=True, max_length=50, null=True)),
                ('projekbind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.projek')),
                ('psmkmrksatulink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.mrksatu')),
            ],
            options={
                'verbose_name_plural': 'Perakuan Siap Membaiki Kecacatan',
            },
        ),
        migrations.CreateModel(
            name='PSK',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('psktarikhambilmilik', models.DateField(blank=True, null=True)),
                ('psktarikhmulatanggug', models.DateField(blank=True, null=True)),
                ('psktarikhtamattanggung', models.DateField(blank=True, null=True)),
                ('projekbind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.projek')),
                ('pskmrksatulink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.mrksatu')),
            ],
            options={
                'verbose_name_plural': 'Perakuan Siap Kerja',
            },
        ),
        migrations.CreateModel(
            name='Perakuanpwjp',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rujukantuan', models.CharField(blank=True, max_length=50, null=True)),
                ('rujukankami', models.CharField(blank=True, max_length=50, null=True)),
                ('namarujukan', models.CharField(blank=True, max_length=150, null=True)),
                ('alamatrujukan', models.CharField(blank=True, max_length=200, null=True)),
                ('koswjp', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('wjppegawai', models.CharField(blank=True, max_length=50, null=True)),
                ('wjpjawatan', models.CharField(blank=True, max_length=50, null=True)),
                ('projekbind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.projek')),
                ('wjpmrksatulink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.mrksatu')),
            ],
            options={
                'verbose_name_plural': 'PPWJP',
            },
        ),
        migrations.CreateModel(
            name='MRKTiga',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mrktigabina', models.CharField(blank=True, max_length=50, null=True)),
                ('mrktigatadbir', models.CharField(blank=True, max_length=50, null=True)),
                ('mrktigakemajuan', models.CharField(blank=True, max_length=50, null=True)),
                ('mkrtigamutukerangka', models.CharField(blank=True, max_length=50, null=True)),
                ('mrktigamutukerja', models.CharField(blank=True, max_length=50, null=True)),
                ('mrktigamutukemasan', models.CharField(blank=True, max_length=50, null=True)),
                ('mrktigamutukerjaluar', models.CharField(blank=True, max_length=50, null=True)),
                ('mrktigapegawasan', models.CharField(blank=True, max_length=50, null=True)),
                ('mrkcatat1', models.CharField(blank=True, max_length=150, null=True)),
                ('mrkcatat2', models.CharField(blank=True, max_length=150, null=True)),
                ('mrkcatat3', models.CharField(blank=True, max_length=150, null=True)),
                ('mrkcatat4', models.CharField(blank=True, max_length=150, null=True)),
                ('mrkcatat5', models.CharField(blank=True, max_length=150, null=True)),
                ('mrkcatat6', models.CharField(blank=True, max_length=150, null=True)),
                ('mrkcatat7', models.CharField(blank=True, max_length=150, null=True)),
                ('mrkcatat8', models.CharField(blank=True, max_length=150, null=True)),
                ('mrktigasokongan', models.CharField(blank=True, max_length=500, null=True)),
                ('mrktigatarikh', models.DateField(blank=True, null=True)),
                ('marktigamrksatu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.mrksatu')),
                ('projekbind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.projek')),
            ],
            options={
                'verbose_name_plural': 'MRK 3',
            },
        ),
        migrations.AddField(
            model_name='mrksatu',
            name='projekbind',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.projek'),
        ),
        migrations.CreateModel(
            name='MRKDua',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mrkduakerjajadual', models.CharField(blank=True, max_length=50, null=True)),
                ('mrkduakerjasebenartarikh', models.DateField(blank=True, null=True)),
                ('mrkduakerjasebenar', models.CharField(blank=True, max_length=50, null=True)),
                ('mrkduakemajuan', models.CharField(blank=True, max_length=50, null=True)),
                ('mrkduabayarankemajuan', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('mrkduamodal', models.CharField(blank=True, max_length=50, null=True)),
                ('mkrduabahan', models.CharField(blank=True, max_length=50, null=True)),
                ('mrkduapekerja', models.CharField(blank=True, max_length=50, null=True)),
                ('mrkduatapak', models.CharField(blank=True, max_length=50, null=True)),
                ('mrkduacuaca', models.CharField(blank=True, max_length=50, null=True)),
                ('mrkduadisebabkanoleh', models.CharField(blank=True, max_length=500, null=True)),
                ('mrkdualainlain', models.CharField(blank=True, max_length=500, null=True)),
                ('mrkdualanjutmasa', models.CharField(blank=True, max_length=50, null=True)),
                ('mrkdualanjutdari', models.DateField(blank=True, null=True)),
                ('mrkdualanjutsehingga', models.DateField(blank=True, null=True)),
                ('mrkduadisebabkan', models.CharField(blank=True, max_length=500, null=True)),
                ('mrkduaLAD', models.CharField(blank=True, max_length=50, null=True)),
                ('mrkduaLADdari', models.DateField(blank=True, null=True)),
                ('mrkduaLADSehingga', models.DateField(blank=True, null=True)),
                ('mrkduaperakuan', models.DateField(blank=True, null=True)),
                ('mrkduamansuh', models.DateField(blank=True, null=True)),
                ('mrkduatarikhlaporan', models.DateField(blank=True, null=True)),
                ('mrksatulink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bindone', to='jpskit.mrksatu')),
                ('projekbind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.projek')),
            ],
            options={
                'verbose_name_plural': 'MRK 2',
            },
        ),
        migrations.CreateModel(
            name='Laporansiapkerja',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lskhargasebenar', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('lsklanjutmasa', models.DateField(blank=True, null=True)),
                ('lskkerjasiap', models.DateField(blank=True, null=True)),
                ('lskperuntukan', models.CharField(blank=True, max_length=50, null=True)),
                ('lsklaporan', models.CharField(blank=True, max_length=500, null=True)),
                ('lsktarikhperakui', models.DateField(blank=True, null=True)),
                ('lskketuabahagian', models.CharField(blank=True, max_length=50, null=True)),
                ('lskjawatanketuabahagian', models.CharField(blank=True, max_length=50, null=True)),
                ('lskjuruteraj41', models.CharField(blank=True, max_length=50, null=True)),
                ('lskjawatanj41', models.CharField(blank=True, max_length=50, null=True)),
                ('lskjuruteradaerah', models.CharField(blank=True, max_length=50, null=True)),
                ('lskjawatanjuruteradaerah', models.CharField(blank=True, max_length=50, null=True)),
                ('lskperkeso', models.CharField(blank=True, max_length=50, null=True)),
                ('lskjenisinsurancesatu', models.CharField(blank=True, max_length=50, null=True)),
                ('lsknoinsurancesatu', models.CharField(blank=True, max_length=50, null=True)),
                ('lskjenisinsurancedua', models.CharField(blank=True, max_length=50, null=True)),
                ('lsknoinsurancedua', models.CharField(blank=True, max_length=50, null=True)),
                ('lskmrksatulink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bindtwo', to='jpskit.mrksatu')),
                ('projekbind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.projek')),
            ],
            options={
                'verbose_name_plural': 'Laporan Siap Kerja',
            },
        ),
        migrations.CreateModel(
            name='kosprojek',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kos_belanja', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('kos_tanggung', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('projekbind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.projek')),
            ],
        ),
        migrations.CreateModel(
            name='komponen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_name', models.CharField(blank=True, max_length=100, null=True)),
                ('subidlink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.subsistem')),
            ],
        ),
    ]
