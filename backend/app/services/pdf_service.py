# importing required modules
from pypdf import PdfReader



def pdf_text_extraction(file):

    # creating a pdf reader object
    reader = PdfReader(file)
    # Using a list comprehension is faster and more memory-efficient
    parts = [page.extract_text() for page in reader.pages]
    
    # Join everything once at the end
    return "".join(parts)
