from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    # Additional fields for the form
    class Meta:
        model = Contact
        fields = ['name', 'email', 'content', 'last_name', 'health_number', 'date_of_birth', 'sex', 'send_notices_by', 'email_address', 'version_code', 'apartment_number', 'mailing_address', 'city_town', 'second_name', 'first_name', 'street_info', 'postal_code', 'residence_address_same_as_mailing', 'residence_address','agreement', 'signature', 'date', 'home_telephone', 'work_telephone','doctor_info','appointment_date']
