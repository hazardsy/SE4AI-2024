import json
import pathlib
from datetime import datetime

from transformers import T5ForConditionalGeneration, T5Tokenizer

from .languages import Language

LOGGING_FILE_PATH = pathlib.Path("./logs/translations.jsonl")
LOGGING_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)


class Translator(object):
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained("google-t5/t5-base")
        self.model = T5ForConditionalGeneration.from_pretrained("google-t5/t5-base")

    def translate(
        self, input_language: Language, output_language: Language, input_text: str
    ) -> str:
        input_ids = self.tokenizer(
            f"translate {input_language.value} to {output_language.value}: {input_text}",
            return_tensors="pt",
        ).input_ids
        outputs = self.model.generate(input_ids)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        with open(LOGGING_FILE_PATH, "a+") as f:
            f.write(
                json.dumps(
                    {
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "input_language": input_language.value,
                        "output_language": output_language.value,
                        "input_text": input_text,
                        "output_text": response,
                    }
                )
            )
            f.write("\n")

        return response


# Create a singleton instance of Translator
translator = Translator()
