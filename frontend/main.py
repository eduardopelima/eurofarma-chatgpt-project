from services.transformations import extract_text_from_files
import requests
import streamlit as st

def main():
    st.title("File Uploader")

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        st.write("Filename:", uploaded_file.name)
        st.write("File type:", uploaded_file.type)
        st.write("File size:", uploaded_file.size, "bytes")

        text_from_file = extract_text_from_files(uploaded_file)

        st.text_area('File content', text_from_file)

        categoria = st.text_input("Categoria", max_chars=50)
        nome = st.text_input("Nome", max_chars=50)
        descricao = st.text_input("Descrição", max_chars=1000)

        prosseguir = st.button('Prosseguir')

        if prosseguir:
            archive_data = {
                "categoria": categoria,
                "nome": nome,
                "descricao": descricao,
                "conteudo": text_from_file
            }
        
            try:
                response = requests.post("http://127.0.0.1:8000/add/archive", json=archive_data)
                
                if response.status_code == 200:
                    st.success("Archive successfully added!")
                    st.json(response.json())
                else:
                    st.error(f"Failed to add archive: {response.status_code} - {response.text}")
            
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
