from abc import ABC, abstractmethod

#an interface is a design for a class structure BUT without any logic

#LLM roles: 1/Embedding => texts to vectors, 2/Generation of text
class LLMInterface(ABC):

    @abstractmethod  #using this DECORATOR make the methode defined by the interface mandatory to be there
    def set_generation_model(self, model_id: str):
        pass #there's no logic since it's an interface (only design)


    @abstractmethod
    def set_embedding_model(self, model_id:str, embedding_size: int):
        pass

    @abstractmethod
    def generate_text(self, prompt: str, chat_history: list = [], max_output_tokens: int = None,
                      temperature: float = None):
        pass

    @abstractmethod
    def embed_text(self, text: str, document_type: str = None):
        pass

    @abstractmethod
    def construct_prompt(self, prompt: str, role: str):
        pass


