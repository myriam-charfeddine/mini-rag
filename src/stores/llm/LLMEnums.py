from enum import Enum

class LLMEnums(Enum):

    OPENAI = "OPENAI"
    COHERE = "COHERE"

    GEMINI = "GEMINI"
    LLAMA = "LLAMA"

class OpenAIEnum(Enum):
    SYSTEM = "system",
    USER = "user",
    ASSISTANT = "assistant"

class CohereEnum(Enum):
    SYSTEM = "SYSTEM",
    USER = "USER",
    ASSISTANT = "CHATBOT"


