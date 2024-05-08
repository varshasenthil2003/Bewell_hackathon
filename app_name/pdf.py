from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import ArrayObject, IndirectObject, NameObject, TextStringObject

pdf_paths = "C:/Users/91948/Downloads/4383-80e-patient-enrolment-eng (1) (1).pdf"

def fill_last_name(pdf_path, output_path, last_name):
    with open(pdf_path, 'rb') as input_file:
        reader = PdfReader(input_file)
        writer = PdfWriter()

        for page in reader.pages:
            annotations = page.get('/Annots', [])
            if isinstance(annotations, IndirectObject):
                annotations = [annotations]
            elif isinstance(annotations, ArrayObject):
                annotations = annotations.getObject()
            for annotation_ref in annotations:
                annotation = reader.get_object(annotation_ref)
                if isinstance(annotation, ArrayObject):
                    for item in annotation:
                        if isinstance(item, IndirectObject):
                            item = reader.get_object(item)
                        if isinstance(item, dict) and item.get('/T') == 'Last\040name\040of\040adult\040submitting\040form':
                            item.update({"/V": TextStringObject(last_name)})
                elif isinstance(annotation, dict) and annotation.get('/T') == 'Last\040name\040of\040adult\040submitting\040form':
                    annotation.update({"/V": TextStringObject(last_name)})
            writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

# Example usage
pdf_path = "C:/Users/91948/Downloads/4383-80e-patient-enrolment-eng (1) (1).pdf"
output_path = "filled_form_S.pdf"
last_name = "varsha"

fill_last_name(pdf_paths, output_path, last_name)
