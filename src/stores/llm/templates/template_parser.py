import os

class TemplateParser:
    def __init__(self, language: str = None, default_language = "en"):
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.default_language = default_language
        self.language = None

        self.set_language(language)

    def set_language(self, language: str):
        if not language:
            self.language = self.default_language
        
        language_path = os.path.join(self.current_path, "locales", language)
        if os.path.exists(language_path):
            self.language = language

        else:
            self.language = self.default_language

    def get(self, group: str, key: str, vars: dict = {}):
        # group == file were the prompts templates are located (rag.py file in our case)
        # key == the concerned prompt (e.g: system_prompt, document_prompt, ...)

        if not group or not key:
            return None

        
    
        
