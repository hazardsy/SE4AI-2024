from transformers import T5ForConditionalGeneration, T5Tokenizer

from .languages import Language


class Translator(object):
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained("google-t5/t5-small")
        self.model = T5ForConditionalGeneration.from_pretrained("google-t5/t5-small")

    def translate(
        self, input_language: Language, output_language: Language, input_text: str
    ) -> str:
        input_ids = self.tokenizer(
            f"translate {input_language.value} to {output_language.value}: {input_text}",
            return_tensors="pt",
        ).input_ids
        outputs = self.model.generate(input_ids)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


# Create a singleton instance of Translator
translator = Translator()
