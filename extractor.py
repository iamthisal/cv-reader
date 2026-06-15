import  pdfplumber

def extract_text(file_path: str ) -> str:
    text_parts = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text_parts.append(page_text)


    return "\n".join(text_parts)
