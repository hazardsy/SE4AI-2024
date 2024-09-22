from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.get("/hello-world")
def read_root(name: str):
    return {"message": f"Hello {name}"}


@app.post("/posting")
def post_data(data: dict):
    return data
