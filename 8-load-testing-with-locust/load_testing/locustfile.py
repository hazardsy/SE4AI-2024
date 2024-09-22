import random

import requests
from locust import HttpUser, between, task


class CatFactUser(HttpUser):
    wait_time = between(1, 10)

    @task
    def translate_fact(self):
        self.client.get(
            "/translate",
            params={
                "input_language": "English",
                "output_language": "French",
                "input_text": random.choice(self.cat_facts),
            },
            name="/translate",
        )

    def on_start(self):
        self.cat_facts = [
            fact.get("fact")
            for fact in requests.get("http://catfact.ninja/facts?limit=50").json()[
                "data"
            ]
        ]
