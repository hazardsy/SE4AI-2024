from pydantic import BaseModel

from .languages import Language


class TranslationRequest(BaseModel):
    input_language: Language
    output_language: Language
    input_text: str


class TranslationResponse(BaseModel):
    output_text: str
    output_language: Language
