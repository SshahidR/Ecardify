# Generated by Django 5.0.2 on 2024-03-08 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Age', models.IntegerField()),
                ('PhoneNum', models.CharField(max_length=50)),
                ('Designation', models.CharField(max_length=500)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='Register_photos/')),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
            ],
        ),
    ]
