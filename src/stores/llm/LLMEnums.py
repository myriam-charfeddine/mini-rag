from enum import Enum

class LLMEnums(Enum):

    OPENAI = "OPENAI"
    COHERE = "COHERE"

    GOOGLE = "GOOGLE"
    LLAMA = "LLAMA"

class OpenAIEnum(Enum):
    SYSTEM = "system",
    USER = "user",
    ASSISTANT = "assistant"

class CohereEnum(Enum):
    SYSTEM = "SYSTEM"
    USER = "USER"
    ASSISTANT = "CHATBOT"

    DOCUMENT = "search_document"
    QUERY = "search_query"

class GoogleEnum(Enum):
    USER = "user"
    ASSISTANT = "model"

class DocumentTypeEnum(Enum):
    DOCUMENT = "document"
    QUERY = "query"


