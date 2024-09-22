from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .src.languages import Language
from .src.translation import translator

app = FastAPI()


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.get("/translate")
def translate(
    input_language: Language, output_language: Language, input_text: str
) -> str:
    return translator.translate(input_language, output_language, input_text)
