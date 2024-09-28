from .get_client import OpenAIClient
import json

class PromptFilterFileAndResponse:

    def __init__(self, files_list, prompt_question):
        self.files_list = files_list
        self.prompt_question = prompt_question
        self.client_ai = OpenAIClient().client
        self.selected_file_id = None
        self.selected_file_content = None
    
    def get_file_id(self):
        return self.selected_file_id

    def search_file_id(self):

        chat_completion = self.client_ai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system", 
                    "content": (
                        "You are a support system for a company, handling Portuguese questions from employees. "
                        "You will receive a list of metadata for files and need to select the file ID that most closely "
                        "matches the employee's question. Use synonyms and semantic matching to find the best fit. "
                        "If none of the metadata is relevant, return ID 0. The return should be a single integer "
                        "corresponding to the best-matching file ID. "
                        "Example: 'Posso usar chinelo?' should match metadata like 'vestimenta', 'dress code'."
                    )
                },
                {
                    "role": "user", 
                    "content": f"Prompt question: {self.prompt_question}"
                },
                {
                    "role": "user", 
                    "content": f"Files list (metadata): {json.dumps(self.files_list)}"
                }
            ]
        )

        response_content = chat_completion.choices[0].message.content
        
        self.selected_file_id = int(response_content)
 
    def set_selected_file_content(self, file_content):

        self.selected_file_content = file_content

    def get_user_response(self):

        chat_completion = self.client_ai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a support employee for a company. Answer the employee's question strictly based on the following text: {self.selected_file_content}. Do not provide any additional information or interpretations."
                },
                {
                    "role": "user",
                    "content": f"Prompt question: {self.prompt_question}"
                }
            ]
        )

        response_content = chat_completion.choices[0].message.content
        
        return response_content


