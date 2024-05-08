import pdfrw
import io

def generate_filled_pdf(data):
    # Load the PDF template
    template_path = "C:/Users/91948/Downloads/4383-80e-patient-enrolment-eng (1) (1).pdf"
    template_pdf = pdfrw.PdfReader(template_path)

    # Access the first page of the PDF template
    page = template_pdf.pages[0]

    # Update form fields with data
    for field, value in data.items():
        # Convert field name to PdfName object
        field_name = pdfrw.PdfName(field)
        # Update form field value
        page[field_name] = value

    # Create a buffer to store the filled PDF content
    filled_pdf_buffer = io.BytesIO()

    # Write the modified PDF content to the buffer
    pdfrw.PdfWriter().write(filled_pdf_buffer, [page])

    # Reset the buffer pointer to the beginning
    filled_pdf_buffer.seek(0)

    # Return the filled PDF content as bytes
    return filled_pdf_buffer.read()