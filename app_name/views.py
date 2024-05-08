from django.shortcuts import render,redirect
# Create your views here.
from .forms import ContactForm
from .pdf_generator import generate_filled_pdf
from django.http import HttpResponse

def success(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save contact details to the database
            form.save()
            # Process signature details here if needed
            contact_data = form.cleaned_data  # Use cleaned_data to get form data
            filled_pdf_content=generate_filled_pdf(contact_data)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="filled_form.pdf"'
            response.write(filled_pdf_content)
            return redirect('success_url')
    else:
        form = ContactForm()
    return render(request, 'success.html', {'form': form})
