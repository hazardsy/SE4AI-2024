from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.get("/hello-world")
def read_root():
    return {"Hello": "World"}


@app.post("/posting")
def post_data(data: dict):
    return data
