from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='pages')


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/message")
async def message(request: Request, text=Form()):
    return templates.TemplateResponse(request=request, name="answer.html", context={"message": text})
