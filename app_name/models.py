from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    content = models.TextField(max_length=300)
    last_name = models.CharField(max_length=100, verbose_name='Last Name', default="")
    health_number = models.CharField(max_length=100, verbose_name='Health Number', default="")
    date_of_birth = models.DateField(verbose_name='Date of Birth (dd/mm/yyyy)', default="2000-01-01")
    sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], verbose_name='Sex', default='M')
    send_notices_by = models.CharField(max_length=20, choices=[('regular_mail', 'Regular Mail'), ('email', 'Email')], verbose_name='Send notices from my family doctor\'s office to me by', default='regular_mail')
    email_address = models.EmailField(verbose_name='Email Address', blank=True, null=True)
    version_code = models.CharField(max_length=100, verbose_name='Version Code', default="")
    apartment_number = models.CharField(max_length=100, verbose_name='Apartment #', blank=True, null=True, default="")
    mailing_address = models.CharField(max_length=100, verbose_name='Mailing Address', default="")
    city_town = models.CharField(max_length=100, verbose_name='City/Town', default="")
    second_name = models.CharField(max_length=100, verbose_name='Second Name', default="")
    first_name = models.CharField(max_length=100, verbose_name='First Name', default="")
    street_info = models.CharField(max_length=100, verbose_name='Street No. and Name or P.O. Box, Rural Route, General Delivery', default="")
    postal_code = models.CharField(max_length=100, verbose_name='Postal Code', default="")
    residence_address_same_as_mailing = models.BooleanField(verbose_name='Residence Address same as mailing address', default=False)
    residence_address = models.CharField(max_length=100, verbose_name='Residence Address', blank=True, null=True, default="")
    agreement = models.BooleanField(verbose_name='I have read and agree to the Patient Commitment, the Consent to Release Personal Health Information, and the Cancellation Conditions', default=False)
    signature = models.CharField(max_length=100, verbose_name='Signature', default="")
    date = models.DateField(verbose_name='Date (dd/mm/yyyy)', default="2000-01-01")
    home_telephone = models.CharField(max_length=20, verbose_name='Home Telephone No.', default="")
    work_telephone = models.CharField(max_length=20, verbose_name='Work Telephone No.', default="")
    doctor_info = models.CharField(max_length=200, default="Dr. Farrell, 123 Hillview St, Oshawa, R1X 3D4", verbose_name='Family Doctor Information')
    appointment_date = models.DateField(verbose_name="Date", default="2000-01-01")

    class Meta:
        app_label='app_name'
