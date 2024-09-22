import json
import os

import requests

CAT_FACTS_URL = "http://catfact.ninja/facts"
N_FACTS = os.getenv("N_FACTS", 10)

TRANSLATION_BASE_URL = os.getenv("TRANSLATION_URL", "http://localhost:8000/")


def fetch_cat_facts() -> list[str]:
    response = requests.get(CAT_FACTS_URL, params={"limit": N_FACTS})
    response.raise_for_status()
    return [fact["fact"] for fact in response.json()["data"]]


def translate_facts(facts: list[str], output_language: str = "French") -> list[str]:
    response = requests.post(
        f"{TRANSLATION_BASE_URL}/translate/batch",
        json=[
            {
                "input_language": "English",
                "output_language": output_language,
                "input_text": fact,
            }
            for fact in facts
        ],
    )
    response.raise_for_status()
    return [response.json()[i]["output_text"] for i in range(len(facts))]


facts = fetch_cat_facts()
translated_facts = translate_facts(facts)
print(json.dumps(translated_facts, ensure_ascii=False, indent=4))
