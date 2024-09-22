from typing import List

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .languages import Language
from .models import TranslationRequest, TranslationResponse
from .translation import translator

app = FastAPI()


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.get("/translate")
def translate(
    input_language: Language, output_language: Language, input_text: str
) -> str:
    return translator.translate(input_language, output_language, input_text)


@app.post("/translate/batch")
def translate_batch(
    translations: List[TranslationRequest],
) -> List[TranslationResponse]:
    return [
        TranslationResponse(
            output_text=translator.translate(
                input_language=request.input_language,
                output_language=request.output_language,
                input_text=request.input_text,
            ),
            output_language=request.output_language,
        )
        for request in translations
    ]
