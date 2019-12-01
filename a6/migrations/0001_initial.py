# Generated by Django 2.0 on 2019-10-23 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_status', models.BooleanField(default=False)),
                ('payment_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avail_date', models.DateField()),
                ('start_time', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=100)),
                ('symptoms', models.CharField(max_length=200)),
                ('status', models.CharField(default='active', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('qualification', models.CharField(blank=True, max_length=100)),
                ('speciality', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=10)),
                ('clinic', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('birthdate', models.DateField()),
                ('location', models.CharField(blank=True, max_length=30)),
                ('about_doc', models.CharField(blank=True, max_length=100)),
                ('profile_pic', models.FileField(default='doc_male.png', upload_to='doctorfinder/img/')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uplaod_image', models.ImageField(upload_to='Image/')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('birthdate', models.DateField()),
                ('blood_group', models.CharField(blank=True, max_length=10)),
                ('blood_presure', models.CharField(blank=True, max_length=10)),
                ('sugar', models.CharField(blank=True, max_length=10)),
                ('Haemoglobin', models.CharField(blank=True, max_length=10)),
                ('profile_pic', models.FileField(default='patient_icon.png', upload_to='doctorfinder/img/')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('customer_id', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_file', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('case_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a6.Case')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a6.Doctor')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a6.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('otp', models.IntegerField(default=459)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verfied', models.BooleanField(default=False)),
                ('role', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='payments',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a6.User'),
        ),
        migrations.AddField(
            model_name='patient',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a6.User'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a6.User'),
        ),
        migrations.AddField(
            model_name='case',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a6.Doctor'),
        ),
        migrations.AddField(
            model_name='case',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a6.Patient'),
        ),
        migrations.AddField(
            model_name='availability',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a6.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='availability_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='a6.availability'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a6.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a6.Patient'),
        ),
    ]