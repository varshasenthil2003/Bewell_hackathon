# Generated by Django 5.0.4 on 2024-05-07 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField(max_length=300)),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('health_number', models.CharField(max_length=100, verbose_name='Health Number')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth (yyyy/mm/dd)')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Sex')),
                ('send_notices_by', models.CharField(choices=[('regular_mail', 'Regular Mail'), ('email', 'Email')], max_length=20, verbose_name="Send notices from my family doctor's office to me by")),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address')),
                ('version_code', models.CharField(max_length=100, verbose_name='Version Code')),
                ('apartment_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Apartment #')),
                ('mailing_address', models.CharField(max_length=100, verbose_name='Mailing Address')),
                ('city_town', models.CharField(max_length=100, verbose_name='City/Town')),
                ('second_name', models.CharField(max_length=100, verbose_name='Second Name')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('street_info', models.CharField(max_length=100, verbose_name='Street No. and Name or P.O. Box, Rural Route, General Delivery')),
                ('postal_code', models.CharField(max_length=100, verbose_name='Postal Code')),
                ('residence_address_same_as_mailing', models.BooleanField(verbose_name='Residence Address same as mailing address')),
                ('residence_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Residence Address')),
            ],
        ),
    ]