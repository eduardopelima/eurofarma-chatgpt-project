from io import StringIO
import PyPDF2

def extract_text_from_files(uploaded_file):

    if uploaded_file.name.endswith(".txt"):
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            return stringio.read()

    elif uploaded_file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        all_text = ""
        for page in pdf_reader.pages:
            all_text += page.extract_text()

        return all_text