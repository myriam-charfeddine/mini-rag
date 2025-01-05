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


