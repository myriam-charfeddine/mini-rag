import google.generativeai as genai
from ..LLMInterface import LLMInterface
from ..LLMEnums import GoogleEnum
import logging

class GoogleProvider(LLMInterface):
    def __init__(self, api_key: str, api_url: str = None,
                 default_input_max_characters: int = 1000,
                 default_generation_max_output_tokens: int = 1000,
                 default_generation_temperature: float = 0.1):
        
        self.api_key = api_key
        self.api_url = api_url

        self.default_input_max_characters = default_input_max_characters
        self.default_generation_max_ouput_tokens = default_generation_max_output_tokens
        self.default_generation_temperature = default_generation_temperature

        self.generation_model_id = None

        self.embedding_model_id = None
        self.embedding_size = None

        genai.configure(api_key=self.api_key)

        self.enums = GoogleEnum
        self.logger = logging.getLogger(__name__)

    def set_generation_model(self, model_id: str):
        self.generation_model_id = model_id

    def set_embedding_model(self, model_id: str, embedding_size: int):
        self.embedding_model_id = model_id
        self.embedding_size = embedding_size

    def process_text(self, text: str):
        return text[:self.default_input_max_characters].strip()
    
    def generate_text(self, prompt: str, chat_history: list = [], max_output_tokens: int = None,
                      temperature: float = None):
        
        if not self.generation_model_id:
            self.logger.error("Generation model for Google was not set")
            return None
        
        max_output_tokens = max_output_tokens if max_output_tokens else self.default_generation_max_ouput_tokens
        temperature = temperature if temperature else self.default_generation_temperature
        
        chat = genai.GenerativeModel(model_name = self.generation_model_id,
                                        generation_config = genai.GenerationConfig(
                                        max_output_tokens = max_output_tokens,
                                        temperature = temperature,
                                    ))
        
        # chat_history.append(
        #     self.construct_prompt(prompt=prompt, role=GoogleEnum.USER.value)
        # )
        
        response = chat.start_chat(history = chat_history).send_message(self.process_text(prompt))
        
        if not response or not response.text:
            self.logger.error("Error while generating text with Google")
            return None
        
        return response.text

        
    def embed_text(self, text: str, document_type: str = None):

        if not self.embedding_model_id :
            self.logger.error("Embedding model for Google was not set")

        response = genai.embed_content(
        model = self.embedding_model_id,
        content = text
        )

        if not response or not response['embedding']:
            self.logger.error("Error while embedding text with Google")

        return response['embedding']
    
    def construct_prompt(self, prompt: str, role: str):
        return {
            "role": role,
            "parts": self.process_text(prompt)
        }


