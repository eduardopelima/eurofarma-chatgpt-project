from services.transformations import extract_text_from_files
import requests
import streamlit as st

def upload_file_area():
    st.title("Carregador de Arquivos")

    uploaded_file = st.file_uploader("Escolha um arquivo")

    if uploaded_file is not None:
        st.write("Nome do arquivo:", uploaded_file.name)
        st.write("Tipo de arquivo:", uploaded_file.type)
        st.write("Tamanho do arquivo:", uploaded_file.size, "bytes")

        text_from_file = extract_text_from_files(uploaded_file)

        st.text_area('Conteúdo do arquivo', text_from_file)

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
                response = requests.post("http://api:8080/add/archive", json=archive_data)
                
                if response.status_code == 200:
                    st.success("Arquivo adicionado com sucesso!")
                    st.json(response.json())
                else:
                    st.error(f"Falha ao adicionar arquivo: {response.status_code} - {response.text}")
            
            except requests.exceptions.RequestException as e:
                st.error(f"Ocorreu um erro: {e}")

def prompt_area():
    st.title("Área de Prompt")
    user_input = st.text_area("Digite seu prompt aqui:")
    
    if st.button("Enviar Prompt"):
        
        try:
            response = requests.post("http://api:8080/get/prompt_response", params={"question": user_input})
            response_from_api = (response.content).decode('utf-8')
            
            if response.status_code == 200:
                st.text_area('Resposta:', response_from_api)
            else:
                st.error(f"Falha ao adicionar arquivo: {response.status_code} - {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"Ocorreu um erro: {e}")

def main():
    st.sidebar.title("Navegação")
    option = st.sidebar.selectbox("Escolha uma área", ["Carregar Arquivo", "Prompt"])

    if option == "Carregar Arquivo":
        upload_file_area()
    elif option == "Prompt":
        prompt_area()

if __name__ == "__main__":
    main()
